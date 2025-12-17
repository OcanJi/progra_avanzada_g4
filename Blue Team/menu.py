#!/usr/bin/env python3
import os

def mostrar_menu():
    print("\nMenu principal - Blue Team\n")
    print("1 - Deteccion de trafico sospechoso (IDS)")
    print("2 - Auditoria del sistema operativo")
    print("3 - Aplicar hardening de firewall")
    print("4 - Sistema de alertas")
    print("0 - Salir\n")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            os.system("sudo python3 sniffer_defense.py")

        elif opcion == "2":
            os.system("sudo python3 os_audit.py")

        elif opcion == "3":
            os.system("sudo ./firewall_hardening.sh")

        elif opcion == "4":
            os.system("python3 alert_logger.py")

        elif opcion == "0":
            break

        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()
