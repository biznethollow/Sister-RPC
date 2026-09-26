from socketserver import ThreadingMixIn
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

storage = xmlrpc.client.ServerProxy("http://localhost:9000")
tampil = xmlrpc.client.ServerProxy("http://localhost:12000")

class ThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

class Inventory:

    def tambah_item(self, name, quantity):
        if quantity < 0:
            return "Item {} tidak bisa ditambahkan, tidak boleh minus".format(
                name
            )
        stok_lama = storage.get_item(name)
        stok_baru = stok_lama + quantity
        storage.set_item(name, stok_baru) 
        return "Item {} berhasil ditambahkan. Stok saat ini : {}".format(
            name, stok_baru
        )

    def ping(self):
        if "ping-4" in storage.get_items():
            p = storage.get_item("ping-4") + 1
            storage.set_item("ping-4", p)
        else:
            storage.set_item("ping-4", 1)
        tampil.ping()

port = 8000
server = ThreadedXMLRPCServer(("localhost", port), allow_none=True)
inventory = Inventory()
server.register_instance(inventory)
print(f"Server berjalan di port {port}...")
server.serve_forever()

