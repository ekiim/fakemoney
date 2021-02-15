import bottle

app = bottle.Bottle()

@app.get("/alive")
def index():
    return {"code": 200}
