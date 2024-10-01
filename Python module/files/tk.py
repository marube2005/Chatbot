import tkinter as tk

# Create a Tk window.
root = tk.Tk()

# Define a function to handle the file selection.
def file_selection():
    # Use the askopenfilename() method to display the file dialog box.
    file_path = tk.filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    if file_path:
        # Display the selected file path in a label.
        label_file_path.config(text=f"Selected file: {file_path}")

# Create a label to display the selected file path.
label_file_path = tk.Label(root)

# Create a button to trigger the file selection.
button_browse = tk.Button(root, text="Browse", command=file_selection)

# Configure the label and button positions.
label_file_path.pack()
button_browse.pack(pady=(10, 0))

# Start the Tk event loop.
root.mainloop()