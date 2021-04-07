import bottle

from server.modules.contenttype import content_type_json
from server.modules.cors import enable_cors


import fakemoney.models as models
from fakemoney.exceptions import FakeMoneyException
from fakemoney.utils import jwt_decode

app = bottle.Bottle()

@app.route("/signup", method=["POST", "OPTIONS"])
@enable_cors
@content_type_json
def signup():
    try:
        data = bottle.request.json
        user = models.User.signup(data)
    except FakeMoneyException as e:
        bottle.abort(406, e.message)
    except:
        bottle.abort(500)
    bottle.response.status = 201
    return {"code": 201, "message": "User Creation Successful"}


@app.route("/login", method=["POST", "OPTIONS"])
@enable_cors
@content_type_json
def login_email():
    try:
        data = bottle.request.json
        user = models.User.login(data)
        if not user:
            raise Exception()
    except FakeMoneyException as e:
        bottle.abort(406, e.message)
    except:
        bottle.abort(500)
    token = user.generate_token()
    bottle.response.status = 200
    return {"code": 200, "token": token}

@app.route("/validate", method=["GET", "OPTIONS"])
@enable_cors
@content_type_json
def validate_token():
    try:
        token = bottle.request.headers["Authorization"].split(" ")[1]
        decoded = jwt_decode(token)
        if not decoded:
            raise FakeMoneyException()
    except FakeMoneyException as e:
        bottle.abort(406, e.message)
    except:
        bottle.abort(500)
    bottle.response.status = 200
    return {"code": 200, "token": token}
