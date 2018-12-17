import json


class HTTPObject:
    def __init__(self, request_text):
        self.request = str(request_text.decode('utf-8').strip("\\r\\n")).splitlines()  # Parses decoded socket response to a list

        self.status_code = ""  # 200 if ok, 400 if bad request
        # self.content_type = ""  # ie. JSON
        self.content_type = get_content_type(self.request)
        # self.json = ""  # JSON payload for POST methods
        self.json = get_json(self.request, self.content_type)
        # self.method = ""  # eg. POST, GET etc.
        self.method = get_method(self.request)
        # self.URI = ""  # eg /users/Andreas
        self.URI = get_URI(self.request)

        # self.response = ""

    def __str__(self):
        return f'''Request:\t\t{self.request}\nPath:\t\t\t{self.URI}\nHTTP method:\t{self.method}\nJSON payload:\t{self.json}'''

    def response(self):
        return f"{self.status_code}\nContent-Type: {self.content_type}\n\n{self.json}"


def get_content_type(request):
    content_type = ""
    for (e, i) in enumerate(request):
        if request[e][:12] == "Content-Type":
            content_type = request[e][14:]

    return content_type


# Returns dict of JSON objects, if payload content-type is json.
def get_json(request, content_type):
    if content_type == "application/json":
        for (e, i) in enumerate(request):
            if i == "":
                try:
                    return json.loads("".join(request[e:]))
                except:
                    return ""
    else:
        return "{}"


# Returns the request method as a str
def get_method(request):
    return get_request_line(request)[0]


# Returns the path as a list ie. /[users]/[id]
def get_URI(request):
    uri = get_request_line(request)[1].split("/")[1:]

    if uri[0].casefold() != "api".casefold():  # Checks if the request is on /api/ (caseless)
        print("Not an api call")
    else:
        if uri[-1] == "":  # Checks if last element is empty (happens when URI ends with "/")
            return uri[1:-1]
    return uri[1:]


# Returns the request line (includes method, path and version)
def get_request_line(request):
    return request[0].split(" ")


# @DeprecationWarning
# # Returns decoded socket response as a list
# def response_parsing(request):
#     return str(request.decode('utf-8').strip("\\r\\n")).splitlines()
