from xmlrpc.server import SimpleXMLRPCServer

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

port = 9000
server = SimpleXMLRPCServer(("localhost", port), allow_none=True)
inventory = Inventory()
server.register_instance(inventory)
print(f"Server berjalan di port {port}...")
server.serve_forever()
