print('PROGRAM MENGHITUNG LUAS GEOMETRI \n')

print('=====MENGITUNG LUAS PERSEGI PANJANG=====')

# Proses memasukkan yang diketahui
panjang = int(input('Masukkan panjang: '))
lebar = int(input('Masukkan lebar: '))

# Proses pengerjaan
luas = panjang * lebar

# Hasil
print('Luas persegi panjang = ', luas, '\n')

print('=====MENGHITUNG LUAS LINGKARAN=====')

jari_jari = int(input('Masukkan jari-jari: '))

luas = 3.14 * (jari_jari)**2
print('Luas lingkaran = ', luas)
