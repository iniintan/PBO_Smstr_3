class TemperatureConverter:
    def __init__(self):
        pass

    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9


class Application:
    def __init__(self):
        self.converter = TemperatureConverter()

    def run(self):
        print("Selamat Datang di Aplikasi Konversi Suhu")
        while True:
            print("\nPilih jenis konversi suhu:")
            print("1. Celsius ke Fahrenheit")
            print("2. Fahrenheit ke Celsius")
            print("3. Keluar")

            choice = input("Masukkan pilihan (1/2/3): ")

            if choice == '1':
                celsius = float(input("Masukkan suhu dalam Celsius: "))
                fahrenheit = self.converter.celsius_to_fahrenheit(celsius)
                print(f"{celsius} derajat Celsius sama dengan {fahrenheit} derajat Fahrenheit")
            elif choice == '2':
                fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
                celsius = self.converter.fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit} derajat Fahrenheit sama dengan {celsius} derajat Celsius")
            elif choice == '3':
                print("Terima kasih telah menggunakan aplikasi konversi suhu.")
                break
            else:
                print("Pilihan tidak valid, silakan masukkan pilihan yang benar.")


if __name__ == "__main__":
    app = Application()
    app.run()