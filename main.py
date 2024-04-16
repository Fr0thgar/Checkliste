import tkinter as tk

def show_selected():
    selected_items = [var.get() for var in checkboxes]
    print("Selected items:", selected_items)

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
