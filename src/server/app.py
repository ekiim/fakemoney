import logging
import json

import bottle

import server.routes.health
import server.routes.transactions

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
app.route_mount('/transactions', server.routes.transactions.app)


@app.get("/")
def index():
    return dict(code=200)


def error_handler(error_code):
    def error_error_code(*args, **kwargs):
        bottle.response.status = error_code
        bottle.response.content_type = 'application/json'
        return json.dumps({"code": error_code})
    return error_error_code


for error_code in [400, 401, 402, 403, 404, 500]:
    app.error(code=error_code)(error_handler(error_code))


app.route_mount('/health', server.routes.health.app)
app.route_mount('/transactions', server.routes.transactions.app)
