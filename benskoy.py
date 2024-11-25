import subprocess
import sys

# Banner
banner = """
==================================================================  
//  ██████╗|███████╗███╗|||██╗███████╗██╗||██╗|██████╗|██╗|||██╗
//  ██╔══██╗██╔════╝████╗||██║██╔════╝██║|██╔╝██╔═══██╗╚██╗|██╔╝
//  ██████╔╝█████╗||██╔██╗|██║███████╗█████╔╝|██║|||██║|╚████╔╝|
//  ██╔══██╗██╔══╝||██║╚██╗██║╚════██║██╔═██╗|██║|||██║||╚██╔╝||
//  ██████╔╝███████╗██║|╚████║███████║██║||██╗╚██████╔╝|||██║|||
//  ╚═════╝|╚══════╝╚═╝||╚═══╝╚══════╝╚═╝||╚═╝|╚═════╝||||╚═╝|||
//  ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
_________________________EDITED BY BENSKOY________________________  
==================================================================
"""

# Menampilkan banner
print(banner)

def install_requirements():
    try:
        # Menjalankan perintah pip3 install -r requirements.txt
        print("Memulai instalasi keperluan...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Instalasi selesai.")
    except subprocess.CalledProcessError as e:
        print(f"Terjadi kesalahan saat instalasi: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def input_token():
    try:
        print("Mengedit file 'config.json'...")
        subprocess.check_call(["nano", "config.json"])
    except Exception as e:
        print(f"Terjadi kesalahan saat membuka 'config.json': {e}")

def input_proxy():
    try:
        print("Mengedit file 'proxies.txt'...")
        subprocess.check_call(["nano", "proxies.txt"])
    except Exception as e:
        print(f"Terjadi kesalahan saat membuka 'proxies.txt': {e}")

def run_script():
    try:
        print("Menjalankan skrip 'py'...")
        # Menjalankan skrip 'run-multi-bypass.py' dan menunggu sampai selesai
        subprocess.run([sys.executable, "main.py"])
        print("Skrip 'main.py' telah selesai dijalankan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menjalankan 'main.py': {e}")

def donate():
    print("Ton : UQAoNkeMz_aMlhUWTzgWITB6s6g68uosBpSFteBv2iDY_mjD")

def main_menu():
    while True:
        print("\n==== DI PILIH MASE ====")
        print("1. Install Keperluan (requirements)")
        print("2. Input config.json") #Input Akun
        print("3. Input Proxy") # Gak perlu
        print("4. Run")
        print("5. Donate")
        print("6. Cabut (Keluar)")
        
        choice = input("Pilih menu (1-100) HAHAHA: ")

        if choice == '1':
            install_requirements()
        elif choice == '2':
            input_token()
        elif choice == '3':
            input_proxy()
        elif choice == '4':
            run_script()
        elif choice == '5':
            donate()
        elif choice == '6':
            print("Keluar dari aplikasi...")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 dan 7.")

if __name__ == "__main__":
    main_menu()
