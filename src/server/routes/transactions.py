import bottle

app = bottle.Bottle()

# /transactions/<transaction_id>
@app.get("/<transaction_id>")
def transactions_get_by_id(transaction_id):
    return {
        "code": 200,
        "transaction_id": transaction_id,
        "message": "Bajo construccion",
        "detail": {
            "amount": 0,
            "from": "user 1",
            "to": "user 2",
            "date": "2021-02-17"
        }
    }
