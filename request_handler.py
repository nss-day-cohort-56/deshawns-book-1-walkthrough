import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import (get_all_walkers,
                   get_single_walker,
                   get_all_dogs,
                   get_single_dog,
                   delete_walker,
                   create_walker,
                )


class HandleRequests(BaseHTTPRequestHandler):

    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def parse_url(self, path):

        path_params = path.split("/")
        resource = path_params[1]
        id = None

        try:
            id = int(path_params[2])
        except IndexError:
            pass
        except ValueError:
            pass

        return (resource, id)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Handles GET requests to the server
        """
        self._set_headers(200)

        (resource, id) = self.parse_url(self.path)

        if resource == "walkers":
            if id is not None:
                response = f"{get_single_walker(id)}"

            else:
                response = f"{get_all_walkers()}"
        elif resource == "dogs":
            if id is not None:
                response = f"{get_single_dog(id)}"

            else:
                response = f"{get_all_dogs()}"

        else:
            response = []

        self.wfile.write(f"{response}".encode())

    def do_POST(self):
        """Handles POST requests to the server
        """
        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        post_body = json.loads(post_body)

        (resource, _) = self.parse_url(self.path)

        new_data = None

        if resource == "walkers":
            new_data = create_walker(post_body)
        if resource == "dogs":
            # TODO: Finish the code to add a dog
            pass

        self.wfile.write(f"{new_data}".encode())

    def do_DELETE(self):
        """Handles delete requests to the server
        """
        self._set_headers(204)

        (resource, id) = self.parse_url(self.path)

        if resource == 'walkers':
            delete_walker(id)
        if resource == 'dogs':
            # TODO: Finish the code to delete a dog
            pass

        self.wfile.write("".encode())


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
