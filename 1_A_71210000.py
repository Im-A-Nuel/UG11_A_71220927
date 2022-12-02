print('======= Program Manipulasi String =======\n\r Pilihan Menu : \n\r 1. Hitung kata\n\r 2. Ubah Kata')
pilihan=input('Pilihan anda :')
kata=input('Masukan sebuah kalimat/kata :')

def hitung_kata():
    a=input('Masukan kata yang ingin dihitung :')
    x1=kata.count(a)
    print('Terdapat sebanyak', x1, 'kata',a , 'di dalam kalimat')

def ubah_kata():
    k=input('Masukan kata yang ingin diubah :')
    l=input('Masukan kata pengganti :')
    x2=kata.replace(k,l)
    
    print('String berhasil diubah menjadi :', x2)

if pilihan == "1":
    hitung_kata()

elif pilihan == "2":
    ubah_kata()

else :
    print("Pilihan yang anda input tidak terdaftar di daftar pilihan")