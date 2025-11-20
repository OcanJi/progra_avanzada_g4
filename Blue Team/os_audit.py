#!/usr/bin/env python3
import subprocess
import datetime

report_file = "os_audit_report.txt"

def run_cmd(cmd):
    try:
        result = subprocess.check_output(cmd, shell=True, text=True)
        return result.strip()
    except Exception as e:
        return f"Error ejecutando {cmd}: {e}"

def main():
    now = datetime.datetime.now()
    with open(report_file, "a") as f:
        f.write("\n============================\n")
        f.write(f" AUDITORÍA DEL SISTEMA - {now}\n")
        f.write("============================\n\n")

        f.write("== Información del sistema ==\n")
        f.write(run_cmd("systeminfo") + "\n\n" if subprocess.run("systeminfo", shell=True).returncode == 0 
                else run_cmd("uname -a") + "\n\n")

        f.write("== Procesos corriendo ==\n")
        f.write(run_cmd("tasklist") + "\n\n" if subprocess.run("tasklist", shell=True).returncode == 0
                else run_cmd("ps aux") + "\n\n")

        f.write("== Puertos abiertos ==\n")
        f.write(run_cmd("netstat -ano") + "\n\n")

    print(f"[✔] Auditoría completada. Guardada en {report_file}")

if __name__ == "__main__":
    main()
