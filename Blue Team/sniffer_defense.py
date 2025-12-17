#!/usr/bin/env python3
from scapy.all import sniff
from scapy.layers.inet import IP, TCP
import datetime
import logging
import alert_logger

archivo_log = "traffic_alerts.log"
logging.basicConfig(filename=archivo_log, level=logging.INFO)
open(archivo_log, "a").close()

contador_syn = {}
contador_ack = {}

def es_ip_local(ip):
    return ip.startswith("10.") or ip.startswith("192.168.") or ip.startswith("172.")

def analizar_paquete(paquete):
    if not paquete.haslayer(IP) or not paquete.haslayer(TCP):
        return

    ip_origen = paquete[IP].src
    puerto = paquete[TCP].dport
    flags = paquete[TCP].flags
    ahora = datetime.datetime.now()

    if es_ip_local(ip_origen):
        return

    logging.info(f"[{ahora}] TCP desde {ip_origen} al puerto {puerto} flags={flags}")

    if flags == "S" or flags == 0x02:
        contador_syn[ip_origen] = contador_syn.get(ip_origen, 0) + 1
        if contador_syn[ip_origen] > 5:
            alert_logger.registrar_evento(
                f"Posible escaneo SYN desde {ip_origen}"
            )
            alert_logger.bloquear_ip(ip_origen)

    if flags == "A" or flags == 0x10:
        contador_ack[ip_origen] = contador_ack.get(ip_origen, 0) + 1
        if contador_ack[ip_origen] > 5:
            alert_logger.registrar_evento(
                f"Posible escaneo ACK desde {ip_origen}"
            )
            alert_logger.bloquear_ip(ip_origen)

print("IDS activo, monitoreando trafico de red")
sniff(filter="tcp", prn=analizar_paquete, store=0)
