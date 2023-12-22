# TempMonitor

---
## Inhaltverzeichnis

## 1. Einleitung

Das Tempmonitor-Projekt ist eine Implementierung eines Webservers, der als API-Endpunkt zum Senden von Temperatur- 
und Feuchtigkeitsdaten von einem ESP32-Mikrocontroller dient. Der Mikrocontroller verwendet einen Sensor, um die Temperaturdaten zu lesen und führt dann API-Aufrufe an den Webserver aus,
um die Daten in einen SQL-Server zu schreiben und sie dann visuell auf der Webseite darzustellen. Diese Readme-Datei dient als Dokumentation des Prozesses der Konfiguration des Servers, der Installation der notwendigen Software zum Betrieb des Servers, der Programmierung des Backends mit dem Flask-Framework, der Programmierung des Mikrocontrollers zum 
Lesen und Senden der Daten und der Programmierung des Frontends für die visuelle Darstellung der Daten.

