print("========== Kelompok 19 ==========")
print("Rajwa Vourza Tsaqifa (21120123130091)")
print("Arga Mulyana Saputra (211201231300665)")
print("Denok Intan Permata Sari (21120123130059)")

class ATM:
    def __init__(self, saldo_awal):
        self.saldo = saldo_awal

    # Method tanpa parameter dan non return type
    def tampilkan_menu(self):
        print("Selamat datang di ATM")
        print("1. Cek Saldo")
        print("2. Tarik Tunai")
        print("3. Setor Tunai")
        print("4. Keluar")

    # Method dengan parameter dan return type
    def cek_saldo(self):
        return self.saldo

# Function dengan parameter dan non return type
def tarik_tunai(atm, jumlah_tarik):
    if jumlah_tarik > atm.saldo:
        print("Saldo tidak mencukupi")
    else:
        atm.saldo -= jumlah_tarik
        print("Penarikan tunai sebesar", jumlah_tarik, "berhasil")
        print("Saldo Anda sekarang:", atm.saldo)

# Function dengan parameter dan non return type
def setor_tunai(atm, jumlah_setor):
    atm.saldo += jumlah_setor
    print("Setor tunai sebesar", jumlah_setor, "berhasil")
    print("Saldo Anda sekarang:", atm.saldo)

# Main program
atm = ATM(1000000)  # Saldo awal ATM

while True:
    atm.tampilkan_menu()
    pilihan = int(input("Masukkan pilihan: "))

    if pilihan == 1:
        print("Saldo Anda:", atm.cek_saldo())
    elif pilihan == 2:
        jumlah_tarik = int(input("Masukkan jumlah tarik tunai: "))
        tarik_tunai(atm, jumlah_tarik)
    elif pilihan == 3:
        jumlah_setor = int(input("Masukkan jumlah setor tunai: "))
        setor_tunai(atm, jumlah_setor)
    elif pilihan == 4:
        print("Terima kasih telah menggunakan ATM. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang sesuai.")
