import os
import time

# Warna untuk styling teks
merah = '\033[31m'
magenta = '\033[35m'
reset = '\033[0m'

# Fungsi untuk membersihkan layar terminal
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Fungsi untuk menampilkan logo dengan format yang lebih rapih
def print_logo():
    logo = f""" {magenta}
⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⡅⡅⠄⠄⠄⠄⡉⠹⠄⡅⠄⠄⠄
⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀
⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿
⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿
⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉
⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇
⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿
⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⣿⣽⣿⣿⣿⣿⣵⣾
⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃
⠛⢿⣿⣿⣿⣦⠁⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄
⠄⠄⠉⠻⣿⣿⣿⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀
⣮⣥⠄⠄⠄⠛⢿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿
=====================================
\  AUTHOR = ANDHIKA ANGGA KURNIAWAN /
  \     KELAS  = X RPL 2          /
    \                           /
=========================================================================================================
    {reset}
"""
    print(logo)

# Menampilkan pesan informasi
def show_information():
    print(f"{merah}SCRIPT INI BUATAN ANDHIKA YANG BERTUJUAN UNTUK MERUSAKAN HP SESEORANG{reset}")
    print(f"{merah}MEREK HP YANG DAPAT DI RUSAK{reset}")
    print("iphone")
    print("android")
    print("=========================================================================================")

# Fungsi untuk simulasi serangan
def serang_attack():
    print(f"{merah}Siap meluncurkan serangan!{reset}")
    time.sleep(1)

    # Meminta input nomor target
    nomer = input(f"{magenta}Masukkan nomor target (tanpa spasi): {reset}")
    print(f"\n{merah}Target yang diserang: {nomer}{reset}")

    # Animasi loading serangan
    print(f"{magenta}Melakukan serangan pada {nomer}...")
    for i in range(10):
        print(f"{merah}Serangan ke-{i+1} ke {nomer} berhasil!{reset}")
        time.sleep(0.5)  # Delay 0.5 detik untuk efek loading
    print(f"{magenta}Serangan selesai!{reset}\n")

# Main code untuk menjalankan program
def main():
    clear_screen()
    print_logo()
    show_information()
    serang_attack()

# Program dijalankan hanya jika file ini dijalankan langsung
if __name__ == "__main__":
    main()
