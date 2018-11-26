import json


class HTTPRequest:
    def __init__(self, request_text):
        request_text = response_parsing(request_text)
        self.request = request_text
        self.path = get_path(request_text)
        self.method = get_method(request_text)
        self.json = jsonhandler(request_text)

        # Implement an error functionality
        # self.error_code = self.error_message = None

    def __str__(self):
        return f'''Request:\t\t"{self.request}\nPath:\t\t\t"{self.path}\nHTTP method:\t"{self.method}\nJSON payload:\t\"{self.json}'''


# Returns dict of JSON objects, if payload content-type is json.
def jsonhandler(request):
    if any("Content-Type: application/json" in s for s in request):
        for (e, i) in enumerate(request):
            if i == "":
                return json.loads("".join(request[e:]))

# Returns decoded socket response as a list
def response_parsing(request):
    return str(request.decode('utf-8').strip("\\r\\n")).splitlines()

# Returns the path as a list ie. /[users]/[id]
def get_path(request):
    path = get_request_line(request)[1].split("/")
    if path[1].casefold() != "api".casefold(): # Checks if the request is on /api/ (caseless)
        print("Not an api call")
    else:
        return path[2:]

# Returns the request method as a str
def get_method(request):
    return get_request_line(request)[0]

# Returns the request line (includes method, path and version)
def get_request_line(request):
    return request[0].split(" ")