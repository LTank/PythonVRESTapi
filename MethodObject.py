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
            model = request.path[0]
            try:
                usr = request.path[1].split("=")[1]
            except:
                usr = ""

            response = f"HTTP/1.1 200 OK\n\n{json.dumps(getallmessages())}"

            request.response = response

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
