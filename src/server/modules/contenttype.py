from functools import wraps
from bottle import request, response, abort

def content_type_json(_route_func):
    @wraps(_route_func)
    def _content_type_json(*args, **kwargs):
        if request.content_type != 'application/json':
            abort(415, "Only accepts: application/json")
        response.content_type = 'application/json'
        return _route_func(*args, **kwargs)
    return _content_type_json

