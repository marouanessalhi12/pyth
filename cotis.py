import mysql.connector
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import simpledialog, messagebox
from tkinter import ttk

def coti():
    # Connect to the MySQL database
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="coti"
    )


    

    # Create a cursor object to interact with the database
    mycursor = mydb.cursor()

    # Define a function to handle the "Add Contribution" button click
    def add_contribution():
        # Get the values from the entry widgets
        name = name_entry.get()
        apartment_number = apartment_entry.get()
        month = month_entry.get()
        contribution_amount = contribution_entry.get()
        year = year_combo.get()


        # Insert the contribution into the database
        sql = "INSERT INTO contributions (name, apartment_number, month, contribution_amount, year) VALUES (%s, %s, %s, %s, %s)"
        val = (name, apartment_number, month, contribution_amount, year)
        mycursor.execute(sql, val)
        mydb.commit()

        # Clear the entry widgets
        name_entry.delete(0, tk.END)
        apartment_entry.delete(0, tk.END)
        month_entry.delete(0, tk.END)
        contribution_entry.delete(0, tk.END)
        year_combo.set("")

        # Refresh the contributions list
        refresh_contributions()

    # Define a function to handle the "Update Contribution" button click
    # Define a function to handle the "Update Contribution" button click
    # Define a function to handle the "Update Contribution" button click
    def update_contribution():
        # Get the selected contribution from the treeview
        selected_item = contributions_treeview.selection()
        if len(selected_item) == 0:
            return
        contribution_id = contributions_treeview.item(selected_item[0], "text")

        # Retrieve the selected contribution from the database
        sql = "SELECT * FROM contributions WHERE id = %s"
        val = (contribution_id,)
        mycursor.execute(sql, val)
        contribution = mycursor.fetchone()

        # Create a new window for updating the contribution
        global update_window
        update_window = tk.Toplevel(roote)

        update_window.title("Update Contribution")

        # Create the label and entry widgets for the contribution details
        

        name_label = ttk.Label(update_window, text="Name:")
        name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        name_entry = ttk.Entry(update_window, width=30)
        name_entry.grid(row=0, column=1, padx=5, pady=5)
        name_entry.insert(0, contribution[1])

        apartment_label = ttk.Label(update_window, text="Apartment Number:")
        apartment_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        apartment_entry = ttk.Entry(update_window, width=30)
        apartment_entry.grid(row=1, column=1, padx=5, pady=5)
        apartment_entry.insert(0, contribution[2])

        month_label = ttk.Label(update_window, text="Month:")
        month_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        month_entry = ttk.Entry(update_window, width=30)
        month_entry.grid(row=2, column=1, padx=5, pady=5)
        month_entry.insert(0, contribution[3])

        contribution_label = ttk.Label(update_window, text="Contribution Amount:")
        contribution_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        contribution_entry = ttk.Entry(update_window, width=30)
        contribution_entry.grid(row=3, column=1, padx=5, pady=5)
        contribution_entry.insert(0, contribution[4])

        year_label = ttk.Label(update_window, text="Year:")
        year_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        year_combo = ttk.Combobox(update_window, values=[str(year) for year in range(2018, 2041)], width=30)
        year_combo.grid(row=4, column=1, padx=5, pady=5)
        year_combo.set(contribution[5])


        # Create the "Update" button
        update_button = ttk.Button(update_window, text="Update", command=lambda: update_contribution_db(contribution_id, name_entry.get(), apartment_entry.get(), month_entry.get(), contribution_entry.get(), year_combo.get()))
        update_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        


    # Define a function to update the contribution in the database
    def update_contribution_db(contribution_id, name, apartment_number, month, contribution_amount, year):
        # Update the contribution in the database
        sql = "UPDATE contributions SET name = %s, apartment_number = %s, month = %s, contribution_amount = %s, year = %s WHERE id = %s"
        val = (name, apartment_number, month, contribution_amount, year, contribution_id)
        mycursor.execute(sql, val)
        mydb.commit()

        # Close the update window
        update_window.destroy()

        # Refresh the contributions list
        refresh_contributions()

    # Define a function to handle the "Delete Contribution" button click
    def delete_contribution():
        # Get the selected contribution from the treeview
        selected_item = contributions_treeview.selection()
        if len(selected_item) == 0:
            return
        contribution_id = contributions_treeview.item(selected_item[0], "text")

        # Delete the contribution from the database
        sql = "DELETE FROM contributions WHERE id = %s"
        val = (contribution_id,)
        mycursor.execute(sql, val)
        mydb.commit()

        # Clear the entry widgets
        name_entry.delete(0, tk.END)
        apartment_entry.delete(0, tk.END)
        month_entry.delete(0, tk.END)
        contribution_entry.delete(0, tk.END)
        year_combo.delete(0, tk.END)

        # Refresh the contributions list
        refresh_contributions()

    # Define a function to refresh the contributions list
    def refresh_contributions():
        # Clear the treeview
        for item in contributions_treeview.get_children():
            contributions_treeview.delete(item)

        # Retrieve the contributions from the database
        sql = "SELECT * FROM contributions ORDER BY year"
        mycursor.execute(sql)
        contributions = mycursor.fetchall()

        # Insert the contributions into the treeview
        for contribution in contributions:
            contributions_treeview.insert("", tk.END, text=contribution[0], values=(contribution[1], contribution[2], contribution[3], contribution[4], contribution[5]))



    def calculate_total(year):
        # Create a cursor
        cursor = mydb.cursor()

        # Execute the query to get the sum of contributions for the given year
        query = f"SELECT SUM(contribution_amount) FROM contributions WHERE year = {year}"
        cursor.execute(query)

        # Get the result of the query
        result = cursor.fetchone()

        # Display the sum of contributions for the given year in a message box
        messagebox.showinfo("Total Contributions", f"The total contributions amount for {year} is {result[0]}")

    def total_contributions():
        # Get the year from user using a simple dialog box
        year = simpledialog.askinteger("Enter Year", "Enter the year you want to calculate the total for:")

        # Create a window to show the result
        result_window = tk.Toplevel()
        result_window.title("Total Contributions")

        # Create a label to display the result
        result_label = tk.Label(result_window, text=f"The total contributions amount for {year} is:")
        result_label.pack()

        # Create a button to calculate the total contributions
        calculate_button = tk.Button(result_window, text="Calculate", command=lambda: calculate_total(year))
        calculate_button.pack()

        # Show the result window
        result_window.mainloop()




    # Create the main window
    roote = tk.Tk()
    roote.title("Contribution Tracker")

    # Create the label and entry widgets for the contribution details
    name_label = ttk.Label(roote, text="Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    name_entry = ttk.Entry(roote, width=30)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    apartment_label = ttk.Label(roote, text="Apartment Number:")
    apartment_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    apartment_entry = ttk.Entry(roote, width=30)
    apartment_entry.grid(row=1, column=1, padx=5, pady=5)

    month_label = ttk.Label(roote, text="Month:")
    month_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    month_entry = ttk.Combobox(roote, width=27, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    month_entry.grid(row=2, column=1, padx=5, pady=5)

    contribution_label = ttk.Label(roote, text="Contribution Amount:")
    contribution_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    contribution_entry = ttk.Entry(roote, width=30)
    contribution_entry.grid(row=3, column=1, padx=5, pady=5)

    year_label = ttk.Label(roote, text="Year:")
    year_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

    year_combo = ttk.Combobox(roote, values=[str(year) for year in range(2018, 2041)], width=27)
    year_combo.grid(row=4, column=1, padx=5, pady=5)


    # Create the treeview to display the contributions
    contributions_treeview = ttk.Treeview(roote, columns=("name", "apartment_number", "month", "contribution_amount", "year"), show="headings")
    contributions_treeview.heading("name", text="Name")
    contributions_treeview.heading("apartment_number", text="Apartment Number")
    contributions_treeview.heading("month", text="Month")
    contributions_treeview.heading("contribution_amount", text="Contribution Amount")
    contributions_treeview.heading("year", text="Year")
    contributions_treeview.grid(row=5, column=0, columnspan=2, padx=7, pady=5)

    # Create the buttons to add, update, and delete contributions
    add_button = ttk.Button(roote, text="Add Contribution", command=add_contribution)
    add_button.grid(row=6, column=0, padx=5, pady=5)

    update_button = ttk.Button(roote, text="Update Contribution", command=update_contribution)
    update_button.grid(row=6, column=1, padx=5, pady=5)

    delete_button = ttk.Button(roote, text="Delete Contribution", command=delete_contribution)
    delete_button.grid(row=6, column=2, padx=5, pady=5)




    # Create the button for total contributions
    total_button = ttk.Button(roote, text="Total Contributions", command=total_contributions)
    total_button.grid(row=6, column=3, padx=5, pady=5)



    # Refresh the contributions list on startup
    refresh_contributions()

    # Start the main event loop
    roote.mainloop()