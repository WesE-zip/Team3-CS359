-- Cruz Urbina, Christian Kurdi
-- Database Design

--INSERT MEMBER DATA
INSERT INTO member(memberId, name, email, phone, address, age, membershipStartDate, membershipEndDate)
VALUES 
  (1, 'Dwight Schrute', 'beetsmotel@dundermifflin.com', '(888)666-7986', '1212 Livin St Scranton, PA 18447', 35, '2025-01-01', '2025-02-01'),
  (2, 'Michael Scott', 'thatswhat@dundermifflin.com', '(888)452-6985', '3505 Bad Call Dr Scranton, PA 18447', 40, '2024-01-01', '2025-02-01'),
  (3, 'Jim Halpert', 'receptionlover@dundermifflin.com', '(888)892-4562', '7878 Parents Pl Scranton, PA 18447', 30, '2025-03-15', '2026-03-15'),
  (4, 'Pam Beasley', 'saleslover@dundermifflin.com', '(888)651-8889', '7878 Parents Pl Scranton, PA 18447', 29, '2023-03-15', '2024-03-15'),
  (5, 'Kevin Malone', 'barkingdogs@dundermifflin.com', '(888)959-6454', '1111 Chili Way Scranton, PA 18447', 40, '2025-01-01', '2026-01-01'),
  (6, 'Erin Hannon', 'erin.hannon@dundermifflin.com', '(888)959-7878', '3022 Lincoln Pl Scranton, PA 18447', 26, '2025-01-01', '2026-01-01'),
  (7, 'Jan Levinson', 'jan.levinson@dundermifflin.com', '(888)959-6432', '1313 Park Rd Scranton, PA 18447', 42, '2024-01-01', '2025-01-01'),
  (8, 'Andy Bernard', 'andy.bernard@dundermifflin.com', '(888)959-8778', '3512 Mesita Rd Scranton, PA 18447', 36, '2025-01-01', '2026-01-01'),
  (9, 'Karen Filippelli', 'karen.filippelli@dundermifflin.com', '(888)959-4445', '1010 Lake Way Scranton, PA 18447', 35, '2025-01-01', '2026-01-01'),
  (10, 'Angela Martin', 'angela.martin@dundermifflin.com', '(888)959-3022', '1001 West St Scranton, PA 18447', 32, '2025-01-01', '2026-01-01');

--INSERT MEMBERSHIP PLAN DATA
INSERT INTO membershipPlan(planId, planType, cost)
VALUES 
  (1, 'Monthly', 49.95),
  (2, 'Monthly', 69.95),
  (3, 'Annual', 99.99), 
  (4, 'Annual', 125.99),
  (5, 'Annual', 200.99);

--INSERT PAYMENT DATA
INSERT INTO payment(paymentId, memberId, planId, amountPaid, paymentDate)
VALUES
  (1, 1, 1, 49.95, '2025-01-01'),
  (2, 1, 2, 69.95, '2025-01-20'),
  (3, 2, 2, 69.95, '2025-01-01'),
  (4, 4, 3, 99.99, '2025-03-15'),
  (5, 5, 5, 200.99, '2025-01-01');


-- INSERT GYM FACILITY DATA
INSERT INTO gymFacility (location, phone, manager)
VALUES
  ('Northwest', '(888)789-1122', 'Russell Walter'),
  ('Mission Valley', '(888)789-1244', 'Jesus Garcia'),
  ('Meadows', '(888)321-3642', 'Alexis Wayne'),
  ('Sun Ridge', '(888)789-4512', 'Luis Montoya'),
  ('Mesilla Park', '(888)321-8956', 'Tyler Mason');

-- INSERT EQUIPMENT DATA  
INSERT INTO equipment (name, type, quantity, gymId)
VALUES
  ('Bench Press', 'Strength', 6, 1),
  ('Bench Press', 'Strength', 8, 2),
  ('Bench Press', 'Strength', 10, 3),
  ('Treadmill', 'Cardio', 10, 2),
  ('Treadmill', 'Cardio', 8, 3),
  ('Treadmill', 'Cardio', 8, 4),
  ('Exercise Bike', 'Cardio', 4, 1),
  ('Exercise Bike', 'Cardio', 10, 2),
  ('Exercise Bike', 'Cardio', 8, 3),
  ('Crosstrainer', 'Strength', 5, 2),
  ('Kettlebelss', 'Strength', 8, 1),
  ('Kettlebelss', 'Strength', 7, 2),
  ('Kettlebelss', 'Strength', 7, 3),
  ('Yoga Mat', 'Flexibility', 10, 2),
  ('Stretch Straps', 'Flexibility', 5, 1),
  ('Refrigerant Recovery Machine', 'Recovery', 1, 2),
  ('Massage Gun', 'Recovery', 5, 1);

--INSERT INSTRUCTOR DATA
INSERT INTO Instructor (instructorId, name, specialty, phone, email)
VALUES
  (1, 'Ethan', 'HIIT', '(888)789-1245','E.Hunt.instructor@XYZgym.com'),
  (2, 'Parker', 'Yoga', '(888)789-4513','Parker.instructor@XYZgym.com'),
  (3, 'Hardison', 'Zumba', '(888)789-4514','Hardison.instructor@XYZgym.com'),
  (4, 'Elliot', 'HIIT', '(888)789-4515','Elliot.instructor@XYZgym.com'),
  (5, 'Nate', 'Weights', '(888)789-4516','Nate.instructor@XYZgym.com');

--INSERT CLASS DATA
INSERT INTO   class (classId, className, classType, duration, classCapacity, instructorId, gymID)
VALUES
  (1, 'HIIT', 'Flexibility', 10, 5, 1, 2),
  (2, 'Yoga', 'Flexibility', 10, 5, 2, 4),
  (3, 'Zumba', 'Cardio', 20, 10, 3, 1),
  (4, 'Weights', 'Strength', 30, 5, 5, 1),
  (5, 'Cardio Blast', 'Cardio', 20, 5, 1, 4),
  (6, 'Strength Training', 'Strength', 20, 5, 2, 2),
  (7, 'Body Pump', 'Strength', 30, 5, 3, 4),
  (8, 'Pilates', 'Cardio', 20, 10, 1, 4);
  
-- INSERT ATTENDS DATA
INSERT INTO attends (memberId, classId, attendanceDate)
VALUES
  (1, 1, '2025-01-05'),
  (2, 1, '2025-01-10'),
  (3, 1, '2025-01-12'),
  (1, 2, '2025-01-02'),
  (1, 1, '2025-02-10'),
  (4, 3, '2025-02-10'),
  (3, 1, '2025-02-10'),
  (1, 2, '2025-02-12'),
  (2, 4, '2025-02-12'),
  (3, 2, '2025-02-12'),
  (1, 3, '2025-02-15'),
  (2, 1, '2025-02-15'),
  (3, 4, '2025-02-15'),
  (1, 2, '2025-02-18'),
  (2, 3, '2025-02-18'),
  (3, 2, '2025-02-24'),
  (1, 3, '2025-02-25'),
  (4, 4, '2025-03-01'),
  (1, 4, '2025-03-02'),
  (1, 3, '2025-03-09'),
  (2, 1, '2025-03-10'),
  (1, 2, '2025-03-12'),
  (2, 4, '2025-03-12'),
  (3, 2, '2025-03-12'),
  (1, 3, '2025-03-13'),
  (2, 1, '2025-03-14'),
  (3, 4, '2025-03-14'),
  (3, 1, '2025-03-15'),
  (4, 3, '2025-03-18'),
  (2, 4, '2025-03-20'),
  (1, 2, '2025-03-22'),
  (2, 2, '2025-03-22'),
  (3, 2, '2025-03-28'),
  (1, 3, '2025-03-30'),
  (3, 4, '2025-04-04'),
  (1, 4, '2025-04-04');
