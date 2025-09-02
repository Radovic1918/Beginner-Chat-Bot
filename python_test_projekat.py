import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

root = tk.Tk()
root.title("To-Do Lista")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Dodaj zadatak", command=add_task)
add_button.pack(pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

delete_button = tk.Button(root, text="Obriši izabrani zadatak", command=delete_task)
delete_button.pack(pady=5)

root.mainloop()