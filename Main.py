import os, csv
import Dashoard
# import klu
from itertools import permutations
# lintasan=""
database="database.csv"

data_salesman = []
data_user = []
tampung_username = []
tampung_password = []

try:
    with open("database.csv", "r") as cswrite:
        reader = csv.reader(cswrite, delimiter=",")
        for baris in reader:
            data_salesman.append(baris)
except:
    pass
# main tidak perlu dirubah
def main_menu():
    os.system("clear")
    print("="*108)
    print("||"+"Ninjago ".center(104)+"||")
    print("||"+"Selamat Datang di Aplikasi Ninjago".center(104)+"||")
    print("||"+"Silahkan login jika anda telah memiliki akun".center(104)+"||")
    print("||"+"dan Silahkan mendaptar jika belum memiliki akun".center(104)+"||")
    print("="*108)
    print("||"+"[1] Masuk ".ljust(103)+"||")
    print("||"+"[2] Daftar".ljust(103)+"||")
    print("||"+"[3] Keluar".ljust(103)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    pilih = input("Masukan pilihan anda: ")
    if pilih == "1":
        login()
    elif pilih == "2":
        register()
    elif pilih == "3":
        exit()

def register():
    os.system("clear")
    errors = 0
    print("="*108)
    print("||"+"NinjaGo".center(104)+"||")
    print("="*108)
    username = input(" Usnername    :")
    password = input(" Password     :")
    if username.isalnum() == False or password.isalnum() == False:
        errors += 1
        print("Username atau password hanya berupa huruf dan angka saja")
    if len(username) < 5 or len(password) < 5:
        errors += 1
        print("Username atau password minimal terdiri dari 6 karakter")
    if username == password:
        errors = 1
        print("Username dan password tidak boleh sama")
    if errors == 0:
        data_salesman.append([username, password])
        with open("database.csv", "a", newline="") as css:
            write = csv.writer(css, delimiter=",")
            for t in data_salesman:
                write.writerow(t)
        print("Akun anda berhasil dibuat, silahkan login1")
    input("Tekan enter untuk kembali")
    main_menu() 

def login():
    os.system("clear")
    print("="*108)
    print("||"+"Ninjago".center(104)+"||")
    print("="*108)
    nama = []
    sandi = []
    with open("database.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        try:
            for row in csv_reader:
                nama.append(row[0])
                sandi.append(row[1])
        except:
            pass
    username = input("Username :")
    password = input("Password :")
    if username in nama:
        index = nama.index(username)
        if password == sandi[index]:
            Dashoard.dashboard()
        else:
            print("Password anda salah")
    else:
        print("Akun tidak ditemukan")
    input("Enter untuk kembali")
    main_menu()
    

if __name__ == "__main__":
    main_menu()





