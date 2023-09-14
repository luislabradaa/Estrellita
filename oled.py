import time
import network 
from umqtt.simple import MQTTClient
from machine import Pin, I2C, ADC, PWM
import ssd1306
import ujson

# ESP32 Pin assignment 
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

VIBRA_PIN = 23
vibrator_pin = Pin(VIBRA_PIN, Pin.OUT) 
vibrator_pin.off()

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Configuración MQTT
MQTT_BROKER = "192.168.137.147"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC_RUIDO = "ruido"
MQTT_TOPIC_TEMP = "temperatura"
MQTT_PORT = 1883

#Función para conectar a la red wifi
def wifi_connect():
    print("Connecting...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('TUFLL9255', '272@Hu22')

    while not sta_if.isconnected():
        print(".", end="")
        time.sleep(0.5)
    print("Wifi connection!")

wifi_connect()

# Función para activar el vibrador
def activate_vibrator():
    vibrator_pin.on() 
    time.sleep(3)    
    vibrator_pin.off()

#Subscribe to mqtt
def subscribe_temp():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=0)
    client.set_callback(message_temp)
    client.connect()
    client.subscribe(MQTT_TOPIC_TEMP)

    return client

# SUBCRIPCION
def message_temp(topic, msg):
    print("holaaaa")
    if topic == b'temperatura':
        print(msg.decode())
        oled.fill(0)  # Limpiar la pantalla OLED
        oled.text("Temperatura:", 0, 20)
        oled.text(msg.decode(), 0, 40)
        oled.show()
        
#Subscribe to mqtt
def subscribe_ruido():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=0)
    client.set_callback(message_ruido)
    client.connect()
    client.subscribe(MQTT_TOPIC_RUIDO)

    return client

# SUBCRIPCION
def message_ruido(topic, msg):
    if topic == b'ruido' and int(msg) > 230 :
        oled.fill(0)  # Limpiar la pantalla OLED
        oled.text("El bebe", 0, 20)
        oled.text("esta llorando", 0, 30)
        oled.show()
        activate_vibrator()
        

client = subscribe_temp()
client2 = subscribe_ruido()

while True:
    client.check_msg()
    client2.check_msg()
    time.sleep(1)