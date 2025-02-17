-- Cruz Urbina
-- Database Design

-- DROP TABLE equipment;
-- DROP TABLE gym_facility;
-- DROP TABLE attends;
-- DROP TABLE class;
-- DROP TABLE member;

-- MEMBER TEMP TABLE
-- CREATE TABLE member (
-- 	member_id INTEGER PRIMARY KEY AUTOINCREMENT,
-- 	proxy INTEGER
-- );

-- -- CLASS TEMP TABLE
-- CREATE TABLE class (
-- 	class_id INTEGER PRIMARY KEY AUTOINCREMENT,
-- 	proxy INTEGER
-- );


-- EQUIPMENT TABLE
CREATE TABLE equipment (
  equipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL,
  type VARCHAR(30)
            CHECK( 
                type == "Cardio" OR
                type == "Strength" OR
                type == "Flexibility" OR
                type == "Recovery"),
  quantity INTEGER(30),
  gym_id INTEGER,
  FOREIGN KEY(gym_id) REFERENCES gym_facility(gym_id)
);

-- GYM FACILITY TABLE
CREATE TABLE gym_facility (
  gym_id INTEGER PRIMARY KEY AUTOINCREMENT,
  location VARCHAR(100),
  phone VARCHAR(50),
  manager VARCHAR(50)
);

-- ATTENDS TABLE
CREATE TABLE attends (
  member_id INTEGER NOT NULL,
  class_id INTEGER NOT NULL,
  attendance_date DATE NOT NULL,
  PRIMARY KEY (member_id, class_id, attendance_date),
  FOREIGN KEY(member_id) REFERENCES member(member_id),
  FOREIGN KEY(class_id) REFERENCES class(class_id)
);
