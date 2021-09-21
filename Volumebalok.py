#volume balok

class VolumeBalok :
    Panjang = None
    Lebar = None
    Tinggi = None

#membangun instance/variable sebagai"objek nyata"
VB = VolumeBalok()
VolumeBalok.Panjang = 9
VolumeBalok.Lebar = 7
VolumeBalok.Tinggi = 5

Hasil = VolumeBalok.Panjang*VolumeBalok.Lebar*VolumeBalok.Tinggi

#output yang akan ditampilkan
print("Panjang Balok :", VolumeBalok.Panjang)
print("lebar Balok :", VolumeBalok.Lebar)
print("Tinggi Balok :", VolumeBalok.Tinggi)
print("Hasil Volume Balok :", Hasil)