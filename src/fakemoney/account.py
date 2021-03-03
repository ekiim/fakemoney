from time import time
import fakemoney.types as types
import fakemoney.picture as picture


fields = {
    "created_time": float,
    "uuid": types.UUID,
    "picture": picture,
    "owner": types.str_nonempty,
    "users": types.list_of(types.str_nonempty),
    "blocked": bool
}

validate = types.isValidConstructor(fields)

def create(owner=None, users=None, timestamp=None, blocked=None):
    if users is None:
        users = []
    if timestamp is None:
        timestamp = time()
    return {
        "created_time": timestamp,
        "owner": owner,
        "picture": picture.create(),
        "uuid": types.UUID.create(owner, _collection="account"),
        "users": users,
        "blocked": False
    }
