-- Cruz Urbina, Christian Kurdi
-- Database Design

-- INSERT TEMP DATA
-- INSERT INTO class (proxy) VALUES (1);
-- INSERT INTO class (proxy) VALUES (1);
-- INSERT INTO class (proxy) VALUES (1);
-- INSERT INTO class (proxy) VALUES (1);
-- INSERT INTO class (proxy) VALUES (1);

--INSERT MEMBER DATA
INSERT INTO member(memberId, name, email, phone, address, age, membershipStartDate, membershipEndDate)
VALUES 
  (1, 'Dwight Schrute', 'beetsmotel@dundermifflin.com', '(888)666-7986', '1212 Livin St Scranton, PA 18447', 35, '2025-01-01', '2025-02-01'),
  (2, 'Michael Scott', 'thatswhat@dundermifflin.com', '(888)452-6985', '3505 Bad Call Dr Scranton, PA 18447', 40, '2025-01-01', '2026-02-01'),
  (3, 'Jim Halpert', 'receptionlover@dundermifflin.com', '(888)892-4562', '7878 Parents Pl Scranton, PA 18447', 30, '2025-03-15', '2026-03-15'),
  (4, 'Pam Beasley', 'saleslover@dundermifflin.com', '(888)651-8889', '7878 Parents Pl Scranton, PA 18447', 29, '2025-03-15', '2026-03-15'),
  (5, 'Kevin Malone', 'barkingdogs@dundermifflin.com', '(888)959-6454', '1111 Chili Way Scranton, PA 18447', 40, '2025-01-01', '2026-01-01');

--INSERT MEMBERSHIP PLAN DATA
INSERT INTO membershipPlan(planId, planType, cost)
VALUES 
  (1, 'Monthly', 49.95),
  (2, 'Monthly', 69.95),
  (3, 'Annually', 99.99), 
  (4, 'Annually', 125.99),
  (5, 'Annually', 200.99);

--INSERT PAYMENT DATA
INSERT INTO payment(paymentId, memberId, planId, amountPaid, paymentDate)
VALUES
  (1, 1, 1, 49.95, '2025-01-01'),
  (2, 1, 2, 69.95, '2025-01-20'),
  (3, 2, 2, 69.95, '2025-01-01'),
  (4, 4, 3, 99.99, '2025-03-15'),
  (5, 5, 5, 200.99, '2025-01-01');


-- INSERT GYM FACILITY DATA
INSERT INTO gym_facility (location, phone, manager)
VALUES
  ('Northwest', '(888)789-1122', 'Russell Walter'),
  ('Mission Valley', '(888)789-1244', 'Jesus Garcia'),
  ('Meadows', '(888)321-3642', 'Alexis Wayne'),
  ('Sun Ridge', '(888)789-4512', 'Luis Montoya'),
  ('Mesilla Park', '(888)321-8956', 'Tyler Mason');

-- INSERT EQUIPMENT DATA  
INSERT INTO equipment (name, type, quantity, gym_id)
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

-- INSERT ATTENDS DATA
INSERT INTO attends (member_id, class_id, attendance_date)
VALUES
  (1, 1, DATE('now')),
  (2, 1, DATE('now')),
  (3, 1, DATE('now')),
  (1, 2, DATE('now')),
  (2, 2, DATE('now')),
  (3, 2, DATE('now')),
  (1, 3, DATE('now'));

--INSERT INSTRUCTOR DATA
INSERT INTO Instructor (instructorId, name, specialty, phone, email)
VALUES
  (1, 'Ethan Hunt', 'HIIT', '(888)789-1245','E.Hunt.instructor@XYZgym.com'),
  (2, 'Parker', 'Yoga', '(888)789-4513','Parker.instructor@XYZgym.com'),
  (3, 'Hardison', 'Zumba', '(888)789-4514','Hardison.instructor@XYZgym.com'),
  (4, 'Elliot', 'HIIT', '(888)789-4515','Elliot.instructor@XYZgym.com'),
  (5, 'Nate', 'Weights', '(888)789-4516','Nate.instructor@XYZgym.com');

--INSERT CLASS DATA
INSERT INTO   class (classId, className, classType, duration, classCapacity, instrucotorId, gymID)
VALUES
  (1, 'HIIT with Hunt', 'HIIT', 20, 5, 1, 2),
  (2, 'HIIT with Elliot', 'HIIT', 20, 5, 4, 4),
  (3, 'Weights with Nate', 'Weights', 20, 5, 5, 4),
  (4, 'Zumba with Hardison', 'Zumba', 20, 5, 3, 4),
  (5, 'Yoga with Parker', 'Yoga', 5, 5, 2, 4);
