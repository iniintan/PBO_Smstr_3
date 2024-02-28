from googletrans import Translator

def translate_text():
    # Inisialisasi objek Translator
    translator = Translator()

    # Mengambil input teks dan bahasa asal
    text = input("Masukkan teks yang ingin diterjemahkan: ")
    source_lang = input("Masukkan kode bahasa asal (contoh: 'en' untuk bahasa Inggris): ")

    # Mendeteksi bahasa asal jika kode bahasa tidak disediakan
    if not source_lang:
        try:
            source_lang = translator.detect(text).lang
        except Exception as e:
            print("Gagal mendeteksi bahasa asal:", e)
            return

    # Memilih bahasa tujuan
    target_lang = input("Masukkan kode bahasa tujuan (contoh: 'id' untuk bahasa Indonesia): ")

    # Melakukan terjemahan
    translated_text = translator.translate(text, src=source_lang, dest=target_lang)

    # Menampilkan hasil terjemahan
    print(f"Hasil Terjemahan dari {translated_text.src} ke {translated_text.dest}:")
    print(translated_text.text)

if __name__ == "__main__":
    translate_text()