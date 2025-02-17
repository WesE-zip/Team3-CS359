-- Cruz Urbina
-- Database Design

-- INSERT TEMP DATA
-- INSERT INTO class (proxy) VALUES (1);
-- INSERT INTO class (proxy) VALUES (1);
-- INSERT INTO class (proxy) VALUES (1);
-- INSERT INTO class (proxy) VALUES (1);
-- INSERT INTO class (proxy) VALUES (1);
-- INSERT INTO member (proxy) VALUES (1);
-- INSERT INTO member (proxy) VALUES (1);
-- INSERT INTO member (proxy) VALUES (1);
-- INSERT INTO member (proxy) VALUES (1);
-- INSERT INTO member (proxy) VALUES (1);

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

  
  