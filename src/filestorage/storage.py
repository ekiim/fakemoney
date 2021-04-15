"""Modulo de almacenamiento
En este modulo crearemos las funciones para almacenar
registros en un sitema de archivos.
"""

from time import time
from os import environ
from os.path import relpath
from pathlib import Path
import json


def store_new_record(
    collection, name, data,
    timestamp=None, storage_dir=environ["STORAGE_DIR"]
):
    storage_path = Path(storage_dir)
    if not (storage_path / collection).exists():
        (storage_path / collection).mkdir(parents=True)
    if timestamp is None:
        timestamp = time()
    target_file = collection / Path(f"{timestamp}_{name}.json")
    if isinstance(data, dict):
        text = json.dumps(data)
    elif isinstance(data, str):
        text = data
    (storage_dir / target_file).write_text(text)
    return target_file.name


def query_collection(
    collection,
    filter_func=lambda d: True,
    storage_dir=environ["STORAGE_DIR"]
):
    storage_path = Path(storage_dir)
    target_collection = storage_path / collection
    if not target_collection.exists():
        returnable = []
    else:
        returnable = list(filter(
            filter_func,
            map(
                lambda p: relpath(str(p), str(target_collection)),
                target_collection.iterdir()
            )
        ))
    return returnable


def retrieve_record(
    collection,
    filename,
    storage_dir=environ["STORAGE_DIR"]
):
    storage_path = Path(storage_dir)
    target_file = storage_path / collection / filename
    if not (target_file).exists():
        raise Exception("File not found")
    return json.loads(target_file.read_text())
