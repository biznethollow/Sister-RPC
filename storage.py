from socketserver import ThreadingMixIn
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

storage = xmlrpc.client.ServerProxy("http://localhost:9000")
tambah = xmlrpc.client.ServerProxy("http://localhost:8000")

class ThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

class Inventory:
    def __init__(self):
        self.items = {}

    def get_item(self, name):
        return self.items.get(name, 0)

    def set_item(self, name, quantity):
        self.items[name] = quantity
        return True

    def get_items(self):
        return self.items

    def delete_item(self, name):
        if name in self.items:
            del self.items[name]
            return True
        return False

    def ping(self):
        if "ping-3" in storage.get_items():
            p = storage.get_item("ping-3") + 1
            storage.set_item("ping-3", p)
        else:
            storage.set_item("ping-3", 1)
        tambah.ping()

port = 9000
server = ThreadedXMLRPCServer(("localhost", port), allow_none=True)
inventory = Inventory()
server.register_instance(inventory)
print(f"Server berjalan di port {port}...")
server.serve_forever()