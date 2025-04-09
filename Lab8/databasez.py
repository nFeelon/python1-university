from pydoc import doc
import sqlite3

connection = sqlite3.connect('aid_database.db')
cursor = connection.cursor()

create_tables = """
CREATE TABLE IF NOT EXISTS patient (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    birth_date DATE NOT NULL,
    contact_info TEXT
);

CREATE TABLE IF NOT EXISTS doctor (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    specialty TEXT NOT NULL,
    hospital_id INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS appointment (
    id INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,
    appointment_date DATE NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patient(id),
    FOREIGN KEY (doctor_id) REFERENCES doctor(id)
);
"""

cursor.executescript(create_tables)

insert_data = """
INSERT INTO patient (name, birth_date, contact_info)
VALUES ('Nikita Filon', '2005-01-01', 'n@f.by'),
       ('Mister Brister', '2003-01-01', 'm@b.by');

INSERT INTO doctor (name, specialty, hospital_id)
VALUES ('Dr. Filon', 'Cardiology', 1),
       ('Dr. Helper', 'Neurology', 2),
       ('Dr. Pupko', 'Pediatrics', 3);

INSERT INTO appointment (patient_id, doctor_id, appointment_date)
VALUES (1, 1, '2022-01-01'),
       (2, 2, '2022-02-01'),
       (1, 3, '2022-03-01');
"""

cursor.executescript(insert_data)
connection.commit()
connection.close()

##############
connection = sqlite3.connect("aid_database.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM doctor")
doctors = cursor.fetchall()
print(doctors)

cursor.execute("SELECT * FROM doctor WHERE specialty = ?", ("Cardiology",))
doctors = cursor.fetchall()
print("Доктора кардиологи::")
for doctor in doctors:
    print(doctor)

cursor.execute("SELECT * FROM patient WHERE birth_date < ?", ("2004-01-01",))
patients = cursor.fetchall()
print("Пациенты рожденные раньше 2004-01-01:")
for patient in patients:
    print(patient)

cursor.execute("SELECT * FROM appointment WHERE appointment_date > ?", ("2022-01-01",))
appointments = cursor.fetchall()
print("Записи после 2022-01-01:")
for appointment in appointments:
    print(appointment)

cursor.execute("""
SELECT p.name AS patient_name, d.name AS doctor_name, a.appointment_date
FROM patient p
INNER JOIN appointment a ON p.id = a.patient_id
INNER JOIN doctor d ON a.doctor_id = d.id
""")
appointments = cursor.fetchall()
print("Информация о записях:")
for appointment in appointments:
    print(appointment)

connection.close()


###############
connection = sqlite3.connect('aid_database.db')
cursor = connection.cursor()

cursor.execute("UPDATE doctor SET specialty = 'Python-cardio' WHERE name = ?", ("Dr. Filon",))

connection.commit()
connection.close()


#####################
connection = sqlite3.connect('aid_database.db')
cursor = connection.cursor()

cursor.execute("DELETE FROM doctor WHERE specialty = ?", ("Neurology",))
cursor.execute("SELECT * FROM doctor")
doctors = cursor.fetchall()
print(doctors)

connection.commit()
connection.close()
