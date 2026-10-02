import socket

def iniciar_cliente_udp():
    # Solicita as configurações ao usuário no terminal
    ip_servidor = input("Digite o IP do servidor: ").strip()
    porta = int(input("Digite a porta utilizada: ").strip())

    # O socket UDP é criado com AF_INET (IPv4) e SOCK_DGRAM (UDP)
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"\n[CLIENTE UDP] Conectado ao destino {ip_servidor}:{porta}")
    print("Digite suas mensagens. Digite '/sair' para encerrar.\n")

    try:
        while True:
            mensagem = input("Você > ")
            
            # Condição de saída do loop
            if mensagem.lower().strip() == '/sair':
                print("Encerrando cliente...")
                break

            if not mensagem.strip():
                continue

            # Envia a mensagem para o servidor
            cliente_socket.sendto(mensagem.encode('utf-8'), (ip_servidor, porta))

            # Define um tempo limite para aguardar a resposta do servidor de 3 segundos
            cliente_socket.settimeout(3.0)
            try:
                resposta, _ = cliente_socket.recvfrom(2048)
                print(f"Servidor > {resposta.decode('utf-8')}\n")
            except socket.timeout:
                print("Servidor > [Erro: Sem resposta do servidor / Timeout]\n")

    finally:
        cliente_socket.close()

if __name__ == '__main__':
    iniciar_cliente_udp()