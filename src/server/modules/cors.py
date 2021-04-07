from urllib.parse import urlparse
from functools import wraps
from os import environ
from bottle import response, request, HTTPResponse

def enable_cors(_route_function):
    @wraps(_route_function)
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        http_origin = urlparse(request.headers.get("ORIGIN"))
        allowed_headers = [
            "Access-Control-Allow-Origin",
            "Authorization",
            "Content-Type"
        ]
        allowed_methods = "GET, POST, OPTIONS"
        if http_origin.netloc in [
            request.get_header('host'),
            environ.get("DEPLOY_DOMAIN", None),
            environ.get("DEPLOY_API_DOMAIN", None)
        ]:
            response.headers["Access-Control-Allow-Origin"] = http_origin.geturl()
            response.headers["Access-Control-Allow-Headers"] = ", ".join(
                allowed_headers + [h.lower() for h in allowed_headers]
            )
            response.headers["Access-Control-Allow-Credentials"] = "true"
            response.headers["Access-Control-Allow-Methods"] = allowed_methods
        if request.method == "OPTIONS":
            response.status = 200
            return {}
        return _route_function(*args, **kwargs)
    return _enable_cors
