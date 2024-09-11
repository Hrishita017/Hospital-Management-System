import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import mysql.connector
from tkcalendar import DateEntry

def connect_to_db():
    return mysql.connector.connect(host='localhost', user='root', password='Samsan97', database='hospital')

def show_table(table_name, columns, query):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    db.close()
    
    table_window = tk.Toplevel(root)
    table_window.title(f"View {table_name}")
    table_window.configure(bg="#FAF0E6")  # Pastel color
    
    tk.Label(table_window, text=f"{table_name}", font=("Arial", 18, 'bold'), bg="#FAF0E6").pack(pady=10)
    
    tree = ttk.Treeview(table_window, columns=columns, show='headings')
    tree.pack(padx=10, pady=10)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    for row in data:
        tree.insert('', 'end', values=row)
        
        
def view_patients():
    columns = ['ID', 'NAME', 'AGE', 'GENDER', 'BLOOD_GROUP', 'CONTACT_NO', 'ROOM_NO']
    query = "SELECT * FROM patient_id"
    show_table("Patients", columns, query)

def view_doctors():
    columns = ['DOC_ID', 'NAME', 'DEPARTMENT', 'CONTACT_no']
    query = "SELECT * FROM doctor_id"
    show_table("Doctors", columns, query)
def view_appointments():
    columns = ['Name', 'Contact', 'doctor-id','Appointment date', 'appointment time']
    query = "SELECT * FROM appoint_id"
    show_table("Appointments", columns, query)

def view_doctors_availability():
    query = """
    SELECT NAME,DOC_ID,AVAILABILITY_TYPE
    FROM doctor_id
    """
    columns = ['Doctor Name', 'Doctor ID', 'Availability']
    show_table("Doctors Availability", columns, query)




def insert_patient():
    def submit():
        name = name_entry.get()
        age = age_entry.get()
        gender = gender_entry.get().upper()
        blood_group = blood_group_entry.get().upper()
        contact_no = contact_no_entry.get()
        room_no = room_no_entry.get()

        if len(contact_no) != 10:
            messagebox.showerror("Input Error", "Contact number must be 10 digits")
            return

        db = connect_to_db()
        cursor = db.cursor()
        query = "INSERT INTO patient_id (NAME, AGE, GENDER, BLOOD_GROUP, CONTACT_NO, ROOM_NO) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (name, age, gender, blood_group, contact_no, room_no)
        cursor.execute(query, values)
        db.commit()
        db.close()
        messagebox.showinfo("Success", "Patient record inserted successfully")
        insert_patient_window.destroy()

    insert_patient_window = tk.Toplevel(root)
    insert_patient_window.title("Insert Patient")
    insert_patient_window.configure(bg="#FAF0E6")  # Pastel color

    tk.Label(insert_patient_window, text="Insert New Patient", font=("Arial", 14), bg="#FAF0E6").pack(pady=10)
    tk.Label(insert_patient_window, text="Name:").pack(pady=5)
    name_entry = tk.Entry(insert_patient_window)
    name_entry.pack(pady=5)

    tk.Label(insert_patient_window, text="Age:").pack(pady=5)
    age_entry = tk.Entry(insert_patient_window)
    age_entry.pack(pady=5)

    tk.Label(insert_patient_window, text="Gender (M/F/Other):").pack(pady=5)
    gender_entry = tk.Entry(insert_patient_window)
    gender_entry.pack(pady=5)

    tk.Label(insert_patient_window, text="Blood Group:").pack(pady=5)
    blood_group_entry = tk.Entry(insert_patient_window)
    blood_group_entry.pack(pady=5)

    tk.Label(insert_patient_window, text="Contact Number:").pack(pady=5)
    contact_no_entry = tk.Entry(insert_patient_window)
    contact_no_entry.pack(pady=5)

    tk.Label(insert_patient_window, text="Room Number:").pack(pady=5)
    room_no_entry = tk.Entry(insert_patient_window)
    room_no_entry.pack(pady=5)

    tk.Button(insert_patient_window, text="Submit", command=submit).pack(pady=20)

def insert_doctor():
    def submit():
        name = name_entry.get()
        department = department_entry.get()
        contact_no = contact_no_entry.get()
        availability_type = availability_type_entry.get()

        if len(contact_no) != 10:
            messagebox.showerror("Input Error", "Contact number must be 10 digits")
            return

        db = connect_to_db()
        cursor = db.cursor()
        query = "INSERT INTO doctor_id (NAME, DEPARTMENT, CONTACT_no, AVAILABILITY_TYPE) VALUES (%s, %s, %s, %s)"
        values = (name, department, contact_no, availability_type)
        cursor.execute(query, values)
        db.commit()
        db.close()
        messagebox.showinfo("Success", "Doctor record inserted successfully")
        insert_doctor_window.destroy()

    insert_doctor_window = tk.Toplevel(root)
    insert_doctor_window.title("Insert Doctor")
    insert_doctor_window.configure(bg="#FAF0E6")  # Pastel color

    tk.Label(insert_doctor_window, text="Insert New Doctor", font=("Arial", 14), bg="#FAF0E6").pack(pady=10)
    tk.Label(insert_doctor_window, text="Name:").pack(pady=5)
    name_entry = tk.Entry(insert_doctor_window)
    name_entry.pack(pady=5)

    tk.Label(insert_doctor_window, text="Department:").pack(pady=5)
    department_entry = tk.Entry(insert_doctor_window)
    department_entry.pack(pady=5)

    tk.Label(insert_doctor_window, text="Contact Number:").pack(pady=5)
    contact_no_entry = tk.Entry(insert_doctor_window)
    contact_no_entry.pack(pady=5)

    tk.Label(insert_doctor_window, text="Availability Type:").pack(pady=5)
    availability_type_entry = tk.Entry(insert_doctor_window)
    availability_type_entry.pack(pady=5)

    tk.Button(insert_doctor_window, text="Submit", command=submit).pack(pady=20)


def delete_patient():
    def submit():
        patient_id = id_entry.get()
        db = connect_to_db()
        cursor = db.cursor()
        query = "DELETE FROM patient_id WHERE ID = %s"
        cursor.execute(query, (patient_id,))
        db.commit()
        db.close()
        messagebox.showinfo("Success", "Patient record deleted successfully")
        delete_patient_window.destroy()

    delete_patient_window = tk.Toplevel(root)
    delete_patient_window.title("Delete Patient")
    delete_patient_window.configure(bg="#FAF0E6")  # Pastel color

    tk.Label(delete_patient_window, text="Delete Patient Record", font=("Arial", 14), bg="#FAF0E6").pack(pady=10)
    tk.Label(delete_patient_window, text="Patient ID:").pack(pady=5)
    id_entry = tk.Entry(delete_patient_window)
    id_entry.pack(pady=5)

    tk.Button(delete_patient_window, text="Delete", command=submit).pack(pady=20)
def delete_doctor():
    def submit():
        doctor_id = id_entry.get()

        # Connect to the database
        db = connect_to_db()
        cursor = db.cursor()

        try:
            # First query: Delete the doctor record
            query = "DELETE FROM doctor_id WHERE DOC_ID = %s"
            cursor.execute(query, (doctor_id,))
            
            # Second query: Update the status in the appoint_id table
            query = "UPDATE appoint_id SET status = 'cancelled' WHERE DOC_ID = %s"
            cursor.execute(query, (doctor_id,))
            
            # Commit the changes to the database
            db.commit()
            
            # Success message
            messagebox.showinfo("Success", "Doctor record deleted and appointments updated successfully")

        except Exception as e:
            # In case of any errors, rollback the transaction
            db.rollback()
            messagebox.showerror("Error", f"An error occurred: {e}")
        
        finally:
            # Close the database connection after all operations
            cursor.close()
            db.close()

        # Close the delete doctor window
        delete_doctor_window.destroy()

    # Create a new window for deleting a doctor
    delete_doctor_window = tk.Toplevel(root)
    delete_doctor_window.title("Delete Doctor")
    delete_doctor_window.configure(bg="#FAF0E6")  # Pastel color

    # Add labels and input fields
    tk.Label(delete_doctor_window, text="Delete Doctor Record", font=("Arial", 14), bg="#FAF0E6").pack(pady=10)
    tk.Label(delete_doctor_window, text="Doctor ID:").pack(pady=5)
    id_entry = tk.Entry(delete_doctor_window)
    id_entry.pack(pady=5)

    # Add delete button
    tk.Button(delete_doctor_window, text="Delete", command=submit).pack(pady=20)


def update_patient():
    def submit():
        patient_id = id_entry.get()
        field = field_entry.get()
        new_value = value_entry.get()

        db = connect_to_db()
        cursor = db.cursor()
        query = f"UPDATE patient_id SET {field} = %s WHERE ID = %s"
        cursor.execute(query, (new_value, patient_id))
        db.commit()
        db.close()
        messagebox.showinfo("Success", "Patient record updated successfully")
        update_patient_window.destroy()

    update_patient_window = tk.Toplevel(root)
    update_patient_window.title("Update Patient")
    update_patient_window.configure(bg="#FAF0E6")  # Pastel color

    tk.Label(update_patient_window, text="Update Patient Information", font=("Arial", 14), bg="#FAF0E6").pack(pady=10)
    tk.Label(update_patient_window, text="Patient ID:").pack(pady=5)
    id_entry = tk.Entry(update_patient_window)
    id_entry.pack(pady=5)

    tk.Label(update_patient_window, text="Field to Update (e.g., NAME, AGE, etc.):").pack(pady=5)
    field_entry = tk.Entry(update_patient_window)
    field_entry.pack(pady=5)

    tk.Label(update_patient_window, text="New Value:").pack(pady=5)
    value_entry = tk.Entry(update_patient_window)
    value_entry.pack(pady=5)

    tk.Button(update_patient_window, text="Update", command=submit).pack(pady=20)

def update_doctor():
    def submit():
        doctor_id = id_entry.get()
        field = field_entry.get()
        new_value = value_entry.get()

        db = connect_to_db()
        cursor = db.cursor()
        query = f"UPDATE doctor_id SET {field} = %s WHERE DOC_ID = %s"
        cursor.execute(query, (new_value, doctor_id))
        db.commit()
        db.close()
        messagebox.showinfo("Success", "Doctor record updated successfully")
        update_doctor_window.destroy()

    update_doctor_window = tk.Toplevel(root)
    update_doctor_window.title("Update Doctor")
    update_doctor_window.configure(bg="#FAF0E6")  # Pastel color

    tk.Label(update_doctor_window, text="Update Doctor Information", font=("Arial", 14), bg="#FAF0E6").pack(pady=10)
    tk.Label(update_doctor_window, text="Doctor ID:").pack(pady=5)
    id_entry = tk.Entry(update_doctor_window)
    id_entry.pack(pady=5)

    tk.Label(update_doctor_window, text="Field to Update (e.g., NAME, DEPARTMENT, etc.):").pack(pady=5)
    field_entry = tk.Entry(update_doctor_window)
    field_entry.pack(pady=5)

    tk.Label(update_doctor_window, text="New Value:").pack(pady=5)
    value_entry = tk.Entry(update_doctor_window)
    value_entry.pack(pady=5)

    tk.Button(update_doctor_window, text="Update", command=submit).pack(pady=20)
def book_appointment():
    def submit():
        patient_name = patient_name_entry.get()
        contact_no = contact_no_entry.get()
        doctor_id = doctor_id_entry.get()
        date = date_entry.get_date()  # Get the selected date
        time = f"{hour_spinbox.get().zfill(2)}:{minute_spinbox.get().zfill(2)}:{second_spinbox.get().zfill(2)}"  # Construct time
        
        # Check if doctor is available
        query = """SELECT availability_type FROM doctor_id WHERE doc_id = %s"""
        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute(query, (doctor_id,))
        result = cursor.fetchone()
        db.close()

        if result == 'Available':
            # Insert appointment if doctor is available
            db = connect_to_db()
            cursor = db.cursor()
            query = """INSERT INTO appoint_id (name, contact, doc_id, appointment_date, appointment_time) 
                       VALUES (%s, %s, %s, %s, %s)"""
            values = (patient_name, contact_no, doctor_id, date, time)
            cursor.execute(query, values)
            db.commit()
            db.close()
            messagebox.showinfo("Success", "Appointment booked successfully")
            book_appointment_window.destroy()
        else:
            messagebox.showinfo("Error", "Doctor is not available or not found.")

    book_appointment_window = tk.Toplevel(root)
    book_appointment_window.title("Book Appointment")
    book_appointment_window.configure(bg="#FAF0E6")  # Pastel color

    tk.Label(book_appointment_window, text="Book Appointment", font=("Arial", 14), bg="#FAF0E6").pack(pady=10)
    
    tk.Label(book_appointment_window, text="Patient Name:").pack(pady=5)
    patient_name_entry = tk.Entry(book_appointment_window)
    patient_name_entry.pack(pady=5)

    tk.Label(book_appointment_window, text="Contact Number:").pack(pady=5)
    contact_no_entry = tk.Entry(book_appointment_window)
    contact_no_entry.pack(pady=5)

    tk.Label(book_appointment_window, text="Doctor ID:").pack(pady=5)
    doctor_id_entry = tk.Entry(book_appointment_window)
    doctor_id_entry.pack(pady=5)

    tk.Label(book_appointment_window, text="Select Date:").pack(pady=5)
    date_entry = DateEntry(book_appointment_window, width=12, background='darkblue',
                           foreground='white', borderwidth=2, year=2024)
    date_entry.pack(pady=5)

    # Time Picker Label and Spinboxes
    tk.Label(book_appointment_window, text="Select Time:").pack(pady=5)
    
    # Frame to hold time Spinboxes
    time_frame = tk.Frame(book_appointment_window)
    time_frame.pack(pady=5)
    
    # Hour Spinbox
    hour_spinbox = ttk.Spinbox(time_frame, from_=0, to=23, wrap=True, width=2, state="readonly", justify=tk.CENTER)
    hour_spinbox.set("00")
    hour_spinbox.pack(side=tk.LEFT, padx=5)

    # Minute Spinbox
    minute_spinbox = ttk.Spinbox(time_frame, from_=0, to=59, wrap=True, width=2, state="readonly", justify=tk.CENTER)
    minute_spinbox.set("00")
    minute_spinbox.pack(side=tk.LEFT, padx=5)

    # Second Spinbox
    second_spinbox = ttk.Spinbox(time_frame, from_=0, to=59, wrap=True, width=2, state="readonly", justify=tk.CENTER)
    second_spinbox.set("00")
    second_spinbox.pack(side=tk.LEFT, padx=5)

    # Button to Submit
    submit_btn = tk.Button(book_appointment_window, text="Submit", command=submit)
    submit_btn.pack(pady=10)

    book_appointment_button = tk.Button(root, text="Book Appointment", command=book_appointment)
    book_appointment_button.pack(pady=20)


def cancel_appointment():
    def submit():
        appointment_id = appointment_id_entry.get()
        name = name_entry.get()
        db = connect_to_db()
        cursor = db.cursor()

        # Check if the appointment exists
        check_query = "SELECT * FROM appoint_id WHERE appointment_id = %s "
        cursor.execute(check_query, (appointment_id,))
        appointment = cursor.fetchone()

        if appointment:
            # Update appointment status to 'Cancelled'
            query = "Delete from appoint_id WHERE appointment_id = %s and name = %s "
            cursor.execute(query, (appointment_id,name))
            db.commit()
            messagebox.showinfo("Success", "Appointment canceled successfully")
        else:
            messagebox.showerror("Error", "Appointment not found or already canceled")

        db.close()
        cancel_appointment_window.destroy()

    cancel_appointment_window = tk.Toplevel(root)
    cancel_appointment_window.title("Cancel Appointment")
    cancel_appointment_window.configure(bg="#FAF0E6")  # Pastel color

    tk.Label(cancel_appointment_window, text="Cancel Appointment", font=("Arial", 14), bg="#FAF0E6").pack(pady=10)
    tk.Label(cancel_appointment_window, text="Appointment ID:").pack(pady=5)
    
    appointment_id_entry = tk.Entry(cancel_appointment_window)
    appointment_id_entry.pack(pady=5)
    tk.Label(cancel_appointment_window, text="Patient Name:").pack(pady=5)
    name_entry = tk.Entry(cancel_appointment_window)
    name_entry.pack(pady=5)


    tk.Button(cancel_appointment_window, text="Cancel Appointment", command=submit).pack(pady=20)


def admin_mode():
    def check_password():
        password = password_entry.get()
        if password == "adminpassword":  # Replace with actual admin password logic
            admin_window.destroy()
            admin_menu()
        else:
            messagebox.showerror("Login Failed", "Incorrect password")

    admin_window = tk.Toplevel(root)
    admin_window.title("Admin Login")
    admin_window.configure(bg="#FAF0E6")  # Pastel color

    tk.Label(admin_window, text="Admin Login", font=("Arial", 18, 'bold'), bg="#FAF0E6").pack(pady=10)
    tk.Label(admin_window, text="Password:").pack(pady=5)
    password_entry = tk.Entry(admin_window, show='*')
    password_entry.pack(pady=5)
    tk.Button(admin_window, text="Login", command=check_password).pack(pady=20)

def admin_menu():
    admin_menu_window = tk.Toplevel(root)
    admin_menu_window.title("Admin Menu")
    admin_menu_window.configure(bg="#FAF0E6")  # Pastel color

    tk.Label(admin_menu_window, text="Admin Menu", font=("Arial", 18, 'bold'), bg="#FAF0E6").pack(pady=10)

    tk.Button(admin_menu_window, text="Insert Patient", command=insert_patient).pack(pady=5)
    tk.Button(admin_menu_window, text="Insert Doctor", command=insert_doctor).pack(pady=5)
    tk.Button(admin_menu_window, text="Update Patient", command=update_patient).pack(pady=5)
    tk.Button(admin_menu_window, text="Update Doctor", command=update_doctor).pack(pady=5)
    tk.Button(admin_menu_window, text="Delete Patient", command=delete_patient).pack(pady=5)
    tk.Button(admin_menu_window, text="Delete Doctor", command=delete_doctor).pack(pady=5)
    tk.Button(admin_menu_window, text="View Patients", command=view_patients).pack(pady=5)
    tk.Button(admin_menu_window, text="View Doctors", command=view_doctors).pack(pady=5)
    tk.Button(admin_menu_window, text="View Appointments", command=view_appointments).pack(pady=5)


def user_menu():
    user_menu_window = tk.Toplevel(root)
    user_menu_window.title("User Menu")
    user_menu_window.configure(bg="#FAF0E6")  # Pastel color

    tk.Label(user_menu_window, text="User Menu", font=("Arial", 18, 'bold'), bg="#FAF0E6").pack(pady=20)

    # Adding buttons to the user menu window
    tk.Button(user_menu_window, text="Doctor's availability", command=view_doctors_availability).pack(pady=5)
    tk.Button(user_menu_window, text="Book Appointment", command=book_appointment).pack(pady=5)
    tk.Button(user_menu_window, text="Cancel Appointment", command=cancel_appointment).pack(pady=5)



def main_menu():
    tk.Label(root, text="Hospital Management System", font=("Arial", 24, 'bold'), bg="#FAF0E6").pack(pady=20)

    tk.Button(root, text="Admin Mode", command=admin_mode, width=20).pack(pady=10)
    tk.Button(root, text="User Mode", command=user_menu, width=20).pack(pady=10)

root = tk.Tk()
root.title("Hospital Management System")
root.configure(bg="#FAF0E6")  # Pastel color
root.geometry("400x400")

main_menu()

root.mainloop()
