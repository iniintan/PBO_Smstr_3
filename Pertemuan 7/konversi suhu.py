from colorama import Fore, Back, Style, init

# Inisialisasi Colorama
init(autoreset=True)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print(Back.CYAN + Fore.BLACK + "Selamat Datang di Aplikasi Konversi Suhu" + Style.RESET_ALL)
    print(Fore.YELLOW + "Pilih jenis konversi suhu:")
    print("1. Celsius ke Fahrenheit")
    print("2. Fahrenheit ke Celsius")
    choice = input("Masukkan pilihan (1/2): ")

    if choice == '1':
        celsius_input = float(input("Masukkan suhu dalam Celsius: "))
        fahrenheit_output = celsius_to_fahrenheit(celsius_input)
        print(Fore.GREEN + f"{celsius_input} derajat Celsius sama dengan {fahrenheit_output} derajat Fahrenheit")
    elif choice == '2':
        fahrenheit_input = float(input("Masukkan suhu dalam Fahrenheit: "))
        celsius_output = fahrenheit_to_celsius(fahrenheit_input)
        print(Fore.GREEN + f"{fahrenheit_input} derajat Fahrenheit sama dengan {celsius_output} derajat Celsius")
    else:
        print(Fore.RED + "Pilihan tidak valid")

if __name__ == "_main_":
    main