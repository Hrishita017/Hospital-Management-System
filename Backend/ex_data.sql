
INSERT INTO doctor_id (doc_id, name, department, contact_no, availability_type) VALUES
(2, 'Dr. Alice Johnson', 'Neurology', '0987654321', 'Unavailable'),
(3, 'Dr. Emily Davis', 'Pediatrics', '5555555555', 'Available'),
(4, 'Dr. Michael Brown', 'Orthopedics', '6666666666', 'Available');


INSERT INTO patient_id (id, name, age, gender, blood_group, contact_no, room_no) VALUES
(3, 'Emily Johnson', 40, 'F', 'B+', '1122334455', 103),
(4, 'Michael Brown', 50, 'M', 'AB-', '5566778899', 104);


INSERT INTO appoint_id (name, contact, doc_id, appointment_date, appointment_time, status) VALUES
('John Doe', '1234567890', 1, '2024-09-15', '10:30:00', 'Cancelled'),
('Jane Smith', '0987654321', 2, '2024-09-16', '11:00:00', 'Cancelled'),
('Emily Johnson', '5678901234', 1, '2024-09-17', '09:00:00', 'Cancelled'),
('Michael Brown', '6789012345', 3, '2024-09-18', '14:00:00', 'Cancelled'),
('Naman Jain', '8928600618', 2, '2024-10-12', '13:30:00', 'Cancelled'),
('AB', '1234567891', 3, '2024-09-11', '00:00:00', 'Scheduled');
