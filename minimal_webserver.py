#!/usr/bin/python

import wsgiref.simple_server
import argparse


def simple_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=UTF-8')]
    response_body=[]
    start_response(status, headers)
    response_body.append(b'hello: ')
    response_body.append(environ['REQUEST_METHOD'].encode('utf-8'))
    return response_body

def main(opts):
    print("Serving on port",opts.port)
    httpd=wsgiref.simple_server.make_server(opts.host, opts.port, simple_app)
    httpd.serve_forever()

def parse_cli():
    parser = argparse.ArgumentParser(description="""A minimal wsgi server""",formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-p','--port', help="The port number the server listens on", type=int, default=8080)
    parser.add_argument('--host', help="The host to bind to the server listens on", type=str, default="0.0.0.0")
    opts = parser.parse_args()
    return opts


if __name__ == "__main__":
    opts=parse_cli()
    main(opts)
