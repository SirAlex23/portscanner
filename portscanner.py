import socket
import sys

def escanear_puertos(objetivo, puertos):
    try:
        # Intenta resolver el hostname a IP
        ip_objetivo = socket.gethostbyname(objetivo)
    except socket.gaierror:
        print("El hostname no pudo ser resuelto. Saliendo.")
        sys.exit()
        
    
if __name__ == "__main__":
    puertos_comunes = [21, 22, 23, 80, 443, 3389] # Rango de prueba
    ip_o_hostname = input("Ingrese la dirección IP o hostname a escanear: ")
    escanear_puertos(ip_o_hostname, puertos_comunes)
