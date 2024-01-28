import tkinter as tk

from utilities.userDetails import load_user_details, save_user_details
# Import other necessary modules

def on_submit():
    # Function to handle submit event
    # You can call your existing functions here
    pass

# Create the main window
root = tk.Tk()
root.title("Vivian - Virtual Assistant")
# Set the size of the window
root.geometry("1280x900")

# Add widgets (labels, buttons, text inputs, etc.)
label = tk.Label(root, text="Welcome to Vivian, your virtual assistant!")
label.pack()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

# Start the Tkinter event loop
root.mainloop()
