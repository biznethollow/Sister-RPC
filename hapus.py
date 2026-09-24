from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

storage = xmlrpc.client.ServerProxy("http://localhost:9000")

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

port = 11000
server = SimpleXMLRPCServer(("localhost", port), allow_none=True)
inventory = Inventory()
server.register_instance(inventory)
print(f"Server berjalan di port {port}...")
server.serve_forever()

