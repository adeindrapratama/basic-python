## Tugas akhir Dasar Python
## oleh Ade Indra Pratama

# import library
import datetime #untuk membaca isi library datetime
import random #untuk membaca isi library datetime
import math #untuk membaca isi library math
import os #untuk membaca isi library os
import ast #untuk membaca isi library ast : di gunakan di program untuk menulis file

##default = "maaf, aku belum paham yang kamu tanyakan"

def pilihan():

    pil = input("apakah ada yang bisa aku bantu?: y/t" )

    # Jika user input y akan masuk ke dalam menu yang sudah di definisikan di dalam menu
    # jika user input t program akan keluar
    # jika user input selain y/t akan looping ke def pilihan

    if pil == "y":
        tampilkan_menu()
        #akan masuk ke dalam definisi tampilkan menu
    elif pil == "t":
        print("Program selesai, sampai jumpa!")
    else :
        print("hanya dapat dipilih y/t")
        pilihan()

def tampilkan_menu():
    # pilihan ada 4 dan user dapat memilih salah satu dari 4 pilihan tersebut dengan mengetik angka


    print("--- Menu ---")
    print("1. Kalkulator")
    print("2. Agenda")
    print("3. Chatbot")
    print("4. Selesai")

    print("")
    print("pilih salah satu menu di atas dengan mengetik angkanya saja")
    menu = input("Pilih menu: ")

    if menu == "1":
        menu_1()  # jika user mengetik "1" akan masuk ke definisi menu_1  yang isinya adalah calculator
    elif menu == "2":
        menu_2() # jika user mengetik "2" akan masuk ke definisi menu_2  yang isinya adalah Input Agenda
    elif menu == "3":
        menu_3() # jika user mengetik "3" akan masuk ke definisi menu_3 yang isinya adalah menu chatboot
    elif menu == "4":
        print("Program selesai, sampai jumpa!")
    else:
        print(default)
        menu = input("Pilih menu: ")
        tampilkan_menu()


def menu_1():
    # pada menu_1 ini user akan menginput angka lalu dijumlahkan otomatis oleh import math

    os.system('clear')
    print("menu 1 Kalkulator")
    print("--- Pada Menu Ini akan Menghitung, sinus, cosinus, dan tangen ---")
    w = int(input("Masukkan Angka: "))

    # yang dipakai disini adalah perhtungan sin, cos, dan tan
    x = math.sin(w)
    y = math.cos(w)
    z = math.tan(w)

    # Program akan menampilkan perhitungan atas inputan user tersebut
    print("")
    print("")
    print("angka {} : mempunyai\na.Sinus : {} \nb.Cosinus :{}\nc.tangen :{} ".format(w,x,y,z))
    print("")
    print("")

    #setelah selesai program akan kembali ke menu awal
    tampilkan_menu()


def menu_2():
    # pada menu_2 ini user akan menginput agenda yang disimpan dalam file tugas_akhir.txt
    # file tugas_akhir.txt harus di buat terlebih dahulu oleh user
    os.system('clear')
    print("menu 2 Agenda")

    # jam mengambil otomatis dari libary datetime
    jam = datetime.datetime.now()

    # User diminta untuk menuliskan nama agenda dan isi agendanya
    agenda = input("Nama Agenda: ")
    isi = input("Isi Agenda " )

    # program akan membuka file tugas_akhir, dan akan menambahkan hasil inputan user
    f=open("tugas_akhir.txt","a+")

    # program akan menulis apa yang user input. Penulisan dilakukan di file tugas_akhir.txt

    f.write("nama Agenda : {} \nHari Tanggal {}\nisi : {} \n\n".format(agenda,jam,isi))

    #setelah selesai program akan kembali ke menu awal
    print("")
    print("")
    print("agenda sudah di tambahkan")
    print("")
    tampilkan_menu()

def menu_3():
    os.system('clear')
    # pada menu_3 ini user akan diberikan chat bot, user cukup mengetik angka 3, dan otomatis chatbot akan mulai
    # untuk menggunakan chat bot ini menggunakan library #random

    print("Menu 3 Chatbot")

    # tgl mengambil otomatis dari libary datetime
    tgl = datetime.datetime.now()

    # tanggal mengambil tanggal saja dari tgl, dapat diubah sesuai kebutuhan
    tanggal = tgl.strftime("%d")

    # default jika pertanyaannya tidak dapat di jawab
    default = "maaf, aku belum paham yang kamu tanyakan"

    # list jawaban nama. format(nama) diambil dari yang di masukkan di awal
    jawaban_nama = [
    "nama saya  {0}".format(nama),
    "orang-orang memanggil saya {0}".format(nama),
    "panggil saja saya {0}".format(nama),
    "boleh saja kalau di panggil {0}".format(nama),
    "silahkan panggil saya {0}".format(nama)
    ]

    # list jawaban tanggal. format(tanggal) diambil otomatis dari variabel tanggal
    jawaban_tanggal = [
      "hari ini tanggal {0}".format(tanggal),
      "ya ampun masa tidak tahu, hari ini tanggal {0}".format(tanggal)
    ]


    #program akan merandom list nama dan tanggal. untuk melakukan random menggunakan library #random
    nama_random = random.choice(jawaban_nama)
    random_tanggal = random.choice(jawaban_tanggal)

    #dictionary pertanyaan, dengan jawaban yang sudah di random
    pertanyaan = {
    "nama kamu siapa?": nama_random,
    "kamu siapa?" : nama_random,
    "tanggal berapa hari ini?": random_tanggal,
    "hari ini tanggal berapa?" : random_tanggal,
    "default": default
    }

    # untuk melakukan random dictionary
    # didapat referensi membaca
    # https://stackoverflow.com/questions/4859292/how-to-get-a-random-value-from-dictionary-in-python

    i = random.randint(0, len(pertanyaan) - 1)

    a = list(pertanyaan)[i]
    b = pertanyaan[list(pertanyaan)[i]]

    # menampilkan pertanyaan yang di random
    print("")
    print("")
    print("")
    print (a,b)
    print("")
    print("")
    print("")

    #setelah selesai program akan kembali ke menu awal
    tampilkan_menu()


## Mulai Program
os.system('clear')

print("Hai aku AIs, asisten virtual pertamamu")
print("Siapa namamu")

## Masukkan Nama
nama = input("Masukkan nama: " )

print("Salam kenal {}".format(nama))

#masuk ke definisi pilihan
pilihan()
