from fastapi import FastAPI
import uvicorn
import xmlrpc.client

storage = xmlrpc.client.ServerProxy("http://localhost:9000")

app = FastAPI(title="inv")

@app.delete("/item/{name}")
def hapus_item(name):
    if(storage.delete_item(name)):
        return "Item {} berhasil dihapus".format(
            name
        )
    else:
        return "Item {} tidak bisa dihapus".format(
            name
        )

@app.get("/ping")
def ping():
    storage.ping()
    if "ping-2" in storage.get_items():
        p = storage.get_item("ping-2") + 1
        storage.set_item("ping-2", p)
    else:
        storage.set_item("ping-2", 1)
    return storage.get_item("ping-2")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=11000)
