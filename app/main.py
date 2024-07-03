from fastapi import FastAPI, HTTPException
from redis_package.redis_operation import RedisClient
from redis_package.config import redis_config

app = FastAPI()
client = RedisClient(config=redis_config)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Redis API"}


@app.post("/queue/push/{pairs:path}")
def push_items(pairs: str):
    try:
        pairs_list = pairs.split('/')
        if len(pairs_list) % 2 != 0:
            raise HTTPException(status_code=400, detail="Invalid number of parameters. Must be in key/value pairs.")

        count = 0
        for i in range(0, len(pairs_list), 2):
            key = pairs_list[i]
            value = pairs_list[i + 1]
            client.push(key, value)
            count += 1

        return {"message": f"Pushed {count} items. Current queue lengths: {get_all_lengths()}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/queue/pop/{key}")
def pop_item(key: str):
    try:
        item = client.pop(key)
        return {"message": f"Popped item: {item.decode('utf-8') if item else 'Queue is empty'}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/queue/get_all")
def get_all_items():
    try:
        keys = client.get_all_keys()
        all_items = {key.decode('utf-8'): [item.decode('utf-8') for item in client.get_all(key.decode('utf-8'))] for key
                     in keys if client.is_list(key.decode('utf-8'))}
        return all_items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/queue/remove/{key}/{value}")
def remove_item(key: str, value: str):
    try:
        count = client.remove(key, value)
        return {"message": f"Removed {count} instances of {value} from {key}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/queue/update/{key}/{index}/{value}")
def update_item(key: str, index: int, value: str):
    try:
        success = client.update(key, index, value)
        if success:
            return {"message": f"Updated item at index {index} in {key} to {value}"}
        else:
            return {"message": f"Failed to update item at index {index} in {key}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_all_lengths():
    try:
        keys = client.get_all_keys()
        lengths = {key.decode('utf-8'): client.len(key.decode('utf-8')) for key in keys if
                   client.is_list(key.decode('utf-8'))}
        return lengths
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
