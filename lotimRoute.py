import os, csv
from itertools import permutations
import lotimRoute
from Main import *
import Dashoard
lintasan=""
# database="database.csv"
data_salesman = []
data_user = []
# tampung_username = []
# tampung_password = []

lombok_timur_route=[
    [0,1,2,3,4],
    [1,0,51,38,21],
    [2,51,0,16,36],
    [3,38,16,0,25],
    [4,21,36,25,0]
   
]

def daftar_kota_lotim():
    pilihan = input("Konfirmasi pilihan anda : ")
    if pilihan == '3':
        lotimRoute.menu_kota_lotim()
        lotimRoute.lotim(lombok_timur_route, start)
        lotimRoute.hasil_lintasan_lotim()
    elif pilihan == '0':
        confirm = input("Apakah anda yakin untuk keluar ? [y/n]")
        if confirm == 'y':
            main_menu()
        else:
            Dashoard.dashboard()
    else:
        Dashoard.dashboard()

  
def menu_kota_lotim():
    os.system("clear")
    global start
    print("||"+"Daftar Menu Kota".center(104)+"||")
    print("="*108)
    print("||"+"0 = Aikmel".ljust(104)+"||")
    print("||"+"1 = Jerowaru".ljust(104)+"||")
    print("||"+"2 = Keruak".ljust(104)+"||")
    print("||"+"3 = Labuhan haji".ljust(104)+"||")
    print("||"+"4 = Masbagik".ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    start = int(input("Masukan titik awal: "))

# mataram
def lotim(lombok_timur_route, start):
    global lintasan
    tampung_point = []
    lintasan_tsp = []
    for point in range(len(lombok_timur_route)):
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
            current_cost += lombok_timur_route[baris][kolom]
            baris = kolom
        kota_awal(start)
        current_cost +=lombok_timur_route[baris][start]
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
        lintasan += "Aikmel"
    elif start == 1:
        lintasan += "Jerowaru"
    elif start == 2:
        lintasan += "Keruak"
    elif start == 3:
        lintasan += "Labuhan haji"
    elif start == 4:
        lintasan += "Masbagik"

def kota_tengah(kolom):
    global lintasan
    if kolom == 0:
        lintasan+="Aikmel-->"
    elif kolom == 1:
        lintasan+="Jerowaru-->"
    elif lintasan == 2:
        lintasan+="Keruak-->"
    elif kolom == 3:
        lintasan+="Labuhan haji-->"
    elif kolom == 4:
        lintasan+="Masbagik-->"

def hasil_lintasan_lotim():
    cost_bbm = 1000
    pertamax = 4
    jmlh_pertamax = lotim(lombok_timur_route, start)[0]/pertamax
    total_biaya = lotim(lombok_timur_route, start)[0]/pertamax*cost_bbm
    print("="*108)
    print("||"+"Kesimpulan".center(104)+"||")
    print("="*108)
    print("||"+" Lintasan Terpendek : ", lotim(lombok_timur_route, start)[0], "km".ljust(74)+"||")
    print("||"+" Menghabiskan Pertamax : ", jmlh_pertamax, "liter".ljust(72)+"||")
    print("||"+" Total Biaya : ", total_biaya, "liter".ljust(68)+"||")
    for i in range(len(lotim(lombok_timur_route, start)[2])):
        print("||"+" Lintasan yang dilalui : ", lotim(lombok_timur_route,start)[2][i].ljust(77)+"||")
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
    kota = ["Aimel", "jerowaru", "Keruak", "Labuhan haji", "Masbagik"]
    menu_kota_lotim()
    input("Tekan untuk melihat route")
    print("="*108)
    print("||"+"Detail route".center(104)+"||")
    print("="*108)
    for i in range(len(lombok_timur_route)):
        cost = str(kota[start])+"-->"+str(kota[i])+" = "+str(lombok_timur_route[start][i])+" km"
        print("||"f' {cost}'.ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)







