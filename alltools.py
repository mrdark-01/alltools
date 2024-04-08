import time
import os
import colorama
from colorama import Fore, Style, Back
os.system('clear')
print(Style.BRIGHT, Fore.CYAN)
os.system('figlet All Tools Premium')
print(Style.BRIGHT, Fore.YELLOW)

while True:
    print(Style.BRIGHT, Back.RED, Fore.WHITE + "MASUKAN PERINTAH!" + Style.RESET_ALL)
    print()
    print(Style.BRIGHT, Fore.YELLOW + "1. Hack Facebook Target")
    print(Style.BRIGHT, Fore.YELLOW + "2. Hack WhatsApp OTP")
    print(Style.BRIGHT, Fore.YELLOW + "3. Hack Instagram")
    print(Style.BRIGHT, Fore.YELLOW + "4. Hack FreeFire Account")
    print(Style.BRIGHT, Fore.RED + "0. Buy Akses Premium")
    print()
    prank_choice = int(input(Fore.YELLOW + "Pilih Nomor : "))
    
    if prank_choice == 99:
        os.system('clear')
        os.system('figlet Ngepet')
        print()
        input_nomor = input('Masukkan nomor target : ')
        input_jumlah = int(input('Mau ngepet berapa kali : '))

        for _ in range(input_jumlah):
            print(Fore.RED + f"Berhasil ngepet nomor {input_nomor} sebanyak {input_jumlah} Kali")
            time.sleep(0.03)
        
        break  # Berhenti setelah perintah pertama selesai
        
    elif prank_choice == 1:
        os.system('clear')
        os.system('figlet Facebook')
        input_satelit = input('Masukkan ID Facebook Target: ')
        time.sleep(1)
        print(Fore.CYAN + "Proses, Mohon Tunggu...")
        time.sleep(10)
        time.sleep(3)
        print(Fore.GREEN + f"Anda Bukan Pengguna Premium !")
        print(Fore.RED + f"Gagal Mendapatkan Password..")
        break  # kode berhenti setelah perintah pertama selesai
        
    elif prank_choice == 2:
        os.system('clear')
        os.system('figlet WhatsApp')
        input_satelit = input('Masukkan Nomor Target: ')
        time.sleep(1)
        print(Fore.CYAN + "Sedang Mendapatkan Kode.....")
        time.sleep(10)
        time.sleep(3)
        print(Fore.GREEN + f"Anda Bukan Pengguna Premium !")
        print(Fore.RED + f"Gagal Mendapatkan Kode OTP..")
        break  # kode berhenti setelah perintah pertama selesai
        
    elif prank_choice == 3:
        os.system('clear')
        os.system('figlet Instagram')
        input_satelit = input('Masukkan @Username: ')
        time.sleep(1)
        print(Fore.CYAN + "Sedang Mendapatkan Password.....")
        time.sleep(10)
        time.sleep(3)
        print(Fore.GREEN + f"Anda Bukan Pengguna Premium !")
        print(Fore.RED + f"Gagal Mendapatkan Password..")
        break  # kode berhenti setelah perintah pertama selesai
        
    elif prank_choice == 4:
        print("Coming Soon ")
        break
      #selamat tinggal maksudnya 🗿
        
        
    elif prank_choice == 0:
        print("Buy Akses Premium? Chat Wa : 0852-1535-1487")
        break
      #selamat tinggal maksudnya 🗿

    else:
        print(Fore.RED + "Pilihan tidak valid.")