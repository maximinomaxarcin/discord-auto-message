import requests
import random
import time
import os
from colorama import Fore

print ("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print ("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⢂⣠⣰⣶⣾⣾⣿⣷⣷⣾⣿⣼⣷⣾⣴⣶⣤⣠⡀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print ("⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⠀⠀⠀⠀⠀⠈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print ("⠀⠀⠀⠀⠀⠀⡀⢁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡣⢝⡀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print ("⠀⠀⠀⠀⠀⠀⣠⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡕⣃⠄⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿")
print ("⠀⠀⠀⠀⠀⠰⣽⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⢆⠁⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿")
print ("⠀⠀⠀⠀⡀⢳⢫⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⠀⠠⠀⠠⠈⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿")
print ("⠀⠀⠀⠀⠀⣎⡳⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⠛⠋⠛⠛⠛⠻⠛⢥⠃⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿")
print ("⠀⠀⠀⠀⠀⠎⠙⠋⠙⠛⠛⠛⠛⣿⣿⣿⣿⣿⣿⡗⢉⢠⡤⠖⣰⣤⣶⣦⣤⣄⡀⢢⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿")
print ("⠀⠀⠀⠠⠀⠀⣀⣤⣤⡴⠴⠔⡤⠿⣿⣿⣿⣿⣿⡏⠠⢚⣤⣿⣿⣶⣤⣤⣏⠣⠉⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⣿⣿⡿⣻⣿")
print ("⠀⠀⠀⠀⠀⡰⢊⡭⠛⠛⠿⠶⡈⠷⠾⢻⠿⠛⡛⡋⢠⡾⠋⠈⠀⠐⠲⠀⠀⠀⠀⠈⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠿⠿⢯⡷⢏⣿")
print ("⠀⠀⠈⠀⠀⠐⠁⠀⠘⠃⠁⠀⠀⢐⣁⣵⣿⣟⠀⡆⠽⡇⠀⠠⣦⡈⠀⠀⡀⠀⠀⣄⣤⣴⡀⠀⠀⠀⠀⠀⠀⠀⢀⠐⠀⠀⠀⠹⣿⣻")
print ("⠀⠀⠠⠀⠀⠀⠀⠠⠦⠀⣀⡤⣴⡆⢼⣿⣿⣿⠁⠡⢥⣨⣿⣳⣢⣔⣤⣩⣤⣦⣰⣬⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⠀⢈⢷⣻")
print ("⠀⠀⠀⠀⢠⣇⢫⣺⣖⣖⣯⣾⣿⠃⢸⣿⣿⣿⣦⠐⡈⢄⢵⣿⣿⣿⣿⣿⣷⣟⣿⣿⣿⣿⡏⡨⠁⠀⠀⠀⠀⠀⠀⢠⣿⠂⠀⢰⢧⣻")
print ("⠀⠀⠀⠀⢘⣿⣦⣾⣿⣿⣿⣝⠯⡄⣹⣿⣿⣿⣷⡛⠲⣤⣱⣻⠿⢿⣿⣿⣿⣿⣿⣿⣿⡧⠐⠀⠄⠀⠀⠀⠀⠀⠀⠀⣻⡅⠀⣞⢣⡷")
print ("⠀⠀⠀⠀⢸⣿⣿⣿⡿⠿⢏⣱⡆⡸⣿⣿⣿⣿⣿⣷⣆⡸⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⡱⠀⡀⠀⠀⠀⠀⠀⠀⠀⢰⣹⡇⠀⣏⢇⣿")
print ("⠀⠀⠀⠀⠈⢻⡱⢷⣴⣾⣿⣿⢻⠄⠙⠿⠟⠁⠀⠙⠛⠃⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠉⡄⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠁⢠⡟⢬⢻")
print ("⠀⠀⠀⠀⠀⠠⡑⢿⣿⣿⣿⣿⣆⠀⢀⡀⠀⠀⣀⣤⣀⣠⣴⣿⣿⣿⣿⣿⣿⢿⣻⣷⣦⣜⢂⠐⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠶⡸⢌⣳")
print ("⠀⠀⠀⠀⠀⠀⡘⢼⣿⣿⣿⣿⣷⣷⡏⣷⣤⣾⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡚⠽⣿⣿⠏⠞⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⢊⠰⣁⠲⣸")
print ("⠀⠀⠀⠀⠀⠀⢨⣙⣾⢿⣿⣿⣿⣿⣿⣿⣷⡽⠿⠿⣿⣿⣿⣿⣿⡯⡛⢿⣟⠈⡜⡙⢧⠉⠈⠀⠀⠀⠀⠀⠀⠀⢠⠐⠌⠂⠥⣀⠳⡜")
print ("⠀⠀⠀⠀⠀⠀⠐⡍⠃⡿⣹⣿⣿⡿⠋⠀⠠⠠⠐⠖⠀⠈⠙⠛⠛⠽⡏⠈⣿⡃⠐⡘⢪⠁⠀⠀⠀⠂⠀⠀⠀⠀⠢⠱⢌⠱⡒⢄⠳⣸")
print ("⠀⠀⠀⠀⠀⠀⠈⣷⡐⡏⣟⡿⠋⠁⠀⣀⣠⡄⣀⣤⣤⡤⠀⣀⣠⣤⣼⡆⣸⡧⡀⠀⢺⠂⠀⠀⠀⠀⠀⠀⠀⠠⢁⠣⢌⠢⠑⡌⢒⡡")
print ("⠀⠀⠀⠀⠀⠀⠀⢹⣇⣷⣼⣶⣶⣦⣂⡹⠟⠟⠛⠛⠑⠴⣭⢏⣭⢟⣿⣿⣶⡇⠀⠀⢢⠀⠀⠀⠀⠀⠀⠀⠀⢡⠈⠒⡄⢊⠡⠐⢢⠰")
print ("⠀⠀⠀⠀⠀⠀⠀⠈⣽⣿⣿⣿⣿⣿⣿⣿⣶⣤⣤⣴⣾⢿⣼⣦⢯⣳⡿⢿⠽⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠐⢀⠊⡐⢀⠢⠌⠡⢀⢣")
print ("⠀⠀⠀⠀⠀⠀⠀⠀⠘⢏⢻⣿⣷⣾⣽⣻⣭⣦⣶⣾⣿⣿⣾⣿⣾⣿⡛⠅⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠃⡀⠀⠂⡀⠂⡁⠀⢂")
print ("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢂⠸⠿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠡⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠊⠀⠁⠐⠀⠐⠀⠄⠂")
print ("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⢀⠩⢐⠹⠛⠻⠟⠻⠋⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠐⡀⠈⢀⠈⢀⠂⠄⠐")
print ("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣮⣿⠠⢐⠈⠄⡐⠠⢀⠈⠀")
print ("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣿⣿⣿⣧⣈⠜⡐⢄⠂⠄⢂⠈")
print ("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣶⣬⣜⣰⣄⢪")
print ("⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣷⣿⣿⣿⣿⣿⣿⣧⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢲⣻⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿")

print ("░██████╗░██╗░░░██╗░██████╗██████╗░██████╗░██╗███╗░░██╗░██████╗░")
print ("██╔════╝░██║░░░██║██╔════╝██╔══██╗██╔══██╗██║████╗░██║██╔════╝░")
print ("██║░░██╗░██║░░░██║╚█████╗░██████╔╝██████╔╝██║██╔██╗██║██║░░██╗░")
print ("██║░░╚██╗██║░░░██║░╚═══██╗██╔═══╝░██╔══██╗██║██║╚████║██║░░╚██╗")
print ("╚██████╔╝╚██████╔╝██████╔╝██║░░░░░██║░░██║██║██║░╚███║╚██████╔╝")
print ("░╚═════╝░░╚═════╝░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░")

time.sleep(1)

# Input manual
token = input("Masukkan Token Bot Discord: ").strip()
channel_ids_input = input("Masukkan ID Saluran Discord (pisahkan dengan koma): ").strip()
pesan_input = input("Masukkan pesan yang ingin Anda kirim: ").strip()
waktu_kirim = 86400  # 24 jam dalam detik
waktu_jeda = 5  # Jeda 5 detik antara pengiriman pesan

# Mengubah ID saluran menjadi integer
channel_ids = [int(cid.strip()) for cid in channel_ids_input.split(",")]
os.system('cls' if os.name == 'nt' else 'clear')
while True:
    for channel_id in channel_ids:
        payload = {
            'content': pesan_input  # Menggunakan pesan dari input manual
        }
        headers = {
            'Authorization': token
        }
        # Mengirim pesan
        r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
        if r.status_code == 200:
            print(Fore.WHITE + "Sent message: ")
            print(Fore.YELLOW + payload['content'])
        else:
            print(Fore.RED + f'Gagal mengirim pesan ke channel ID {channel_id}: {r.status_code}')
        # Jeda selama 5 detik sebelum mengirim pesan ke saluran berikutnya
        time.sleep(waktu_jeda)
    print(f"Menunggu selama {waktu_kirim} detik sebelum mengirim pesan lagi...")
    time.sleep(waktu_kirim)  # Tunggu selama 24 jam
