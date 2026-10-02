import socket

def iniciar_servidor_tcp():
    porta = int(input("Digite a porta à ser escutada: "))
    # Porta forçada a ser int, bind precisa obrigatoriamente de um inteiro na segunda posição da tupla
    host = '0.0.0.0'
    # '0.0.0.0' diz ao SO para aceitar conexões vindas de qualquer interface de rede da máquina
    
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # SO_REUSEADDR permite reutilizar a mesma porta imediatamente se o servidor cair
    servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor_socket.bind((host, porta))
    # O '5' é a fila de espera de conexões pendentes, nesse caso até 5 conexões podem ficar aguardando para serem aceitas
    servidor_socket.listen(5)

    print(f"\n[SERVIDOR TCP] Escutando na porta {porta}...")
    print("Aguardando conexões... (Pressione Ctrl+C para encerrar)\n")

    try:
        # Loop principal infinito para garantir que o servidor continue ativo após a desconexão do cliente
        while True:
            # accept() bloqueia a execução até alguém conectar, e então a conexao retorna um socket dedicado apenas a este dialogo cliente-servidor
            conexao, endereco_cliente = servidor_socket.accept()
            print(f"\n[+] Nova conexão estabelecida com {endereco_cliente}")

            # Loop interno para manter a comunicação com o cliente conectado
            while True:
                dados = conexao.recv(2048)
                if not dados:
                    # Se não houver dados, o cliente desconectou
                    print(f"[-] Cliente {endereco_cliente} desconectou.")
                    break

                # Decodifica os dados recebidos de bytes para string usando UTF-8
                mensagem_texto = dados.decode('utf-8')
                print(f"[{endereco_cliente[0]}]: {mensagem_texto}")

                # Envia confirmação codificada de volta para o cliente
                resposta = f"TCP Server: Recebido '{mensagem_texto}'"
                conexao.send(resposta.encode('utf-8'))

            conexao.close()
    # Permite que o servidor seja encerrado com Ctrl+C, capturando a exceção KeyboardInterrupt
    except KeyboardInterrupt:
        print("\nServidor finalizado.")
    finally:
        servidor_socket.close()
    # O bloco finally garante que o socket do servidor seja fechado corretamente, mesmo se ocorrer uma interrupção inesperada

# Bloco condicional que garante que 'iniciar_servidor_tcp()' só rode se este arquivo for executado diretamente
if __name__ == '__main__':
    iniciar_servidor_tcp()