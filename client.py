import xmlrpc.client

tambah = xmlrpc.client.ServerProxy("http://127.0.0.1:8000/", allow_none=True)
tampil = xmlrpc.client.ServerProxy("http://127.0.0.1:12000/", allow_none=True)
hapus = xmlrpc.client.ServerProxy("http://127.0.0.1:11000/", allow_none=True)
ambil = xmlrpc.client.ServerProxy("http://127.0.0.1:10000/", allow_none=True)

def valid_angka(num):
    while True:
        try:
            return int(input(num))
        except:
            print("Inputan harus berupa angka")

while True:
    print("\n====== Inventory Management ======")
    print("1. Tambah")
    print("2. Hapus")
    print("3. Ambil")
    print("4. Ping")
    print("5. Keluar")
    # print("==================================")
    print("======= Inventory saat ini =======")
    for i, j in tampil.tampil_item().items():
        print(f"{i:<5} : {j}")
    # print(tampil.tampil_item())       
    print("==================================")
    inv = valid_angka("Masukkan pilihan anda: ")
    if (inv == 1):
        print("== Tambah barang ==")
        tmb = str(input("Masukkan nama barang: "))
        qnt = valid_angka("Masukkan jumlah: ")
        tambah.tambah_item(tmb, qnt)    

    elif(inv == 2):
        print("== Hapus barang ==")
        hps = str(input("Masukkan nama barang: "))
        hapus.hapus_item(hps)

    elif(inv == 3):
        print("== Ambil barang ==")
        amb = str(input("Masukkan nama barang: "))
        qnt = valid_angka("Masukkan jumlah: ")
        ambil.ambil_item(amb, qnt)

    elif(inv == 4):
        ambil.ping()

    elif(inv == 5):
        break

    else:
        pass