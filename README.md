# ESTRELLITA
## Objetivo del proyecto
Estrellita tiene como objetivo crear un dispositivo para el monitoreo y cuidado de los bebés para los padres de familia, aumentando la productividad al evitar pasar todo el tiempo con el bebé mientras se desee realizar otra actividad. 

## Objetivos específicos:
Mejorar la seguridad y el bienestar de las madres de familia y padres al proporcionar monitoreo en tiempo real sobre situaciones del estado del bebé.
Reducir el tiempo de presencia del cuidado del bebé cuando sea necesario para aumentar la productividad de los padres de familia al desarrollar otras actividades mientras el bebé esta siendo monitoreado por Estrellita.

## Beneficiario
 - Angelica Mendoza Ramírez

## Integrantes
- Pedro Emmanuel Martinez Rodriguez 
- María Guadalupe Mendoza Ramírez
- Juan Luis Negrete Labrada
- Paola Guadalupe Patlán Gónzalez


## Componentes empleados
| No. | Componente | Descripción | Img | Costo | Cantidad |
|-----|------------|-------------|-----|-------|----------|
|1| Sensor de temperatura| Modulo Ky-001 Sensor De Temperatura |<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/42fcd6e5-30ac-4b3a-b80c-49a1fb623dbf" width= "200px"/> |$42| 1|

## Software utilizado
| Id | Software | Version | Tipo |Funcionalidad|
|----|----------|---------|------|-------------|
| 1 | Fritzing | 0.9.3 |Licencia libre|Modelado|
| 2 | Wokwi    | N/A | Licencia libre | Programación / Modelado|
| 3 | Node-RED | 3.0.2 | Licencia libre| Programación|
| 4 | Tinkercad | N/A |Licencia libre|Modelado 3D |
| 5 | Librería NewPing |N/A|Licencia libre|Para sensores ultrasónicos, incluyendo el HC-SR04.|
| 6 | Libreria machine|N/A|Licencia Libre| Proporciona una interfaz para interactuar con el hardware del microcontrolador|
| 7 | Libreria time | N/A | Licencia Libre| ofrece funciones para trabajar con medidas de tiempo.|
| 8 | Libreria network | N/A| Licencia Libre| permite la configuración y gestión de conexiones de red en el microcontrolador|
| 9 | Libreria umqtt | N/A| Licencia Libre| está diseñada para admitir el protocolo MQTT (Message Queuing Telemetry Transport) en entornos de MicroPython.| 

## Historias de Usuario
| Id | Historia de usuario | Prioridad | Estimación | Cómo probarlo | Responsable | Sprint |
|----|---------------------|-----------|------------|---------------|-------------|--------|
|HU01|Yo como taquero quiero que el mandil me alerte mediante un sonido cuando este se esté comenzando a incendiar, para poder tomar acciones inmediatas y que el resto de los cocineros pueda darse cuenta y ayudarme, pues siempre estoy muy ocupado y algunas veces no detecto el fuego hasta que este ya se ha extendido en la mayoría del mandil.|Debe| 1 |Se enciende una llama a 5 cm del sensor y el buzzer debe emitir un sonido|Paola Patlán|1|

## Prototipo en 3D
- Imagen de prototipo realizado en tinkercad


## Circuito en Fritzing y PCB


## Imagen del proyecto físico 


## Aplicación web


## Dashboard en Grafana


## Carta de aceptación del proyecto firmada por la beneficiaria


## Vídeo de aceptación del proyecto


## Código fuente

Funcionamiento de los sensores: https://github.com/maramendoza692/ProjectVetSafeC3000/blob/main/SENSORES.py                  
Funcionamiento de la oled para visualizar pedidos: https://github.com/maramendoza692/ProjectVetSafeC3000/blob/main/PEDIDOS.py        
Flow del crud de la aplicación web: https://github.com/maramendoza692/ProjectVetSafeC3000/blob/main/CRUD%20%20Tacomandi.json      
Flow del broker mqtt: https://github.com/maramendoza692/ProjectVetSafeC3000/blob/main/SENSORES%20Tacomandi.json         









