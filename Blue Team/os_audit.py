#!/usr/bin/env python3
import subprocess
import datetime

archivo_reporte = "os_audit_report.txt"

def ejecutar(comando):
    try:
        return subprocess.check_output(comando, shell=True, text=True)
    except:
        return "No disponible\n"

def main():
    ahora = datetime.datetime.now()

    with open(archivo_reporte, "a") as f:
        f.write("\nAuditoria del sistema\n")
        f.write(f"Fecha: {ahora}\n\n")

        f.write("Sistema\n")
        f.write(ejecutar("uname -a") + "\n")

        f.write("Usuarios\n")
        f.write(ejecutar("cut -d: -f1 /etc/passwd") + "\n")

        f.write("Grupos\n")
        f.write(ejecutar("cut -d: -f1 /etc/group") + "\n")

        f.write("Ultimos accesos\n")
        f.write(ejecutar("last -n 5") + "\n")

        f.write("Puertos abiertos\n")
        f.write(ejecutar("ss -tuln") + "\n")

        f.write("Servicios activos\n")
        f.write(ejecutar(
            "systemctl list-units --type=service --state=running | head -n 20"
        ) + "\n")

        f.write("Configuracion SSH\n")
        f.write(ejecutar(
            "grep -E 'Port|PermitRootLogin|PasswordAuthentication' /etc/ssh/sshd_config"
        ) + "\n")

        f.write("Cron del sistema\n")
        f.write(ejecutar("cat /etc/crontab") + "\n")

    print("Auditoria finalizada")

if __name__ == "__main__":
    main()
