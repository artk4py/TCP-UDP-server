import socket

def iniciar_servidor_udp():
    porta = int(input("Digite a porta à ser escutada: "))
    host = '0.0.0.0' 

    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor_socket.bind((host, porta))

    print(f"\n[SERVIDOR UDP] Rodando na porta {porta}...")
    print("Aguardando mensagens...\n")

    try:
        while True:
            # Recebe a mensagem e o endereço do cliente
            mensagem, endereco_cliente = servidor_socket.recvfrom(2048)
            mensagem_texto = mensagem.decode('utf-8')
            print(f"[{endereco_cliente[0]}:{endereco_cliente[1]}]: {mensagem_texto}")
            
            # Responde ao cliente
            resposta = f"UDP Server: Recebido '{mensagem_texto}'"
            servidor_socket.sendto(resposta.encode('utf-8'), endereco_cliente)
    except KeyboardInterrupt:
        print("\nServidor finalizado.")
    finally:
        servidor_socket.close()

if __name__ == '__main__':
    iniciar_servidor_udp()