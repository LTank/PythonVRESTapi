from socket import *
import _thread
import HTTPHandler

HOST, PORT = '', 5000

listen_socket = socket(AF_INET, SOCK_STREAM)
listen_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)


def main(client_connection, client_address):
    request = client_connection.recv(1024)
    HTTPHandler.response_parsing(request)

    HTTPHandler



while True:
    client_connection, client_address = listen_socket.accept()
    try:
        _thread.start_new_thread(main, (client_connection, client_address))
    except:
        print("Threading error!")
