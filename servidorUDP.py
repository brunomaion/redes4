import socket

udp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Ligação do socket ao endereço e porta
# IPv4='localhost' ou '127.0.0.1', IPv6='::1'
server_address = ('localhost', 12345)
udp_server_socket.bind(server_address)

print("Servidor UDP aguardando mensagens...")
# Recebe dados do cliente
while True:
# Buffer de 1024 bytes
  data, address = udp_server_socket.recvfrom(1024)

  print(f"Mensagem recebida: {data.decode()}
  # Enviar uma resposta opcional para o cliente de {address}")
  response ="Mensagem recebida com sucesso"
  udp_server_socket.sendto(response.encode(), address)
  print(f"Resposta enviada para {address}")