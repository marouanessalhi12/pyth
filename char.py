import mysql.connector
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk

def charg():
    # Connect to the MySQL database
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="coti"
    )


    

    # Create a cursor object to interact with the database
    mycursor = mydb.cursor()

    # Define a function to handle the "Add charge" button click
    def add_charge():
        # Get the values from the entry widgets
        date = date_entry.get()
        libelle = libelle_entry.get()
        somme = somme_entry.get()
        


        # Insert the charge into the database
        sql = "INSERT INTO charges (date, libelle, somme) VALUES (%s, %s, %s)"
        val = (date, libelle, somme)
        mycursor.execute(sql, val)
        mydb.commit()

        # Clear the entry widgets
        date_entry.delete(0, tk.END)
        libelle_entry.delete(0, tk.END)
        somme_entry.delete(0, tk.END)
        

        # Refresh the charges list
        refresh_charges()
    
    # Define a function to handle the "Update charge" button click
    # Define a function to handle the "Update charge" button click
    # Define a function to handle the "Update charge" button click
    def update_charges():
        # Get the selected charge from the treeview
        selected_item = charges_treeview.selection()
        if len(selected_item) == 0:
            return
        charge_id = charges_treeview.item(selected_item[0], "text")

        # Retrieve the selected charge from the database
        sql = "SELECT * FROM charges WHERE id = %s"
        val = (charge_id,)
        mycursor.execute(sql, val)
        charge = mycursor.fetchone()

        # Create a new window for updating the charge
        global update_window
        update_window = tk.Toplevel(roote)

        update_window.title("Update charge")

        # Create the label and entry widgets for the charge details
        

        # Create label for date input
        date_label = ttk.Label(update_window, text="Date (YYYY-MM-DD):")
        date_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        # Create entry widget for date input
        date_entry = ttk.Entry(update_window, width=30)
        date_entry.grid(row=0, column=1, padx=5, pady=5)
        date_entry.insert(0, charge[1])  # Set default date format in the entry widget

        libelle_label = ttk.Label(update_window, text="Libelle")
        libelle_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        libelle_entry = ttk.Entry(update_window, width=30)
        libelle_entry.grid(row=1, column=1, padx=5, pady=5)
        libelle_entry.insert(0, charge[2])

        somme_label = ttk.Label(update_window, text="Somme:")
        somme_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        somme_entry = ttk.Entry(update_window, width=30)
        somme_entry.grid(row=2, column=1, padx=5, pady=5)
        somme_entry.insert(0, charge[3])


        # Create the "Update" button
        update_button = ttk.Button(update_window, text="Modifier", command=lambda: update_charge_db(charge_id, date_entry.get(), libelle_entry.get(), somme_entry.get()))
        update_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        


    # Define a function to update the charge in the database
    def update_charge_db(charge_id, date, libelle, somme):
        # Update the charge in the database
        sql = "UPDATE charges SET date = %s, libelle = %s, somme = %s WHERE id = %s"
        val = (date, libelle, somme, charge_id)
        mycursor.execute(sql, val)
        mydb.commit()

        # Close the update window
        update_window.destroy()

        # Refresh the charges list
        refresh_charges()

    # Define a function to handle the "Delete charge" button click
    def delete_charge():
        # Get the selected charge from the treeview
        selected_item = charges_treeview.selection()
        if len(selected_item) == 0:
            return
        charge_id = charges_treeview.item(selected_item[0], "text")

        # Delete the charge from the database
        sql = "DELETE FROM charges WHERE id = %s"
        val = (charge_id,)
        mycursor.execute(sql, val)
        mydb.commit()

        # Clear the entry widgets
        date_entry.delete(0, tk.END)
        libelle_entry.delete(0, tk.END)
        somme_entry.delete(0, tk.END)
        

        # Refresh the charges list
        refresh_charges()

    # Define a function to refresh the charges list
    def refresh_charges():
        # Clear the treeview
        for item in charges_treeview.get_children():
            charges_treeview.delete(item)

        # Retrieve the charges from the database
        sql = "SELECT * FROM charges ORDER BY date"
        mycursor.execute(sql)
        charges = mycursor.fetchall()

        # Insert the charges into the treeview
        for charge in charges:
            charges_treeview.insert("", tk.END, text=charge[0], values=(charge[1], charge[2], charge[3]))



    def total_charges():
        

        # Create a cursor
        cursor = mydb.cursor()

        # Execute the query to get the sum of charges
        query = "SELECT SUM(somme) FROM charges"
        cursor.execute(query)

        # Get the result of the query
        result = cursor.fetchone()




        # Display the sum of charges in a message box
        messagebox.showinfo("Totale des charges", f"Le totale des charges est:  {result[0]}")


    
    # Create the main window
    roote = tk.Tk()
    roote.title("charge Tracker")
    roote.geometry(f"{roote.winfo_screenwidth()}x1000")  # Set the width of the window to the width of the device


    # Create the label and entry widgets for the charge details
    # Create label for date input
    date_label = ttk.Label(roote, text="Date (YYYY-MM-DD):")
    date_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    # Create entry widget for date input
    date_entry = ttk.Entry(roote, width=30)
    date_entry.grid(row=0, column=1, padx=5, pady=5)
    date_entry.insert(0, "YYYY-MM-DD")  # Set default date format in the entry widget

    libelle_label = ttk.Label(roote, text="Libelle:")
    libelle_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    libelle_entry = ttk.Entry(roote, width=30)
    libelle_entry.grid(row=1, column=1, padx=5, pady=5)

    somme_label = ttk.Label(roote, text="Somme:")
    somme_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    somme_entry = ttk.Entry(roote, width=30)
    somme_entry.grid(row=2, column=1, padx=5, pady=5)

    

    


    # Create the treeview to display the charges
    charges_treeview = ttk.Treeview(roote, columns=("date", "libelle", "somme"), show="headings")
    charges_treeview.heading("date", text="Date")
    charges_treeview.heading("libelle", text="Libelle")
    charges_treeview.heading("somme", text="Somme")
    
    charges_treeview.grid(row=3, column=0, columnspan=2, padx=7, pady=5)

    # Create the buttons to add, update, and delete charges
    add_button = ttk.Button(roote, text="Ajpouter une charge", command=add_charge)
    add_button.grid(row=4, column=0, padx=5, pady=5)

    update_button = ttk.Button(roote, text="Modifier une charge", command=update_charges)
    update_button.grid(row=4, column=1, padx=5, pady=5)

    delete_button = ttk.Button(roote, text="Supprimer une charge", command=delete_charge)
    delete_button.grid(row=4, column=2, padx=5, pady=5)




    # Create the button for total charges
    total_button = ttk.Button(roote, text="Totale des charges", command=total_charges)
    total_button.grid(row=4, column=3, padx=5, pady=5)



    # Refresh the charges list on startup
    refresh_charges()

    # Start the main event loop
    roote.mainloop()
