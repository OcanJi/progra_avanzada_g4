*Descripción*
El script implementa una simulación controlada de ataque de fuerza bruta sobre el servicio SSH de una máquina objetivo autorizada dentro del laboratorio. Su propósito es generar intentos de autenticación visibles para el Blue Team de manera que puedan detectar estos accesos fallidos mediante herramientas de monitoreo y revisar los registros del sistema. El programa prueba una lista fija de contraseñas y registra cada intento, pero sin almacenar las contraseñas en texto claro, respetando buenas prácticas de seguridad.

*Bibliotecas utilizadas*
1. paramiko: Paramiko permite simular el comportamiento de un atacante intentando múltiples credenciales sin necesidad de herramientas externas
Se utiliza para:
	Crear un cliente SSH (SSHClient())
	Configurar la política de claves (AutoAddPolicy()) para aceptar claves del servidor
	Intentar autenticarse mediante connect(), que devuelve éxito o lanza excepciones en caso de error


2. logging: Permite registrar los intentos de autenticación en un archivo (ssh_brute_log.txt).

3. time: Se usa time.sleep() para introducir pequeños retrasos entre intentos y simular un ataque moderado, evitando inundar el servidor con solicitudes continuas.

4. sys: Se utiliza únicamente para detener el programa de manera controlada si Paramiko no está instalado.

*Funcionamiento*
El script inicia configurando un archivo de log y una lista de contraseñas que serán utilizadas para intentar autenticación. La función principal try_password() es responsable de establecer una conexión SSH mediante Paramiko e interpretar la respuesta del servidor. Si la contraseña es incorrecta, se detecta mediante la excepción AuthenticationException; si la conexión es correcta, el método devuelve True indicando que la credencial fue válida.

La función interactive_main() solicita los parámetros del ataque: IP objetivo, puerto y usuario. Luego ejecuta cada intento de autenticación uno por uno, registrando la actividad y deteniéndose si alguna contraseña resulta válida. Este comportamiento simula fielmente la técnica clásica de fuerza bruta, manteniéndose dentro de los límites éticos del entorno académico.

*Uso*
El usuario ejecuta el script desde su máquina local dentro del ambiente permitido. Al iniciarlo, el programa solicitará la IP de la máquina objetivo, el puerto SSH (generalmente 22) y el usuario que se desea probar. A continuación, se recorrerá la lista interna de contraseñas, realizando un intento de autenticación por cada una. El archivo ssh_brute_log.txt contendrá un registro completo de toda la actividad.