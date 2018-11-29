class action:
    def __init__(self, request):
        self.request = request


        def post():
            # TODO
            print("Saving:", request.json)
        def get():
            # TODO
            # Lookup in db
            path = request.path[0]

            print("Retrieving:", request.json)
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
