import nmap

def scan(target):
    nm = nmap.PortScanner()
    print(f"Escaneando {target}...")

    nm.scan(target, arguments="-sS -sV -Pn")

    # Guardar salida en archivo
    with open("resultado_scan.txt", "w") as f:
        f.write(nm.csv())

    # Mostrar resultados simples
    for host in nm.all_hosts():
        print(f"\nHost: {host} ({nm[host].hostname()})")
        for proto in nm[host].all_protocols():
            puertos = nm[host][proto].keys()
            for puerto in puertos:
                estado = nm[host][proto][puerto]["state"]
                print(f"Puerto {puerto}/{proto}: {estado}")

if __name__ == "__main__":
    objetivo = input("IP o dominio objetivo: ")
    scan(objetivo)
