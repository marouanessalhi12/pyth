import tkinter as tk
from cotis import coti
from char import charg
from calcul import cal

# Create the main window
root = tk.Tk()
root.title("Main Window")
root.geometry(f"{root.winfo_screenwidth()}x1000")  # Set the width of the window to the width of the device

# Define the style for the buttons
style = tk.ttk.Style()
style.configure("TButton", font=("Helvetica", 20), padding=10)

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack(expand=True)

# Create the first button
button1 = tk.ttk.Button(button_frame, text="Contributions", command=lambda: [root.withdraw(), coti()])
button1.pack(side=tk.LEFT, padx=10, pady=10)

# Create the second button
button2 = tk.ttk.Button(button_frame, text="Charges", command=lambda: [root.withdraw(), charg()])
button2.pack(side=tk.LEFT, padx=10, pady=10)

button2 = tk.ttk.Button(button_frame, text="Calculate", command=lambda: [root.withdraw(), cal()])
button2.pack(side=tk.LEFT, padx=10, pady=10)

# Center the frame vertically and horizontally
button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Start the main event loop
root.mainloop()
