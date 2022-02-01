import os, csv
from itertools import permutations
import lotengRoute
from Main import *
import Dashoard
lintasan=""
# database="database.csv"
data_salesman = []
data_user = []
# tampung_username = []
# tampung_password = []

lombok_tengah_route=[
    [0,1,2,3,4],
    [1,0,14.2,25.3,17.7],
    [2,14.2,0,18,7.8],
    [3,25.3,18,0,9.6],
    [4,17.7,7.8,9.6,0] 
   
]

def daftar_kota_loteng():
    pilihan = input("Konfirmasi pilihan anda : ")
    if pilihan == '4':
        lotengRoute.menu_kota_loteng()
        lotengRoute.loteng(lombok_tengah_route, start)
        lotengRoute.hasil_lintasan_loteng()
    elif pilihan == '0':
        confirm = input("Apakah anda yakin untuk keluar ? [y/n]")
        if confirm == 'y':
            main_menu()
        else:
            Dashoard.dashboard()
    else:
        Dashoard.dashboard()

  
def menu_kota_loteng():
    os.system("clear")
    global start
    print("||"+"Daftar Menu Kota".center(104)+"||")
    print("="*108)
    print("||"+"0 = Janapria".ljust(104)+"||")
    print("||"+"1 = Kopang".ljust(104)+"||")
    print("||"+"2 = Pringgarata".ljust(104)+"||")
    print("||"+"3 = Batukliang".ljust(104)+"||")
    print("||"+"4 = Praya".ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    start = int(input("Masukan titik awal: "))

# mataram
def loteng(lombok_tengah_route, start):
    global lintasan
    tampung_point = []
    lintasan_tsp = []
    for point in range(len(lombok_tengah_route)):
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
            current_cost += lombok_tengah_route[baris][kolom]
            baris = kolom
        kota_awal(start)
        current_cost +=lombok_tengah_route[baris][start]
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
        lintasan += "Janapria"
    elif start == 1:
        lintasan += "Kopang"
    elif start == 2:
        lintasan += "Pringgarata"
    elif start == 3:
        lintasan += "Batukliang"
    elif start == 4:
        lintasan += "Praya"

def kota_tengah(kolom):
    global lintasan
    if kolom == 0:
        lintasan+="Janapria-->"
    elif kolom == 1:
        lintasan+="Kopang-->"
    elif lintasan == 2:
        lintasan+="Pringgarata-->"
    elif kolom == 3:
        lintasan+="Batukliang-->"
    elif kolom == 4:
        lintasan+="Praya-->"

def hasil_lintasan_loteng():
    cost_bbm = 1000
    pertamax = 4
    jmlh_pertamax = loteng(lombok_tengah_route, start)[0]/pertamax
    total_biaya = loteng(lombok_tengah_route, start)[0]/pertamax*cost_bbm
    print("="*108)
    print("||"+"Kesimpulan".center(104)+"||")
    print("="*108)
    print("||"+" Lintasan Terpendek : ", loteng(lombok_tengah_route, start)[0], "km".ljust(74)+"||")
    print("||"+" Menghabiskan Pertamax : ", jmlh_pertamax, "liter".ljust(72)+"||")
    print("||"+" Total Biaya : ", total_biaya, "liter".ljust(68)+"||")
    for i in range(len(loteng(lombok_tengah_route, start)[2])):
        print("||"+" Lintasan yang dilalui : ", loteng(lombok_tengah_route,start)[2][i].ljust(77)+"||")
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
    kota = ["Janapria", "Kopang", "Pringgarata", "Batukliang", "Praya"]
    menu_kota_loteng()
    input("Tekan untuk melihat route")
    print("="*108)
    print("||"+"Detail route".center(104)+"||")
    print("="*108)
    for i in range(len(lombok_tengah_route)):
        cost = str(kota[start])+"-->"+str(kota[i])+" = "+str(lombok_tengah_route[start][i])+" km"
        print("||"f' {cost}'.ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)







