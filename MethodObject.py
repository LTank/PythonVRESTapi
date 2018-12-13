import json

from db import *

tosend = ""
class action:
    def __init__(self, request):
        self.request = request
        con = database()

        def post():
            if (request.json == ""):
                return ""
            print("Saving:", request.json)

        def get():
            if request.path[0] == "messages":
                request.response = f"HTTP/1.1 200 OK\nContent-Type: application/json\n\n{json.dumps(getallmessages())}"

            if request.path[0] == "user":
                login = request.path[1].split("=")
                login[0] = login[0][:-2]  # removes ?p from username

                request.response = f"HTTP/1.1 200 OK\nContent-Type: application/json\n\n{json.dumps(getUser(login[0], login[1]))}"
            else:
                if getUser(login[0], login[1]):

                request.response = f"HTTP/1.1 400 Bad Request"

        def put():
            print("Replacing JSON object with: ", request.json)

        def patch():
            print("Changing a value from object:", request.json)

        options = {
            "POST": post,
            "GET": get,
            "PUT": put,
            "PATCH": patch,
        }

        options[request.method]()
