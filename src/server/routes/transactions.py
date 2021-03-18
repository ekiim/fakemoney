import bottle

app = bottle.Bottle()


@app.get("/id/<transaction_id>")
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

@app.get("/list")
def transactions_get_list():
    return {
        "code": 200,
        "transactions": [
            {
                "transaction_id": 11,
                "message": "Bajo construccion",
                "detail": {
                    "amount": 0,
                    "from": "user 1",
                    "to": "user 2",
                    "date": "2021-02-17"
                }
            },
            {
                "transaction_id": 10,
                "message": "Bajo construccion",
                "detail": {
                    "amount": 0,
                    "from": "user 1",
                    "to": "user 2",
                    "date": "2021-02-17"
                }
            }
        ]
    }

@app.post("processs/<token>")
def transaction_processing(token):
    return {"code": 201, "token": token}

