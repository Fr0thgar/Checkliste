from tkinter import *
import customtkinter
import os
#import pymongo
from datetime import datetime

customtkinter.set_default_color_theme("./theme.json")

def show_selected():
    selected_items = [var.get() for var in checkboxes]
    selected_text = [entry.get() for entry in entries]
    name = name_var.get()
    selected_items.append(name)
    selected_items_dict = {
         option: text for option, 
         text in zip(options, selected_text) if selected_items[options.index(option)]}
    current_month = datetime.now().strftime("%B")
    current_date = datetime.now().strftime("%d")
    current_year = datetime.now().strftime("%Y")
    folder_path = os.path.join(os.getcwd(), current_year, current_month, current_date)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, name + ".txt")
    with open(file_path, "w") as f:
        f.write("Employee Name: " + name + "\n")
        f.write("Selected items:\n")
        for option, text in selected_items_dict.items():
                f.write(f"{option}: {text}\n")
    print("Selected items have been saved to " + name + ".txt")
    # Clear the checkmarks, text, and name input
    for var in checkboxes:
        var.set(0)
    for entry in entries:
         entry.delete(0, customtkinter.END)
    name_var.set("")

# Create the main application window
root = customtkinter.CTk()
root.title("Log Employee Equiptment")
root.geometry("500x500")

#Create a label for the name input
name_label = customtkinter.CTkLabel(root, text="Employee name:")
name_label.pack()

#Create a textbox for name input
name_var = customtkinter.StringVar()
name_entry = customtkinter.CTkEntry(root, textvariable=name_var)
name_entry.pack()

# Create some checkboxes
options = ["Computer", "Mobil", "Headset", "Nøgle Brik", 
           "Oplader", "Taske", "Andet"]
checkboxes = []
entries = []
for option in options:
    var = customtkinter.IntVar()
    checkbox = customtkinter.CTkCheckBox(root, text=option, variable=var)
    checkbox.pack(anchor=customtkinter.SW)
    checkboxes.append(var)
    entry = customtkinter.CTkEntry(root)
    entry.pack()
    entries.append(entry)

# Create a button to submit selected checkboxes
show_button = customtkinter.CTkButton(master = root, text="Submit", 
                                      command=show_selected)
show_button.pack()

# Start the GUI event loop
root.mainloop()

