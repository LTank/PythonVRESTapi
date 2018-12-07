from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, socket
import _thread
import HTTPHandler
import MethodObject

HOST, PORT = '', 9000

# Setting up socket
listen_socket = socket(AF_INET, SOCK_STREAM)  # IPv4 and TCP
listen_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # SOL_SOCKET is the level of address reuse option (1=yes/true).
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
    # print(request.response)


    client_connection.sendall(request.response.encode())




while True:
    client_connection, client_address = listen_socket.accept()
    try:
        _thread.start_new_thread(main, (client_connection, client_address))
    except:
        print("Threading error!")
