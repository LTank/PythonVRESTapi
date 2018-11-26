class action:
    def __init__(self, request):
        self.request = request

        def post():
            print("Saving:", request.json)
        def get():
            print("Retrieving:", request.json)
        def put():
            print("Replacing JSON object with: ", request.json)
        def patch():
            print("Changing a value from object:", request.json)

        options = {
            "POST": post,
            "GET" : get,
            "PUT" : put,
            "PATCH" : patch,
        }

        options[request.method]()
