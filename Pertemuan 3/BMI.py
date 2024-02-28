import tkinter as tk

def calculate_bmi():
    height = float(height_entry.get()) / 100  # Konversi tinggi dari cm ke m
    weight = float(weight_entry.get())

    bmi = weight / (height ** 2)

    result_label.config(text="BMI: {:.2f}".format(bmi))

    if bmi < 18.5:
        category_label.config(text="Kategori: Kurus")
    elif 18.5 <= bmi < 24.9:
        category_label.config(text="Kategori: Normal")
    elif bmi >= 24.9:
        category_label.config(text="Kategori: Obesitas")

# Membuat GUI
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("250x250")

# Label dan Entry untuk tinggi
height_label = tk.Label(root, text="Tinggi (cm):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

# Label dan Entry untuk berat badan
weight_label = tk.Label(root, text="Berat (kg):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

# Tombol untuk menghitung BMI
calculate_button = tk.Button(root, text="Hitung BMI", command=calculate_bmi)
calculate_button.pack()

# Label untuk menampilkan hasil BMI
result_label = tk.Label(root, text="")
result_label.pack()

# Label untuk menampilkan kategori BMI
category_label = tk.Label(root, text="")
category_label.pack()

root.mainloop()