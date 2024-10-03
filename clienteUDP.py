import socket

 # Criação do socket UDP
udp_client_socket = socket.socket(socket.AF_INET,
socket.SOCK_DGRAM)

# Endereço do servidor e porta
# No mesmo host, IPv4='localhost'ou '127.0.0.1', IPv6='::1'
dest_ip = 'localhost'# Altere para o IP de destino
dest_port = 12345 # Porta de destino

server_address = (dest_ip, dest_port)

# Mensagem a ser enviada ao servidor
message = "!"
udp_client_socket.sendto(message.encode(), server_address)
# Recebe resposta do servidor
data, server = udp_client_socket.recvfrom(1024)
print(f"Resposta do servidor: {data.decode()}")

# Fechando o socket do cliente
udp_client_socket.close()