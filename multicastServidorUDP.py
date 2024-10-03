import socket
import struct
import time

# Criação do socket UDP
# IPv4: 224.0.0.0 a 239.255.255.255
multicast_group = '224.1.1.1'
server_address = ('', 12345)

# Configuração do socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Definindo TTL (Time to Live) para o pacote multicast
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# Enviando mensagens ao grupo multicast
try:
    while True:
        message = "Mensagem multicast UDP"
        print(f"Enviando: {message}")
        
        # Envia a mensagem ao grupo multicast
        sent = sock.sendto(message.encode(), (multicast_group, 12345))
        
        # Pausa antes de enviar a próxima mensagem
        time.sleep(2)
finally:
    # Fecha o socket
    sock.close()