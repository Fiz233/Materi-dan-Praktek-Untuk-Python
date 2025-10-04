# disini adanya operator logika, yaitu gunanya tuh saat kita mencoba menggabungkan sebuah kondisi seperti

orang = str("apis")
orang_2 = str("budi")
lulus = True

# Kondisi "and"
print(orang and orang_2) # digunakan saat menggabung kan kedua variable

# kondisi "or"
print(orang or orang_2) # digunakan saat menentukan mana yang harus di print sesuai dengan kondisi

# kondisi not
if not lulus:
    print("Pengguna tidak lulus")
else:
    print("pengguna lulus") # digunakan saat kondisi nya tidak True maka akan meng output perintah pertama, dan yang keduanya sebaliknya

