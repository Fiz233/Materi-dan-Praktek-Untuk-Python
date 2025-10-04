# nah ini yang pernah kita pelajari sebelumnya
# ada kondisi if, else, dan elif

angka = int(input("masukan angka random: (0-100) "))

if angka >= 90:                     # kondisi if digunakan saat kondisi tersebut menemui kriteria tersebut 
    print("kamu dapat nilai A")
elif angka >= 70:                   # kondisi elif digunakan saat kemungkinan berbeda dari kriteria pertama
    print("kamu dapat nilai B")
else:                               # kondisi else digunakan ketika dari semua kriteria tidak ada yang memenuhi
    print("kamu dapat nilai C")     # maka akan print perintah yang paling akhir