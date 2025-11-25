#!/usr/bin/env python3
from scapy.all import IP, TCP, send, RandShort
import time

def syn_probe(target_ip, target_port, count=5, delay=1.0):
    print(f"[INFO] Enviando {count} paquetes SYN a {target_ip}:{target_port}")

    for i in range(1, count + 1):
        sport = RandShort()  # Puerto de origen aleatorio (simula puertos efímeros)

        # Paquete SYN: primera fase del handshake TCP
        pkt = IP(dst=target_ip) / TCP(sport=sport, dport=target_port, flags="S")

        send(pkt, verbose=False)
        print(f"SYN #{i} enviado (sport={sport})")

        time.sleep(delay)  #Permite observar cada paquete

    print("Prueba terminada. Revisar sniffer/logs por parte del Blue Team.\n")


if __name__ == "__main__":
    print("Red Team-packet_attack\n")

    target_ip = input("IP objetivo: ").strip()
    target_port = int(input("Puerto destino: ").strip())

    count_in = input("Cantidad de SYN (Recomendado 5): ").strip()
    delay_in = input("Delay entre paquetes (Recomendado 1.0): ").strip()

    count = int(count_in) if count_in else 5
    delay = float(delay_in) if delay_in else 1.0

    syn_probe(target_ip, target_port, count, delay)
    