import bottle

app = bottle.Bottle()


@app.get("<transaction_id>")
def transactions_get_by_id(transactions_id):
    return {"code": 200, "message": "Bajo construccion"}
