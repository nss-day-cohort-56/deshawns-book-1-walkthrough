import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from views import (get_all_walkers,
                   get_single_walker,
                   get_all_dogs,
                   get_single_dog,
                   delete_walker,
                   create_walker,
                   update_walker,
                   create_dog,
                   delete_dog,
                   update_dog,
                   get_walkers_by_city,
                   )


class HandleRequests(BaseHTTPRequestHandler):

    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def parse_url(self, path):
        """Parse the url into the resource, id, or query params"""
        parsed_url = urlparse(self.path)
        path_params = parsed_url.path.split('/')
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

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

        parsed = self.parse_url(self.path)

        # If the path does not include a query parameter, continue with the original if block
        if '?' not in self.path:
            (resource, id) = parsed

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
        else:
            (resource, query) = parsed
            if resource == 'walkers' and query.get('city'):
                response = get_walkers_by_city(query['city'])
            if resource == 'dogs' and query.get('walker'):
                response = get_dogs_by_walker(query['walker'])

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
            new_data = create_dog(post_body)

        self.wfile.write(f"{new_data}".encode())

    def do_DELETE(self):
        """Handles delete requests to the server
        """
        self._set_headers(204)

        (resource, id) = self.parse_url(self.path)

        if resource == 'walkers':
            delete_walker(id)
        if resource == 'dogs':
            delete_dog(id)

        self.wfile.write("".encode())

    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        if resource == "walkers":
            update_walker(id, post_body)
        if resource == "dogs":
            update_dog(id, post_body)

        self.wfile.write("".encode())


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
