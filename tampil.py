from socketserver import ThreadingMixIn
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

storage = xmlrpc.client.ServerProxy("http://localhost:9000")

class ThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

class Inventory:

    def tampil_item(self):
        return storage.get_items()

    def ping(self):
        if "ping-5" in storage.get_items():
            p = storage.get_item("ping-5") + 1
            storage.set_item("ping-5", p)
        else:
            storage.set_item("ping-5", 1)

port = 12000
server = ThreadedXMLRPCServer(("localhost", port), allow_none=True)
inventory = Inventory()
server.register_instance(inventory)
print(f"Server berjalan di port {port}...")
server.serve_forever()

