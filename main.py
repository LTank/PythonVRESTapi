from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, socket
import _thread
from HTTPHandler import HTTPObject
import MethodObject

HOST, PORT = '', 9000

# Setting up socket
listen_socket = socket(AF_INET, SOCK_STREAM)  # IPv4 and TCP
listen_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # SOL_SOCKET is the level of address reuse option (1=yes/true).
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)


def main(client_connection, client_address):

    # Making a python obj from a socket obj.
    http_object = HTTPObject(client_connection.recv(1024))

    # Acting on the HTTP method type
    MethodObject.Action(http_object)

    # Prints values of http_object
    print("------------------------")
    for i in http_object.__dict__:
        print(i + ":", http_object.__dict__.get(i))

    # Sends a response and closes the connection.
    client_connection.sendall(http_object.response().encode())
    client_connection.close()


while True:
    client_connection, client_address = listen_socket.accept()
    try:
        _thread.start_new_thread(main, (client_connection, client_address))
    except:  # TODO Be more specific
        print("Threading error!")
