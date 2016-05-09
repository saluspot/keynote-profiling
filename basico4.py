#!/bin/env/python3

import pprint
import cProfile

from wsgiref.util import setup_testing_defaults

def my_wsgi_application(environ, start_response):
    setup_testing_defaults(environ)
    start_response('200 OK', [('Content-type', 'text/plain')])

    ret = pprint.pformat(environ)
    yield ret.encode("utf-8")  # python3 wsgi must return bytes

def my_profiling_middleware(environ, start_response):
    result = []
    profiler = cProfile.Profile()
    profiler.runcall(
        lambda: result.extend(my_wsgi_application(environ, start_response))
    )
    profiler.dump_stats('basico4.profile')
    return result

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('', 8899, my_profiling_middleware)
    server.serve_forever()
