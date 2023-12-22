#include "DHT.h"
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <AsyncTCP.h>

#define DHTPIN 4     // Digital pin connected to the DHT sensor

#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321

DHT dht(DHTPIN, DHTTYPE);

// Wifi log in data
const char* ssid = "BBS-TuG";
const char* password = "Ausbildung";

String serverName = "http://pinghero.online/add";

unsigned long lastTime = 0;
// Delay between readings
unsigned long timerDelay = 5000;

void setup() {
  Serial.begin(9600);
  Serial.println(F("DHTxx test!"));

  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print("--");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network ");

  dht.begin();
}

void loop() {
  delay(5000);

  // Read humidity
  float h = dht.readHumidity();
  // Read temperature as Celsius
  float t = dht.readTemperature();

  // Check if any reads failed and exit early .
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  } else {
    //Check WiFi connection status
    if(WiFi.status()== WL_CONNECTED){
      HTTPClient http;
      // Header for basic auth
      http.addHeader("Authorization", "Basic YWRtaW46cGFzc3dvcmQ=")
      http.addHeader("Content-Type", "application/json");
      http.addHeader("accept", "application/json");
      String serverPath = serverName;
      // Create request body
      StaticJsonDocument<200> doc;
      doc["temperature"] = String(t);
      doc["humidity"] = String(h);
      doc["location"]= String(f);

      String requestBody;
      serializeJson(doc,requestBody);

      http.begin(serverPath.c_str());

      int httpResponseCode = http.POST(requestBody);

      if (httpResponseCode>0) {
        Serial.print("HTTP Response code: ");
        Serial.println(httpResponseCode);
        String payload = http.getString();
        Serial.println(payload);
      }
      else {
        Serial.print("Error code: ");
        Serial.println(httpResponseCode);
      }
      // Free resources
      http.end();
    }
    else {
      Serial.println("WiFi Disconnected");
    }
    lastTime = millis();
  }

}