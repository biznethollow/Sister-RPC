from socketserver import ThreadingMixIn
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

storage = xmlrpc.client.ServerProxy("http://localhost:9000")

class ThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

class Inventory:

    def hapus_item(self, name):
        if(storage.delete_item(name)):
            return "Item {} berhasil dihapus".format(
                name
            )
        else:
            return "Item {} tidak bisa dihapus".format(
                name
            )

    def ping(self):
        if "ping-2" in storage.get_items():
            p = storage.get_item("ping-2") + 1
            storage.set_item("ping-2", p)
        else:
            storage.set_item("ping-2", 1)
        storage.ping()

port = 11000
server = ThreadedXMLRPCServer(("localhost", port), allow_none=True)
inventory = Inventory()
server.register_instance(inventory)
print(f"Server berjalan di port {port}...")
server.serve_forever()

