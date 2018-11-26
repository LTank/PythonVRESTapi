from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, socket
import _thread
import HTTPHandler
import MethodObject

HOST, PORT = '', 5000

listen_socket = socket(AF_INET, SOCK_STREAM)
listen_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)


def main(client_connection, client_address):
    # Making a python obj from a socket obj.
    request = HTTPHandler.HTTPRequest(client_connection.recv(1024))
    # Acting on the HTTP method type
    MethodObject.action(request)


    # for (i,e) in enumerate(request.request):
    #     print(i, e)

    print(request)

while True:
    client_connection, client_address = listen_socket.accept()
    try:
        _thread.start_new_thread(main, (client_connection, client_address))
    except:
        print("Threading error!")
