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
    request_raw = HTTPHandler.response_parsing(request)

    # Takes the first index of request_list and splits it up to get the GET/POST/PUT response and the location
    # in separate values.
    GPP_and_location = request_raw[0].split(' ')
    GPP_response = GPP_and_location[0]
    location = GPP_and_location[1]

    # Gets the json object from the request_List
    json_object = request_raw[7]


while True:
    client_connection, client_address = listen_socket.accept()
    try:
        _thread.start_new_thread(main, (client_connection, client_address))
    except:
        print("Threading error!")
