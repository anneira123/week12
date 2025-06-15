import tkinter as tk

def tampilkan_teks():
    teks = entry.get()
    label_hasil.config(text=f"Anda mengetik: {teks}")

# Membuat window utama
root = tk.Tk()
root.title("Aplikasi Minimalis")
root.geometry("300x200")

# Frame untuk mengelompokkan widget
frame = tk.Frame(root)
frame.pack(pady=20)

# Label
label = tk.Label(frame, text="Masukkan sesuatu:")
label.pack()

# Entry (input teks)
entry = tk.Entry(frame, width=25)
entry.pack(pady=5)

# Button
tombol = tk.Button(frame, text="Tampilkan", command=tampilkan_teks)
tombol.pack(pady=5)

# Label untuk menampilkan hasil
label_hasil = tk.Label(frame, text="")
label_hasil.pack()

# Canvas sederhana
canvas = tk.Canvas(root, width=200, height=50, bg="#f0f0f0")
canvas.pack()
canvas.create_rectangle(10, 10, 50, 40, fill="blue")

# Text widget kecil
text = tk.Text(root, height=3, width=25)
text.pack(pady=5)
text.insert(tk.END, "Ini contoh Text widget")

root.mainloop()