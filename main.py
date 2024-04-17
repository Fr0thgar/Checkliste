import tkinter as tk
import os

def show_selected():
    selected_items = [var.get() for var in checkboxes]
    file_path = os.path.join(os.getcwd(), "selected_items.txt")
    with open(file_path, "w") as f:
        f.write("Selected items:\n")
    print("Selected items have been saved to selected_items.txt")

# Create the main application window
root = tk.Tk()
root.title("Checkbox Example")

# Create some checkboxes
options = ["Option 1", "Option 2", "Option 3"]
checkboxes = []
for option in options:
    var = tk.IntVar()
    checkbox = tk.Checkbutton(root, text=option, variable=var)
    checkbox.pack(anchor=tk.W)
    checkboxes.append(var)

# Create a button to show selected checkboxes
show_button = tk.Button(root, text="Show Selected", command=show_selected)
show_button.pack()

# Start the GUI event loop
root.mainloop()
