# TempMonitor

<p align="center">
  <img src="./img/website.png" alt="pinghero.online" width="650">
</p>

## Inhaltverzeichnis

## 1. Einleitung

Das Tempmonitor-Projekt ist eine Implementierung eines Webservers, der als API-Endpunkt zum Senden von Temperatur- 
und Feuchtigkeitsdaten von einem ESP32-Mikrocontroller dient.Der Mikrocontroller verwendet einen Sensor, um die Temperaturdaten zu lesen und führt dann API-Aufrufe an den Webserver aus,
um die Daten in einen SQL-Server zu schreiben und sie dann visuell auf der Webseite darzustellen. Diese Readme-Datei dient als Dokumentation des Prozesses der Konfiguration des Servers, der Installation der notwendigen Software zum Betrieb des Servers, der Programmierung des Backends mit dem Flask-Framework, der Programmierung des Mikrocontrollers zum 
Lesen und Senden der Daten und der Programmierung des Frontends für die visuelle Darstellung der Daten.

## 2. Server Konfiguration
Der erste Schritt bestand darin, einen virtuellen Server bei einem Hosting-Anbieter zu mieten. Wir wurden angewiesen, den Server mit der geringsten RAM- und Festplattenkapazität zu wählen, da das Projekt nicht viel von diesen Ressourcen benötigt.

Der von mir gewählte virtuelle Server hat die folgenden Eigenschaften:
<table>
  <tr>
    <th>Host</th>
    <td> <a href="https://www.ionos.de/">IONOS</a> </td>
  </tr>
  <tr>
    <th>Betriebssystem</th>
    <td>Ubuntu 22.04</td>
  </tr>
  <tr>
    <th>CPU</th>
    <td>1 vCore</td>
  </tr>
  <tr>
    <th>RAM</th>
    <td>1 GB</td>
  </tr>
  <tr>
    <th>Datenträger</th>
    <td>10 GB SSD</td>
  </tr>
</table>

Nachdem die Anmietung abgeschlossen war, erhielt ich die Root-Benutzeranmeldeinformationen für meinen V-Server.

### 2.1 Benutzer-Konfiguration
Der Serveranbieter stellte mir ein SSH-Passwort für den Root-Benutzer zur Verfügung. Da die Kennwortauthentifizierung anfällig für Brute-Force-Angriffe ist, wurden wir angewiesen, einen Linux-Benutzer zu erstellen, der sich über eine schlüsselbasierte Authentifizierung beim Server anmelden kann.

Um dies zu erreichen, mussen wir uns zunächst mit den Anmeldedaten am Server per SSH anmelden:  
```Console
pinghero@desktop:~$ ssh root@server-ip
```
Nach Eingabe des Passworts in die Eingabeaufforderung habe ich mich erfolgreich mit dem Server verbunden.

### 2.1.1 Neuen Benutzer anlegen
Nach erfolgreicher Verbindung zum Server musste ein neuer Benutzer angelegt werden.  
Dies kann mit folgendem Linux-Befehl erreicht werden:
```Console
root@ubuntu:~$ adduser <username>
```
Nachdem der Befehl ausgeführt wurde, wurde aufgefordert, ein Benutzerpassword zu erstellen. Danach wurde der neue Benutzer erstellt.

Damit der neue Benutzer administrative Befehle auf dem Server ausführen kann, benötigt er sudo-Rechte. Zu diesem Zweck mussen wir den Benutzer zur sudo-Benutzergruppe hinzufügen. Dazu führen wir den Befehl aus:
```Console
root@ubuntu:~$ usermod -aG sudo <username>
```
### 2.1.2 SSH-Schlüssel-Generierung
Um sicherzustellen, dass der Server gegen mögliche Angriffe geschützt ist, ist eine Authentifizierung mit SSH-Schlüssel erforderlich.  
Dazu müssen wir zunächst ein RSA-Schlüsselpaar auf dem Gerät erstellen, von dem aus wir eine Verbindung herstellen wollen.  
Dies kann je nach verwendetem Betriebssystem unterschiedlich sein. In meinem Fall habe ich WSL2 auf meinem Computer verwendet, um eine Verbindung zu meinem Server herzustellen

Lokal auf dem Gerät:
```Console
pinghero@desktop:~$ ssh-keygen
```
Ausgabe:
```Console
Generating public/private rsa key pair.
Enter file in which to save the key (/home/pinghero/.ssh/id_rsa):
```
Wir können den gewünschten Dateipfad für unseren SSH-Schlüssel eingeben oder die Eingabetaste drücken, um den Standardschlüssel zu verwenden.

Wir werden dann aufgefordert, ein Passwort für unseren Schlüssel zu vergeben. Dies ist optional.
```Console
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
```
Nach der Eingabe eines Passworts oder dem Weglassen des Passworts wird der Schlüssel generiert.
```Console
Your identification has been saved in /home/pinghero/.ssh/id_rsa
Your public key has been saved in /home/pinghero/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:dpAQh2tQRp3skIEcli3uEKoMYQ72Iixezt+uBJOwdjI pinghero@desktop
The key's randomart image is:
+---[RSA 3072]----+
|   .oBBB..       |
|oo..*.=o+.       |
|*+.o o +o        |
|=++oo o ..       |
|BE=B .  S .      |
|oo+o+  . .       |
|    ...          |
|    .. .         |
|     .o.         |
+----[SHA256]-----+
```

Nachdem wir den SSH-Schlüssel erfolgreich generiert haben, müssen wir ihn für unseren neuen Benutzer auf den Server kopieren. Dazu können wir das tool ```ssh-copy-id``` verwenden, das in den meisten Linux-Distributions standardmäßig enthalten ist.

Um das Dienstprogramm ssh-copy-id zu verwenden, geben wir den entfernten Host (unseren Server) und den Benutzer an, zu dem wir passwortbasierten SSH-Zugang haben.

```Console
pinghero@desktop:~$ ssh-copy-id username@server-ip
```

Daraufhin wird folgende Meldung angezeigt:
```Console
Output
The authenticity of host 'server-ip (server-ip)' can't be established.
ECDSA key fingerprint is fd:fd:d4:f9:77:fe:73:84:e1:55:00:ad:d6:6d:22:fe.
Are you sure you want to continue connecting (yes/no)? yes
```
Das bedeutet, dass unser lokales System den Server nicht erkennt. Durch die Eingabe von ```yes``` entscheiden wir uns, diesem Server zu vertrauen.

Ausgabe:

```Console
Output
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
username@203.0.113.1's password:
```

Nach der Eingabe des neuen Benutzerkennworts erhalten wir die folgende Meldung:
```Console
Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'username@server-ip'"
and check to make sure that only the key(s) you wanted were added.
```

Das bedeutet, dass wir unseren Schlüssel erfolgreich kopiert haben und uns nun mit ihm anmelden können.

### 2.1.3 Deaktivierung der passwortbasierten Authentifizierung
Although we configured a SSH-Key for out new user,
Obwohl wir einen SSH-Schlüssel für unseren neuen Benutzer konfiguriert haben,
ist eine passwortbasierte Authentifizierung weiterhin möglich. Um sie zu deaktivieren, müssen wir uns zunächst mit unserem Server verbinden und die SSH-Konfigurationsdatei bearbeiten.

Um die SSH-Konfigurationsdatei zu öffnen:
```Console
<username>@ubuntu:~$ vim /etc/ssh/sshd_config
```
Dann müssen wir die Option ```PasswordAuthentication``` auf ```no``` ändern.  
Da wir nun einen neuen Benutzer haben, der sich mit dem Server verbinden kann und sudo-Rechte hat, können wir den Root-Authentifizierung komplett deaktivieren, um unseren Server weiter vor möglichen Angriffen zu schützen. Zu diesem Zweck ändern wir ```PermitRootLogin``` auch auf ```no```.   
Damit die Änderungen durchgeführt werden können, starten wir den SSH-Dienst neu mit ```sudo systemctl restart ssh```.  
Jetzt können wir uns nur noch mit unserem Benutzer und dem generierten SSH-Schlüssel verbinden.

### 2.2 Domain-Konfiguration
Jetzt kann unser Server von einem Browser über seine IP-Adresse erreicht werden. Wir können das ändern, indem wir die IP-Adresse mit einem Domänennamen verknüpfen. Dazu müssen wir die DNS-Einträge ändern. Dies ist je nach Anbieter unterschiedlich, aber in der Regel hat der Anbieter eine Webseite mit DNS-Einstellungen. Dort müssen wir die A-Einträge so ändern, dass sie auf unsere Server-IP-Adresse verweisen.

### 2.3 Reverse-Proxy-Konfiguration
Um unseren Server dem Internet auszusetzen und später die verschiedenen HTTP-Anfragen, die wir erhalten, weiterzuleiten, verwenden wir eine Reverse-Proxy-Lösung.  

In meinem Fall habe ich mich für NGNIX entschieden, einen beliebten Webserver und Reverse Proxy Lösung.

### 2.3.1 NGNIX Installation
Als erstes müssen wir NGNIX auf unserem Server installieren:    
```Console
pinghero@ubuntu:~$ sudo apt install nginx
```

So überprüfen Sie, ob NGNIX installiert ist und läuft:  
```Console
pinghero@ubuntu:~$ sudo systemctl status nginx
```
Ausgabe:
```Console
Output
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Mon 2022-08-29 06:52:46 UTC; 39min ago
       Docs: man:nginx(8)
   Main PID: 9919 (nginx)
      Tasks: 2 (limit: 2327)
     Memory: 2.9M
        CPU: 50ms
     CGroup: /system.slice/nginx.service
             ├─9919 "nginx: master process /usr/sbin/nginx -g daemon on; master_process on;"
             └─9920 "nginx: worker process
```

### 2.3.2 NGNIX Konfiguration
Wir müssen einen benutzerdefinierten Serverblock mit unserer Domain und dem Proxy für den Anwendungsserver hinzufügen.  
Damit wird NGNIX im Wesentlichen mitgeteilt, welche Ports es abhören und welche Webseiten es bei einer Anfrage bereitstellen soll.  

Zu diesem Zweck erstellen wir eine neue Konfigurationsdatei für NGNIX:
```Console
pinghero@ubuntu:~$ sudo vim /etc/nginx/sites-available/tempmonitor
```

Dann fügen wir Folgendes in die Datei ein:  
```Console
server {
    listen 80;
    listen [::]:80;

    server_name pinghero.online www.pinghero.online;
        
    location / {
        proxy_pass http://127.0.0.1:8000;
        include proxy_params;
    }
}
```
Dadurch wird NGNIX angewiesen, Port 80 (HTTP-Port) abzuhören und an localhost weiterzuleiten. Da das HTTP-Protokoll unverschlüsselt ist, müssen wir ein SSL-Zertifikat hinzufügen, um die HTTPS-Kommunikation zu ermöglichen. Dies wird später erklärt unter HIERHIER.  

Wir sollten NGNIX auch anweisen, die Anfragen an unsere Anwendung statt an localhost weiterzuleiten. Dies wird auch später unter HIERHIER erklärt.

Schließlich müssen wir eine Verknüpfung zwischen der Konfigurationsdatei und der Datei ```sites-enabled``` herstellen, die NGINX beim Start liest:
```Console
pinghero@ubuntu:~$ sudo ln -s /etc/nginx/sites-available/tempmonitor /etc/nginx/sites-enabled/
```
Und den NGINX-Dienst neu starten:
```Console
pinghero@ubuntu:~$ sudo systemctl restart nginx
```

### 2.4 Flask und Gunicorn Anwendungsserver
Unser Backend wird mit Python und insbesondere mit dem Flask-Framework verwaltet. Um dies zu erreichen, müssen wir Flask auf unserem Server installieren, um eine Anwendung zu erstellen und Gunicorn, einen Python WSGI HTTP Server, zu konfigurieren, der unsere Anwendung bedient.

### 2.4.1 Erstellung einer virtuellen Umgebung
Da Python und PIP bereits installiert sind, müssen wir eine virtuelle Umgebung erstellen, in der wir alle notwendigen Pakete für unsere Anwendung, einschließlich Flask, installieren werden.  

Zunächst müssen wir das Modul ```python-venv``` installieren. Um dies zu tun:
```Console
pinghero@ubuntu:~$ sudo apt install python3-venv
```
Nachdem die Installation abgeschlossen ist, erstellen wir ein Verzeichnis für unsere Flask-Anwendung:
```Console
pinghero@ubuntu:~$ mkdir ~/tempmonitor
pinghero@ubuntu:~$ cd ~/tempmonitor
```

Innerhalb des neu erstellten Verzeichnisses erstellen wir dann eine virtuelle Umgebung mit der Name ```venv```:
```Console
pinghero@ubuntu:~$ python3 -m venv venv
```

Und aktivieren sie mit:
```Console
pinghero@ubuntu:~$ source myprojectenv/bin/activate
```

Ausgabe:
```Console
(venv) pinghero@ubuntu:~$
```
Das ```venv``` am Anfang bestätigt, dass wir uns in einer virtuellen Umgebung befinden und wir können mit der Installation aller notwendigen Pakete beginnen.

### 2.4.2 
