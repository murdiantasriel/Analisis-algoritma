import os, csv
from itertools import permutations
# from pip import main
import KluRoute
# from Main import *
import Dashoard
lintasan=""
# database="database.csv"
data_salesman = []
data_user = []
# tampung_username = []
# tampung_password = []
                          

klu_route = [
    [0,1,2,3,4,5],
    [1,0,45,32,62,47],
    [2,45,0,27,31,17],
    [3,32,27,0,44,30],
    [4,62,31,44,0,14],
    [5,47,17,30,14,0]
]

def daftar_kota_klu():
    pilihan = input("Konfirmasi pilihan anda : ")
    if pilihan == '5':
        KluRoute.menu_kota_klu()
        KluRoute.klu(klu_route, start)
        KluRoute.hasil_lintasan_klu()
    elif pilihan == '0':
        confirm = input("Apakah anda yakin untuk keluar ? [y/n]")
        if confirm == 'y':
            main_menu()
        else:
            Dashoard.dashboard()
    else:
        print("sesuaikan dengan pilihan anda sebelumnya")
        Dashoard.dashboard()

  
def menu_kota_klu():
    os.system("clear")
    global start
    print("||"+"Daftar Menu Kota".center(104)+"||")
    print("="*108)
    print("||"+"1 = Bayan".ljust(104)+"||")
    print("||"+"2 = Gangga".ljust(104)+"||")
    print("||"+"3 = Kayangan".ljust(104)+"||")
    print("||"+"4 = Pemenang".ljust(104)+"||")
    print("||"+"5 = Tanjung".ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    start = int(input("Masukan titik awal: "))

# klu
def klu(klu_route, start):
    global lintasan
    tampung_point = []
    lintasan_tsp = []
    for point in range(len(klu_route)):
        if point != start:
            tampung_point.append(point)
    min_cost = 1000000
    tampung_permutasi = permutations(tampung_point)
    for permutasi in tampung_permutasi:
        kota_awal(start)
        lintasan+="-->"
        current_cost = 0
        baris = start
        for kolom in permutasi:
            kota_tengah(kolom)
            current_cost += klu_route[baris][kolom]
            baris = kolom
        kota_awal(start)
        current_cost +=klu_route[baris][start]
        lintasa_copy = lintasan
        if current_cost == min_cost:
            lintasan_tsp.append(lintasa_copy)
        elif current_cost < min_cost:
            lintasan_tsp.clear()
            lintasan_tsp.append(lintasa_copy)
        min_cost = min(min_cost, current_cost)
        lintasan = ""
    return min_cost,lintasan, lintasan_tsp

def kota_awal(start):
    global lintasan
    if start == 0:
        pass
    elif start == 1:
        lintasan += "Bayan"
    elif start == 2:
        lintasan += "Gangga"
    elif start == 3:
        lintasan += "Kayangan"
    elif start == 4:
        lintasan += "Pemenang"
    elif start == 5:
        lintasan += "Tanjung"

def kota_tengah(kolom):
    global lintasan
    if kolom == 0:
        pass
    elif kolom == 1:
        lintasan+="Bayan-->"
    elif kolom == 2:
        lintasan+="Gangga-->"
    elif lintasan == 3:
        lintasan+="Kayangan-->"
    elif kolom == 4:
        lintasan+="Pemenang-->"
    elif kolom == 5:
        lintasan+="Tanjung-->"

def hasil_lintasan_klu():
    cost_bbm = 1000
    pertamax = 4
    jmlh_pertamax = klu(klu_route, start)[0]/pertamax
    total_biaya = klu(klu_route, start)[0]/pertamax*cost_bbm
    print("="*108)
    print("||"+"Kesimpulan".center(104)+"||")
    print("="*108)
    print("||"+" Lintasan Terpendek : ", klu(klu_route, start)[0], "km".ljust(74)+"||")
    print("||"+" Menghabiskan Pertamax : ", jmlh_pertamax, "liter".ljust(72)+"||")
    print("||"+" Total Biaya : ", total_biaya, "liter".ljust(68)+"||")
    for i in range(len(klu(klu_route, start)[2])):
        print("||"+" Lintasan yang dilalui : ", klu(klu_route,start)[2][i].ljust(77)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    input("Tekan enter untuk kembali")
    dash()
def dash():
    os.system("clear")
    print("="*108)
    print("||"+"NinjaGo".center(104)+"||")
    print("="*108)
    print("||"+"    [1] = Detail Route".ljust(104)+"||")
    print("||"+"    [0] = Keluar".ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    pilihan = input("Masukan pilihan anda : ")
    if pilihan == '1':
        detail()  
    elif pilihan == '0':
        confirm = input("Apakah anda yakin untuk keluar ? [y/n]")
        if confirm == 'y':
            main_menu()
        else:
            Dashoard.dashboard()
    else:
        Dashoard.dashboard()

def detail():
    kota = ["Bayan", "Gangga", "Kayangan", "Pemenang", "Tanjung"]
    menu_kota_klu()
    input("Tekan untuk melihat route")
    print("="*108)
    print("||"+"Detail route".center(104)+"||")
    print("="*108)
    for i in range(len(klu_route)):
        cost = str(kota[start])+"-->"+str(kota[i])+" = "+str(klu_route[start][i])+" km"
        print("||"f' {cost}'.ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)







