
class Browser:

    def make_http_request(self, url):
        print("Hi, Lets make the HTTP request without auth")

    def make_http_request(self, url, auth = None):
        print("Hi, Lets make the HTTP request with auth", url, auth )


obj = Browser()
obj.make_http_request("google.com")
obj.make_http_request("google.com", "admin")