import socket

def iniciar_servidor_tcp():
    porta = int(input("Digite a porta à ser escutada: "))
    host = '0.0.0.0'

    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor_socket.bind((host, porta))
    servidor_socket.listen(5)

    print(f"\n[SERVIDOR TCP] Escutando na porta {porta}...")
    print("Aguardando conexões... (Pressione Ctrl+C para encerrar)\n")

    try:
        while True:
            # Aceita uma nova conexão de cliente
            conexao, endereco_cliente = servidor_socket.accept()
            print(f"\n[+] Nova conexão estabelecida com {endereco_cliente}")

            # Loop interno para manter a comunicação com o cliente conectado
            while True:
                dados = conexao.recv(2048)
                if not dados:
                    # Se não houver dados, o cliente desconectou
                    print(f"[-] Cliente {endereco_cliente} desconectou.")
                    break

                mensagem_texto = dados.decode('utf-8')
                print(f"[{endereco_cliente[0]}]: {mensagem_texto}")

                # Envia confirmação
                resposta = f"TCP Server: Recebido '{mensagem_texto}'"
                conexao.send(resposta.encode('utf-8'))

            conexao.close()
    except KeyboardInterrupt:
        print("\nServidor finalizado.")
    finally:
        servidor_socket.close()

if __name__ == '__main__':
    iniciar_servidor_tcp()