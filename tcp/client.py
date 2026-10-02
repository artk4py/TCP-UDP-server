import socket

def iniciar_cliente_tcp():
    # Solicita as configurações ao usuário no terminal
    ip_servidor = input("Digite o IP do servidor: ").strip()
    porta = int(input("Digite a porta à ser conectada: ").strip())
    # Porta forçada a ser int, connect precisa obrigatoriamente de um inteiro na segunda posição da tupla


    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # O socket TCP é criado com AF_INET (IPv4) e SOCK_STREAM (TCP)

    try:
        print(f"Tentando conectar a {ip_servidor}:{porta}...")
        cliente_socket.connect((ip_servidor, porta))
        print(f"\n[CLIENTE TCP] Conectado com sucesso!")
        print("Digite suas mensagens. Digite '/sair' para encerrar.\n")

        while True:
            mensagem = input("Você > ")

            if mensagem.lower().strip() == '/sair':
                print("Encerrando conexão...")
                break

            if not mensagem.strip():
                continue

            # Envia a mensagem pelo canal TCP ativo
            cliente_socket.send(mensagem.encode('utf-8'))

            # Aguarda a resposta do servidor
            resposta = cliente_socket.recv(2048)
            print(f"Servidor > {resposta.decode('utf-8')}\n")

    except ConnectionRefusedError:
        print(f"\nErro: Não foi possível conectar a {ip_servidor}:{porta}. Verifique se o servidor está rodando.")
    except Exception as e:
        print(f"\nOcorreu um erro: {e}")
    finally:
        cliente_socket.close()

if __name__ == '__main__':
    iniciar_cliente_tcp()