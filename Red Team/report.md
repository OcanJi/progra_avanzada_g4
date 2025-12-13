# Red Team – Documentación de Ataques

Este documento describe las herramientas ofensivas desarrolladas por el Red Team para evaluar la exposición y capacidad de detección de una máquina virtual.
Los ataques se ejecutan desde una máquina local y están diseñados exclusivamente para un entorno de laboratorio controlado.

Las herramientas desarrolladas siguen una secuencia lógica de ataque:
1. Reconocimiento de puertos.
2. Generación de tráfico TCP sospechoso.
3. Ataque dirigido a un servicio específico (SSH).

---

## 1. scanner.py – Reconocimiento de Puertos

### Objetivo
Identificar los puertos y servicios expuestos en la máquina virtual para determinar posibles vectores de ataque.

### Funcionamiento
- El script solicita la IP objetivo.
- Ejecuta un escaneo TCP SYN utilizando Nmap (`-sS -sV -Pn`).
- Detecta puertos abiertos y servicios asociados.
- Guarda los resultados en un archivo `resultado_scan.txt`.

### Evidencia Generada
- Tráfico SYN observable desde la VM.
- Puertos abiertos visibles en herramientas defensivas.
- Archivo de salida que sirve como insumo para ataques posteriores.


---

## 2. packet_attack.py – Generación de Tráfico TCP (SYN)

### Objetivo
Simular tráfico de red sospechoso enviando múltiples paquetes TCP con el flag SYN activado, imitando técnicas de reconocimiento previas al ataque.

### Funcionamiento
- El usuario ingresa:
  - IP objetivo
  - Puerto destino
  - Cantidad de paquetes SYN
  - Retraso entre envíos
- El script construye manualmente cada paquete usando Scapy:
  - IP(dst=objetivo)
  - TCP(dport=puerto, flags="S")
- Los paquetes son enviados sin completar el handshake TCP.

### Evidencia Generada
- La VM recibe los paquetes SYN y responde con SYN-ACK si el puerto está abierto.
- El tráfico puede observarse mediante sniffers o logs defensivos.
- Se genera información clara sobre IP origen, puerto destino y frecuencia de paquetes.

---

## 3. ssh_brute.py – Ataque de Diccionario SSH

### Objetivo
Evaluar la robustez del servicio SSH expuesto mediante múltiples intentos de autenticación
utilizando una lista controlada de contraseñas.

### Funcionamiento
- El script se ejecuta desde la máquina local.
- Solicita:
  - IP de la VM
  - Puerto SSH
  - Usuario objetivo
- Utiliza Paramiko para intentar autenticaciones SSH de forma secuencial.
- Aplica un retraso entre intentos para hacer el ataque observable.
- Registra cada intento en el archivo `ssh_brute_log.txt`.

### Evidencia Generada
- En la VM:
  - Registros de intentos fallidos en `/var/log/auth.log` (Linux)
- En la máquina atacante:
  - Log local con historial de intentos y resultados

---

## 4. Correlación de Ataques

Los tres scripts generan eventos complementarios que pueden correlacionarse desde el punto
de vista defensivo:

| Script            | Tipo de evento generado                 |
|-------------------|------------------------------------------|
| scanner.py        | Escaneo de múltiples puertos TCP         |
| packet_attack.py  | Tráfico SYN repetitivo hacia un puerto   |
| ssh_brute.py      | Intentos fallidos de autenticación SSH   |

---

## 5. Conclusiones

- La combinación de reconocimiento, tráfico SYN y ataques a servicios expuestos
  representa un escenario realista de amenaza.
- Todos los ataques son observables y registrables desde la VM objetivo.
- La correcta configuración de logs, firewall y monitoreo es clave para la detección temprana.
- El ejercicio demuestra la importancia de correlacionar eventos de red y de sistema.

---

