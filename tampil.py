import xmlrpc.client
import Pyro4

storage = xmlrpc.client.ServerProxy("http://localhost:9000")
tampil = Pyro4.core.Proxy('PYRO:Tampil@localhost:12000')

@Pyro4.expose
class Tampil(object):
    def tampil_item(self):
        return storage.get_items()

    def ping(self):
        if "ping-5" in storage.get_items():
            p = storage.get_item("ping-5") + 1
            storage.set_item("ping-5", p)
        else:
            storage.set_item("ping-5", 1)
        return storage.get_item("ping-5")

port = 12000
daemon = Pyro4.Daemon(host="localhost", port=port)   
uri = daemon.register(Tampil(), objectId="Tampil")   
print(f"Server Tampil (Pyro4) berjalan di port {port}...")
print("URI:", uri)                                   
daemon.requestLoop()                                 