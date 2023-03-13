import mysql.connector
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import simpledialog, messagebox
from tkinter import ttk

def cal():
    # Connect to the MySQL database
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="coti"
    )


    
    
    
    year = simpledialog.askstring("Input", "Enter the year:")
    cursor = mydb.cursor()



    # Use parameterized query to avoid SQL injection
    cursor.execute("SELECT SUM(contribution_amount) FROM contributions WHERE year=%s", (year,))
    contributions_total = cursor.fetchone()[0]
    if contributions_total is None:
        contributions_total = 0

    # Use parameterized query to avoid SQL injection
    cursor.execute("SELECT SUM(somme) FROM charges WHERE date LIKE %s", (f"{year}-%-%",))
    charges_total = cursor.fetchone()[0]
    if charges_total is None:
        charges_total = 0

    result = float(contributions_total) - float(charges_total)

     # hide the window before showing the message box
    messagebox.showinfo(title="Result", message=f"The result is {result}")
    
    
    mydb.close()




    