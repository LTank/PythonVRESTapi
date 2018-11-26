# print(request.error_code)  # None  (check this first)
# print(request.command)  # "GET"
# print(request.path)  # "/who/ken/trust.html"
# print(request.request_version)  # "HTTP/1.1"
# print(len(request.headers))  # 3
# print(request.headers.keys())  # ['accept-charset', 'host', 'accept']
# print(request.headers['host'])  # "cm.bell-labs.com"

#
# class HTTPRequest():
#     def __init__(self, request_text):
#         self.rfile = StringIO(request_text)
#         self.raw_requestline = self.rfile.readline()
#         self.error_code = self.error_message = None
#         self.parse_request()
#

def response_parsing(request):
    request_list = str(request.decode('utf-8').strip("\\r\\n")).splitlines()

    # Takes the first index of request_list and splits it up to get the GET/POST/PUT response and the location
    # in separate values.
    GPP_and_location = request_list[0].split(' ')
    GPP_response = GPP_and_location[0]
    location = GPP_and_location[1]

    # Gets the json object from the request_List
    json_object = request_list[7]


