from itertools import chain
import logging
import json

import bottle
from swagger_ui import api_doc

from server.http_reponse_codes import HTTP_REPONSE_CODES
from server.modules.cors import enable_cors

import server.routes.health
import server.routes.auth

logging.basicConfig(
    filename='server.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)


class BottleGlass(bottle.Bottle):
    """Bottle Glass
    Esta clase hereda de `bottle.Bottle` para redefinir
    el metodo `route_mounte`.

    Para el resto de los metodos de esta clase, dirigirse a
    la documentacion de `bottle.Bottle`.

    Pagina oficial de Bottle.py: https://bottlepy.org/
    """
    def route_mount(self, prefix, _app=None, routes=[]):
        if _app and isinstance(_app, bottle.Bottle):
            routes.extend(_app.routes)
        for route in routes:
            route.rule = prefix + route.rule
            route.app = self
            self.add_route(route)


app = BottleGlass()
api_doc(
    app,
    config_path="../docs/swagger.yaml",
    url_prefix="/swagger",
    title="Swagger Doc"
)
app.route_mount('/health', server.routes.health.app)
app.route_mount('/auth', server.routes.auth.app)

@app.get("/")
def index():
    return dict(code=200)


def error_handler(code=500, message="Internal Error"):
    @enable_cors
    def error_error_code(error):
        bottle.response.status = code
        bottle.response.content_type = 'application/json'
        try:
            reason = str(error.body)
        except:
            reason = "Unknown"
        returnable = dict(
            code=code, message=message, reason=reason
        )
        return json.dumps(returnable)
    return error_error_code


for error_code in filter(lambda e: int(e)>=400, HTTP_REPONSE_CODES.keys()):
    app.error(code=error_code)(error_handler(
        code=int(error_code),
        message=HTTP_REPONSE_CODES[error_code]
    ))

