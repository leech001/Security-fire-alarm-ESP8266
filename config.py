from m_sensor import MS
from machine import Pin

ntp_delta = 3155673600
host = "pool.ntp.org"
ms = MS(5)  # Motion sensor (pin)
led = Pin(2, Pin.OUT)

# Modify below section as required
CONFIG = {
    "MQTT_BROKER": "1.1.1.1",
    "MQTT_USER": "user",
    "MQTT_PASSWORD": "pass",
    "MQTT_PORT": 1883,
    "MQTT_CLIENT_ID": "ESP_18_01",
    "MQTT_MAX_ERR": 5,
    "MQTT_CRIT_ERR": 10,
    "DEVICE_TYPE": "smoke",
    "DEVICE_PLACE": "Home/18",
    "DEVICE_PLACE_TYPE": "kitchen",
    "DEVICE_PLACE_NAME": "main",
    "DEVICE_ID": "01",
    "DEVICE_ID_USE": "01",
    "WIFI_LOGIN": "APP_NAME",
    "WIFI_PASSWORD": "APP_PASS",
    "INT_MAX_ERR": 20,
    "INT_CRIT_ERR": 50
}
