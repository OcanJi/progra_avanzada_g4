#!/usr/bin/env python3
import logging
import datetime
import subprocess

archivo_log = "security_events.log"
logging.basicConfig(filename=archivo_log, level=logging.INFO)
open(archivo_log, "a").close()

def registrar_evento(mensaje):
    texto = f"[{datetime.datetime.now()}] {mensaje}"
    logging.info(texto)
    print(texto)

def bloquear_ip(ip):
    registrar_evento(f"Bloqueo solicitado para la IP {ip}")
    subprocess.run(
        f"ufw deny from {ip}",
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

if __name__ == "__main__":
    print("Sistema de alertas cargado")
