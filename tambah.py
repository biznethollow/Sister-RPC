from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

storage = xmlrpc.client.ServerProxy("http://localhost:9000")

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

port = 8000
server = SimpleXMLRPCServer(("localhost", port), allow_none=True)
inventory = Inventory()
server.register_instance(inventory)
print(f"Server berjalan di port {port}...")
server.serve_forever()

