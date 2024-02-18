import sqlite3 
import tkinter as tk
from tkinter import messagebox 
from tkinter import ttk

def tambah_data():
    nama = entry_list[0].get()
    nama_kampus = entry_list[1].get()
    prodi = entry_list[2].get()
    semester = entry_list[3].get()

    conn = sqlite3.connect('kompetisi.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS DataKompetisi (
                   Nama TEXT,
                   NamaUniversitas TEXT,
                   Prodi TEXT,
                   Semester TEXT
                )''')

    cursor.execute("INSERT INTO DataKompetisi VALUES (?, ?, ?, ?)",
                    (nama, nama_kampus, prodi, semester))

    conn.commit()
    conn.close()

    for entry in entry_list:
        entry.delete(0, 'end')
    
    messagebox.showinfo("Info", "Terimakasih telah mendaftar kompetisi ini")

def tampilkan_data():
    conn = sqlite3.connect('kompetisi.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM DataKompetisi")
    rows = cursor.fetchall()

    conn.commit()
    conn.close()

    # Bersihkan data sebelum menampilkan yang baru
    for row in tree.get_children():
        tree.delete(row)

    # Tampilkan data dari database ke Treeview
    for row in rows:
        tree.insert("", "end", values=row)

root = tk.Tk()
root.title("Input dan Tampilan Data Kompetisi")

labels = ['Nama: ', 'Nama Universitas: ', 'Prodi: ', 'Semester: ']
entry_list = []

for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0)

    entry = tk.Entry(root)
    entry.grid(row=i, column=1)

    entry_list.append(entry)

button_submit = tk.Button(root, text="Submit", command=tambah_data)
button_submit.grid(row=len(labels), column=0, columnspan=2)

button_tampilkan = tk.Button(root, text="Tampilkan Data", command=tampilkan_data)
button_tampilkan.grid(row=len(labels) + 1, column=0, columnspan=2)

tree = ttk.Treeview(root, columns=('Nama', 'Nama Universitas', 'Prodi', 'Semester'), show='headings')
tree.heading('Nama', text='Nama')
tree.heading('Nama Universitas', text='Nama Universitas')
tree.heading('Prodi', text='Prodi')
tree.heading('Semester', text='Semester')
tree.grid(row=len(labels) + 4, column=0, columnspan=2)

root.mainloop()
