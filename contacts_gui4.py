import tkinter as tk
from tkinter import messagebox
import json

contacts = []

def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    
    if name and phone:
        contacts.append({"name": name, "phone": phone})
        save_contacts()
        update_contact_list()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Nama dan Nomor Telepon harus diisi.")

def delete_contact():
    selected = contact_listbox.curselection()
    if selected:
        idx = selected[0]
        del contacts[idx]
        save_contacts()
        update_contact_list()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Selection Error", "Pilih kontak yang ingin dihapus.")

def edit_contact():
    selected = contact_listbox.curselection()
    if selected:
        idx = selected[0]
        new_name = name_entry.get()
        new_phone = phone_entry.get()
        
        if new_name and new_phone:
            contacts[idx] = {"name": new_name, "phone": new_phone}
            save_contacts()
            update_contact_list()
            name_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Nama dan Nomor Telepon harus diisi.")
    else:
        messagebox.showwarning("Selection Error", "Pilih kontak yang ingin diedit.")

def populate_fields(event):
    selected = contact_listbox.curselection()
    if selected:
        idx = selected[0]
        contact = contacts[idx]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, contact["name"])
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, contact["phone"])

def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Setup GUI
root = tk.Tk()
root.title("Buku Kontak")

# Frame untuk Daftar Kontak
list_frame = tk.Frame(root, bg="pink")  # Ubah background menjadi pink
list_frame.pack(pady=10)

contact_listbox = tk.Listbox(list_frame, width=50, height=10, bg="pink", font=("Times New Roman", 12))  # Ubah font dan ukuran font
contact_listbox.pack(side=tk.LEFT, padx=10)
scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
scrollbar.config(command=contact_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
contact_listbox.config(yscrollcommand=scrollbar.set)
contact_listbox.bind('<<ListboxSelect>>', populate_fields)  # Tambahkan bind untuk menampilkan detail kontak yang dipilih

# Frame untuk Form Input
input_frame = tk.Frame(root, bg="pink")  # Ubah background menjadi pink
input_frame.pack(pady=10)

tk.Label(input_frame, text="Nama", font=("Times New Roman", 12)).grid(row=0, column=0, padx=10, pady=5)  # Ubah font dan ukuran font
name_entry = tk.Entry(input_frame, font=("Times New Roman", 12))  # Ubah font dan ukuran font
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Nomor Telepon", font=("Times New Roman", 12)).grid(row=1, column=0, padx=10, pady=5)  # Ubah font dan ukuran font
phone_entry = tk.Entry(input_frame, font=("Times New Roman", 12))  # Ubah font dan ukuran font
phone_entry.grid(row=1, column=1, padx=10, pady=5)

# Frame untuk Tombol
button_frame = tk.Frame(root, bg="pink")  # Ubah background menjadi pink
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Tambah Kontak", command=add_contact, font=("Times New Roman", 12))  # Ubah font dan ukuran font
add_button.grid(row=0, column=0, padx=10)

edit_button = tk.Button(button_frame, text="Edit Kontak", command=edit_contact, font=("Times New Roman", 12))  # Ubah font dan ukuran font
edit_button.grid(row=0, column=1, padx=10)

delete_button = tk.Button(button_frame, text="Hapus Kontak", command=delete_contact, font=("Times New Roman", 12))  # Ubah font dan ukuran font
delete_button.grid(row=0, column=2, padx=10)

# Load contacts and update list
load_contacts()
update_contact_list()

root.mainloop()