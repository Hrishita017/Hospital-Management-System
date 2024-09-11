
=
CREATE TABLE doctor_id (
    doc_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    department VARCHAR(255) NOT NULL,
    contact_no VARCHAR(15) NOT NULL,
    availability_type ENUM('Available', 'Unavailable') NOT NULL
);


CREATE TABLE patient_id (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    gender CHAR(1) NOT NULL,
    blood_group VARCHAR(10) NOT NULL,
    contact_no VARCHAR(15) NOT NULL,
    room_no INT NOT NULL
);


CREATE TABLE appoint_id (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    contact VARCHAR(15) NOT NULL,
    doc_id INT,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    status ENUM('Scheduled', 'Cancelled') DEFAULT 'Scheduled',
    FOREIGN KEY (doc_id) REFERENCES doctor_id(doc_id)
);
