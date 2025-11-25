*Descripción*
El script implementa una simulación controlada de ataque basada en el envío de paquetes TCP con el flag SYN (El flag SYN es la señal que usa TCP para iniciar una conexión)activado hacia un puerto específico de la máquina virtual.
El objetivo principal es generar tráfico reconocible para que el Blue Team pueda detectarlo mediante su sniffer de red y registrar la actividad como potencialmente sospechosa.

Esta técnica reproduce un comportamiento típico de reconocimiento, donde un atacante envía solicitudes SYN para descubrir puertos abiertos sin completar el handshake TCP.

*Bibliotecas utilizadas*
1. scapy.all:
	IP: Se utiliza para construir la capa IP del paquete, definiendo la dirección IP de destino (dst=target_ip).
	TCP: Se utiliza para construir la capa TCP, definiendo:
		Puerto de origen (sport)
		Puerto de destino (dport)
		Bandera de control (flags="S" para SYN)
	send: Envía el paquete construido a la red. Es la función que realmente “dispara” el ataque controlado.
	RandShort: Se usa para que cada paquete tenga un puerto de origen distinto, simulando comportamiento real de un 	sistema.

2. time: Se usa la función time.sleep(segundos) para introducir una pequeña pausa entre cada paquete SYN. Permitiendo observar claramente cada paquete en el sniffer y evita un envío masivo que parezca un ataque de denegación de servicio.

*Funcionamiento*
La función syn_probe se encarga de generar y enviar paquetes TCP con el flag SYN hacia la dirección IP y el puerto objetivo indicados por el usuario, simulando un intento de conexión. Esta función utiliza puertos de origen aleatorios para imitar el comportamiento natural de un sistema operativo y envía cada paquete con un pequeño retraso para evitar patrones agresivos o efectos similares a un ataque de denegación de servicio.

El bloque principal del script actúa como el punto de entrada del programa y solicita al usuario la IP objetivo, el puerto de destino y parámetros opcionales como la cantidad de paquetes SYN a enviar y el retraso entre ellos. Una vez recopilados los datos necesarios, este bloque ejecuta la función syn_probe con los valores proporcionados y permite que el script funcione de manera interactiva, facilitando su uso en diferentes escenarios ofensivos.

*Uso*
El usuario debe ejecutar packet_attack.py desde una terminal en su máquina local, ingresar la dirección IP pública de la máquina objetivo y el puerto permitido en su configuración de red, y proporcionar la cantidad de paquetes SYN que desea enviar junto con el tiempo de espera entre cada uno. Una vez ingresados los datos, el script enviará los paquetes SYN hacia el destino especificado, lo que permite generar tráfico controlado que puede observarse desde la máquina víctima mediante herramientas como tcpdump o un sniffer defensivo.