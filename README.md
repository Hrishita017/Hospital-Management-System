# Hospital Management System

## Description

The Hospital Management System is a comprehensive Python-based application designed to streamline the operations of a hospital or healthcare facility. This system integrates MySQL for database management and provides functionalities for managing patient appointments, doctor schedules, and patient records. The application features a user-friendly graphical interface built using Tkinter, enabling easy interaction and management of hospital data.

### Key Features

- **Appointment Management**: Schedule, update, and cancel patient appointments with doctors. Track appointment statuses (e.g., scheduled, cancelled).
- **Doctor Management**: Maintain a database of doctors including their ID, name, department, contact number, and availability status.
- **Patient Records**: Manage patient information including name, age, gender, blood group, contact number, and assigned room number.
- **Date and Time Picker**: Use integrated date and time pickers to select appointment dates and times easily.
- **Data Validation**: Ensure appointments are only booked with available doctors and manage invalid inputs effectively.

### Technology Stack

- **Backend**: Python
- **Database**: MySQL
- **GUI**: Tkinter
- **Date Handling**: `tkcalendar`

### Installation

1. **Create and Set Up the Database**:
   - Use the provided `schema.sql` to create the necessary tables in a MySQL database.
   - Optionally, use `data.sql` to populate the database with sample data.

2. **Install Python Dependencies**:
   - Install the required Python packages.

3. **Run the Application**:
   - Execute the `hospital_management.py` script to start the application.

### Database Schema

The system includes the following key tables:

- **doctor_id**: Stores information about doctors, including their ID, name, department, contact number, and availability.
- **patient_id**: Stores information about patients, including their ID, name, age, gender, blood group, contact number, and room number.
- **appoint_id**: Manages appointment details, including patient name, contact information, doctor ID, appointment date and time, and appointment status.

### Example Use Case

1. **Book an Appointment**: A user can book an appointment by entering patient details, selecting a date and time, and choosing an available doctor.
2. **Manage Appointments**: Users can view, update, or cancel existing appointments and ensure proper scheduling based on doctor availability.

### Contribution

Contributions to improve and extend the system are welcome. Please refer to the contribution guidelines in the repository for more details.

