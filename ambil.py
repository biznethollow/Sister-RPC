from socketserver import ThreadingMixIn
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

storage = xmlrpc.client.ServerProxy("http://localhost:9000")
hapus = xmlrpc.client.ServerProxy("http://localhost:11000")

class ThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

class Inventory:
    
    def ambil_item(self, name, quantity):
        if quantity < 0:
            return "Item {} tidak bisa diambil, tidak boleh minus".format(
                name
            )
        stok_lama = storage.get_item(name)
        stok_baru = stok_lama - quantity
        if stok_baru < 0:
            return f"Tidak boleh melebihi stok"
        storage.set_item(name, stok_baru)
        return "Item {} berhasil diambil. Stok saat ini : {}".format(
            name, stok_baru
    )

    def ping(self):
        if "ping-1" in storage.get_items():
            p = storage.get_item("ping-1") + 1
            storage.set_item("ping-1", p)
        else:
            storage.set_item("ping-1", 1)
        hapus.ping()

port = 10000
server = ThreadedXMLRPCServer(("localhost", port), allow_none=True)
inventory = Inventory()
server.register_instance(inventory)
print(f"Server berjalan di port {port}...")
server.serve_forever()

