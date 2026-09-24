from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

storage = xmlrpc.client.ServerProxy("http://localhost:9000")

class Inventory:

    def ambil_item(self, name, quantity):
        if quantity < 0:
            return "Item {} tidak bisa diambil, tidak boleh minus".format(
                name
            )
        stok_lama = storage.get_item(name)
        stok_baru = stok_lama - quantity
        storage.set_item(name, stok_baru)
        return "Item {} berhasil diambil. Stok saat ini : {}".format(
            name, stok_baru
        )

port = 10000
server = SimpleXMLRPCServer(("localhost", port), allow_none=True)
inventory = Inventory()
server.register_instance(inventory)
print(f"Server berjalan di port {port}...")
server.serve_forever()

