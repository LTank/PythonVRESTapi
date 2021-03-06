import json

from db import *


class Action:
    def __init__(self, request):
        self.request = request
        con = database()

        def post():
            if request.json == "":  # Might be redundant.
                return ""
            else:
                if type(request.json) is not dict:
                    request.json = json.loads(request.json)

            if request.URI[0] == "messages":
                try:
                    createmessage(request.json)
                    request.status_code = "HTTP/1.1 200 OK"

                except Exception as e:
                    print("Failed to create message")
                    print(e)
                    request.status_code = "HTTP/1.1 400 Bad Request"

            elif request.URI[0] == "user":
                try:
                    createuser(request.json)
                    request.status_code = "HTTP/1.1 200 OK"

                except Exception as e:
                    print("Failed to create user")
                    print(e)
                    request.status_code = "HTTP/1.1 400 Bad Request"

            else:
                request.status_code = "HTTP/1.1 400 Bad Request"

        def get():
            if request.URI[0] == "messages":
                request.json = json.dumps(getallmessages())
                request.status_code = "HTTP/1.1 200 OK"

            elif request.URI[0] == "user":
                login = request.URI[1].split("=")
                login[0] = login[0][:-2]  # removes ?p from username
                request.json = json.dumps(getUser(login[0], login[1]))
                request.status_code = "HTTP/1.1 200 OK"

            else:
                request.status_code = "HTTP/1.1 400 Bad Request"

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
