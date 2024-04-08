import tkinter as tk

contacts = []

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        update_contact_list()

def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    search_text = entry_search.get()
    if search_text:
        search_results = [contact for contact in contacts if search_text.lower() in contact['name'].lower() or search_text in contact['phone']]
        contact_list.delete(0, tk.END)
        for contact in search_results:
            contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def delete_contact():
    try:
        index = contact_list.curselection()[0]
        del contacts[index]
        update_contact_list()
    except IndexError:
        pass

root = tk.Tk()
root.title("Contact Information Management System")

tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Phone:").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Address:").pack()
entry_address = tk.Entry(root)
entry_address.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack()

tk.Label(root, text="Search:").pack()
entry_search = tk.Entry(root)
entry_search.pack()

tk.Button(root, text="Search", command=search_contact).pack()

tk.Label(root, text="Contacts:").pack()
contact_list = tk.Listbox(root)
contact_list.pack()

tk.Button(root, text="Delete Contact", command=delete_contact).pack()

update_contact_list()

root.mainloop()