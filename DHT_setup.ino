#include "DHT.h"
#define DHTTYPE DHT22

const int DHTPin = 4;
long now = millis();
long lastMeasure = 0;

DHT dht(DHTPin, DHTTYPE);

void setup() {
  dht.begin();
  
  Serial.begin(115200);
}

void loop() {
  now = millis();
  if (now - lastMeasure > 5000) {
    lastMeasure = now;
    float t = dht.readTemperature();
    Serial.print(" My Temperature measurement is: ");
    Serial.print(t);
  }
}
