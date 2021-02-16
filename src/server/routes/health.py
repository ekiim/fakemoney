import bottle

app = bottle.Bottle()


@app.get("/alive")
def index():
    print("Alive Route")
    return {"code": 200}


def get_test_text(usuario, fecha, cantidad):
    return "Mensaje de prueba %s - %s - %s" % (usuario, fecha, cantidad)


@app.get("/test")
def test():
    test_value = get_test_text(1, 2, 3)
    return {"code": 200, "test": test_value}
