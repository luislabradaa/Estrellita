import time
import network 
from umqtt.simple import MQTTClient
from machine import Pin, ADC, PWM
import dht

#*************************************** PINES BUZER & SENSOR SONIDO *******************************************
# Pin buzzer
pin_zumbador = Pin(21, Pin.OUT)
zumbador_pwm = PWM(pin_zumbador, freq=1000, duty=0)
# Pin del sensor de sonido KY-038 
sound_sensor = ADC(Pin(32))
THRESHOLD = 230

#*************************************** PINES FOTORRESISTENCIA & LED RGB *******************************************
# Pin fotorresistencia
pin_ldr = Pin(4, Pin.IN)
# Led RGB
pin_led_r = Pin(12, Pin.OUT)  
pin_led_g = Pin(13, Pin.OUT)  
pin_led_b = Pin(14, Pin.OUT) 

#*************************************** PINES SENSOR TEMP & MOTO DC *******************************************
# Pin temperatura
pin = Pin(2)  
# Inicializa el sensor DHT11
sensor = dht.DHT11(pin)
#Pin motor
pin_rele_motor = Pin(18, Pin.OUT)

#*************************************** CONFIGURACIONES MQTT *******************************************
# Configuración MQTT
MQTT_BROKER = "192.168.137.147"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC_RUIDO = "ruido"
MQTT_TOPIC_TEMP = "temperatura"
MQTT_TOPIC_LUZ = "luz"
MQTT_TOPIC_BUZZER = "buzzer"
MQTT_TOPIC_VENT = "ventilador"
MQTT_TOPIC_LED = "led"
MQTT_PORT = 1883

# Función para conectar a la red wifi
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

# ***************************************** CODIGO SONIDO Y BUZZER ***********************************************
# Función para detectar el sonido
def detect_ruido():
    sound_value = sound_sensor.read()
    return sound_value;

# Función de publicación de ruido
def publish_ruido():
    ruido_value = detect_ruido()  
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=30)
    client.connect()
    client.publish(MQTT_TOPIC_RUIDO, str(ruido_value))
    time.sleep(1)
    client.disconnect()
    print("ruido ",ruido_value)
    
      # Reproducir la canción si se cumple la condición
    if ruido_value > THRESHOLD < 600:
        tocar_cancion()
 
 # Función para suscribirse al tópico "buzzer" y manejar los mensajes
def subscribe_buzzer():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=0)
    client.set_callback(message_buzzer)
    client.connect()
    client.subscribe(MQTT_TOPIC_BUZZER)
    print("Connected on %s, topic subscribed %s" % (MQTT_BROKER, MQTT_TOPIC_BUZZER))
    return client

# Función que se llama cuando llega un mensaje al tópico "buzzer"
def message_buzzer(topic, msg):
    msg = msg.decode()
    if topic == b'buzzer':
        print("mensaje decodificado: ", msg)
        if msg == 'true':
            tocar_cancion()
        else:
            pin_zumbador.off()
           
# Define las notas y sus duraciones para la canción "Twinkle, Twinkle, Little Star"
cancion = [
    ("C4", 500),
    ("C4", 500),
    ("G4", 500),
    ("G4", 500),
    ("A4", 500),
    ("A4", 500),
    ("G4", 1000),
    ("F4", 500),
    ("F4", 500),
    ("E4", 500),
    ("E4", 500),
    ("D4", 500),
    ("D4", 500),
    ("C4", 1000),
    ("C4", 500),
    ("C4", 500),
    ("G4", 500),
    ("G4", 500),
    ("A4", 500),
    ("A4", 500),
    ("G4", 1000),
    ("F4", 500),
    ("F4", 500),
    ("E4", 500),
    ("E4", 500),
    ("D4", 500),
    ("D4", 500),
    ("C4", 1000),
]

# Función para reproducir una nota en el zumbador
def tocar_nota(nota, duracion):
    notas = ["C", "D", "E", "F", "G", "A", "B"]
    octava = int(nota[1])  # Obtiene el número de octava de la nota
    frecuencia = 1000.0 * (2 ** ((octava - 4) + (notas.index(nota[0]) / 12.0)))
    zumbador_pwm.freq(int(frecuencia))
    zumbador_pwm.duty(50)  # Ajusta el ciclo de trabajo para un volumen adecuado
    time.sleep_ms(duracion)
    zumbador_pwm.duty(0)

# Función para tocar la canción completa
def tocar_cancion():
    for nota, duracion in cancion:
        tocar_nota(nota, duracion)
        time.sleep_ms(50)  
    
# ***************************************** CODIGO FOTORESISTENCIA Y LED RGB ***********************************************
# Función para leer fotorresistencia
def read_ldr():
    return pin_ldr.value()

# Función de publicación de luz
def publish_luz():
    luz_value = read_ldr()  
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=30)
    client.connect()
    client.publish(MQTT_TOPIC_LUZ, str(luz_value))
    time.sleep(1)
    client.disconnect()
    print("luz ", luz_value)
    
    if luz_value == 1:
        pin_led_r.value(0) 
        pin_led_g.value(0)  
        pin_led_b.value(0)  
    else:
        pin_led_r.value(1)  
        pin_led_g.value(1)
        pin_led_b.value(1)
            
# Función para suscribirse al tópico "luz" y manejar los mensajes
def subscribe_led():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=0)
    client.set_callback(message_led)
    client.connect()
    client.subscribe(MQTT_TOPIC_LED)
    print("Connected on %s, topic subscribed %s" % (MQTT_BROKER, MQTT_TOPIC_LED))
    return client

# Función que se llama cuando llega un mensaje al tópico "luz"
def message_led(topic, msg):
    if topic == b'led':
        msg = msg.decode()
        print(msg)
        if msg == 'false':
            pin_led_r.value(0)  
            pin_led_g.value(0)
            pin_led_b.value(0)
        else:
            pin_led_r.value(1) 
            pin_led_g.value(1)  
            pin_led_b.value(1)
            
# ***************************************** CODIGO TEMPERATURA & VENTILADOR MOTOR DC ***********************************************
# Función para leer la temperatura desde el sensor
def leer_temperatura():
    sensor.measure()
    temperatura = sensor.temperature()
    return temperatura


# Función de publicación de temperatura
def publish_temp():
    temp_value = leer_temperatura()  
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=30)
    client.connect()
    client.publish(MQTT_TOPIC_TEMP, str(temp_value))
    time.sleep(1)
    client.disconnect()
    print("temp ", temp_value)
    
    if temp_value > 26:
        pin_rele_motor.on()
    else:
        pin_rele_motor.off()

        time.sleep(2)

# Función para suscribirse al tópico "temp" y manejar los mensajes
def subscribe_vent():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=0)
    client.set_callback(message_vent)
    client.connect()
    client.subscribe(MQTT_TOPIC_VENT)
    print("Connected on %s, topic subscribed %s" % (MQTT_BROKER, MQTT_TOPIC_VENT))
    return client

# Función que se llama cuando llega un mensaje al tópico "buzzer"
def message_vent(topic, msg):
    if topic == b'ventilador':
        msg = msg.decode()
        print(msg)
        if msg == 'true':
            pin_rele_motor.on()
        else:
            pin_rele_motor.off()

        time.sleep(2)

# ***************************************** BUCLES PRINCIPALES ***********************************************
# Bucle principal
client = subscribe_buzzer()
client2 = subscribe_led()
client3 = subscribe_vent()

# ***************************************** WHILE TRUE  ***********************************************
while True:    
    publish_luz()
    publish_temp()
    publish_ruido() 
    client.check_msg()
    client2.check_msg()
    client3.check_msg()
    time.sleep(1)  
