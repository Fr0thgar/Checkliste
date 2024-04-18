import tkinter as tk
import os
from datetime import datetime

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
         entry.delete(0, tk.END)
    name_var.set("")

# Create the main application window
root = tk.Tk()
root.title("Checkbox Example")

#Create a label for the name input
name_label = tk.Label(root, text="Employee name:")
name_label.pack()

#Create a textbox for name input
name_var = tk.StringVar()
name_entry = tk.Entry(root, textvariable=name_var)
name_entry.pack()

# Create some checkboxes
options = ["Computer", "Mobil", "Headset", "Nøgle Brik", 
           "Oplader", "Taske", "Andet"]
checkboxes = []
entries = []
for option in options:
    var = tk.IntVar()
    checkbox = tk.Checkbutton(root, text=option, variable=var)
    checkbox.pack(anchor=tk.W)
    checkboxes.append(var)
    entry = tk.Entry(root)
    entry.pack()
    entries.append(entry)

# Create a button to submit selected checkboxes
show_button = tk.Button(root, text="Submit", command=show_selected)
show_button.pack()

# Start the GUI event loop
root.mainloop()
