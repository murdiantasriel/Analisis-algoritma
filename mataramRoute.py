import os, csv
from itertools import permutations
# from pip import main
import mataramRoute
# from Main import *
import Dashoard
lintasan=""
# database="database.csv"
data_salesman = []
data_user = []
# tampung_username = []
# tampung_password = []
                          

mataram_route = [
    [0,1,2,3,4],
    [1,0,4.3,6.9,7.8],
    [2,4.3,0,4.7,11],
    [3,6.9,4.7,0,12],
    [4,7.8,11,12,0]
]

def daftar_kota_mataram():
    pilihan = input("Konfirmasi pilihan anda : ")
    if pilihan == '1':
        mataramRoute.menu_kota_mataram()
        mataramRoute.mataram(mataram_route, start)
        mataramRoute.hasil_lintasan_mtr()
    elif pilihan == '0':
        confirm = input("Apakah anda yakin untuk keluar ? [y/n]")
        if confirm == 'y':
            main_menu()
        else:
            Dashoard.dashboard()
    else:
        Dashoard.dashboard()

  
def menu_kota_mataram():
    os.system("clear")
    global start
    print("||"+"Daftar Menu Kota".center(104)+"||")
    print("="*108)
    print("||"+"0 = Selaparang".ljust(104)+"||")
    print("||"+"1 = Ampenan".ljust(104)+"||")
    print("||"+"2 = Sekarbela".ljust(104)+"||")
    print("||"+"3 = Sandubaya".ljust(104)+"||")
    print("||"+"4 = Cakranegara".ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    start = int(input("Masukan titik awal: "))

# mataram
def mataram(mataram_route, start):
    global lintasan
    tampung_point = []
    lintasan_tsp = []
    for point in range(len(mataram_route)):
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
            current_cost += mataram_route[baris][kolom]
            baris = kolom
        kota_awal(start)
        current_cost +=mataram_route[baris][start]
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
        lintasan += "Selaparang"
    elif start == 1:
        lintasan += "Ampenan"
    elif start == 2:
        lintasan += "Sekarbela"
    elif start == 3:
        lintasan += "Sandubaya"
    elif start == 4:
        lintasan += "Cakranegara"

def kota_tengah(kolom):
    global lintasan
    if kolom == 0:
        lintasan+="Selaparang-->"
    elif kolom == 1:
        lintasan+="Ampenan-->"
    elif lintasan == 2:
        lintasan+="SEkarbela-->"
    elif kolom == 3:
        lintasan+="Sandubaya-->"
    elif kolom == 4:
        lintasan+="Cakranegara-->"

def hasil_lintasan_mtr():
    cost_bbm = 1000
    pertamax = 4
    jmlh_pertamax = mataram(mataram_route, start)[0]/pertamax
    total_biaya = mataram(mataram_route, start)[0]/pertamax*cost_bbm
    print("="*108)
    print("||"+"Kesimpulan".center(104)+"||")
    print("="*108)
    print("||"+" Lintasan Terpendek : ", mataram(mataram_route, start)[0], "km".ljust(74)+"||")
    print("||"+" Menghabiskan Pertamax : ", jmlh_pertamax, "liter".ljust(72)+"||")
    print("||"+" Total Biaya : ", total_biaya, "liter".ljust(68)+"||")
    for i in range(len(mataram(mataram_route, start)[2])):
        print("||"+" Lintasan yang dilalui : ", mataram(mataram_route,start)[2][i].ljust(77)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
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
    kota = ["Selaparang", "Ampenan", "Sekarbela", "Sandubaya", "Sandubaya"]
    menu_kota_mataram()
    input("Tekan untuk melihat route")
    print("="*108)
    print("||"+"Detail route".center(104)+"||")
    print("="*108)
    for i in range(len(mataram_route)):
        cost = str(kota[start])+"-->"+str(kota[i])+" = "+str(mataram_route[start][i])+" km"
        print("||"f' {cost}'.ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)







