-- Create a database called University.
CREATE DATABASE University
USE University

/* Create database tables according to your data model.
Create the necessary indexes in the tables.
Build relationships between tables using the keys. Use data types for table fields.
Create the appropriate constraints in the tables.*/
CREATE TABLE Staff(
	StaffNo int NOT NULL IDENTITY(1,1),
	StaffFirstName varchar(255) NOT NULL,
	StaffLastName varchar(255) NOT NULL,
	StaffRegion varchar(255) NOT NULL,
	PRIMARY KEY (StaffNo)
);
CREATE TABLE Student(
	StudentID int NOT NULL IDENTITY(1,1),
	StudentFirstName varchar(255) NOT NULL,
	StudentLastName varchar(255) NOT NULL,
	RegisteredDate datetime NOT NULL,
	StudentRegion varchar(255) NOT NULL,
	StaffNo int NOT NULL,
	CONSTRAINT fk1_staff_no FOREIGN KEY (StaffNo) REFERENCES Staff(StaffNo),
	PRIMARY KEY (StudentID)
);
--CONSTRAINTS :
	--1. A staff member may only counsel or tutor a student who is resident 
	--in the same region as that staff member.
/*
CREATE PROC sp_region
AS
BEGIN
	select *
	from Student s
		inner join Staff f on s.StaffNo = f.StaffNo
	if (s.StudentRegion != f.StaffRegion)
		print 'You have to choose the staff from the same region'
END; */
CREATE FUNCTION fn_checkregion3()
RETURNS INT
AS
BEGIN
	DECLARE @ret INT
	IF EXISTS(
		SELECT StudentRegion
		FROM Student st
			INNER JOIN Staff ff on st.StaffNo = ff.StaffNo
		WHERE st.StudentRegion <> ff.StaffRegion
		) SET @ret = 0
		ELSE SET @ret = 1
	RETURN @ret
END
GO
ALTER TABLE Student
ADD CONSTRAINT check_region2 CHECK(dbo.fn_checkregion3() = 1)
GO

CREATE TABLE Course(
	CourseCode int NOT NULL IDENTITY(1,1),
	Title varchar(255) NOT NULL,
	Credit int NOT NULL CONSTRAINT check_kredit CHECK (Credit=15 OR Credit=30),
	Quota int NOT NULL,
	StaffNo int NOT NULL,
	CONSTRAINT fk2_staf_no FOREIGN KEY (StaffNo) REFERENCES Staff(StaffNo),
	PRIMARY KEY (CourseCode)
);

CREATE TABLE Enrollment(
	StudentID int NOT NULL,
	CourseCode int NOT NULL,
	EnrolledDate datetime NOt NULL,
	FinalGrade int,
	CONSTRAINT fk1_student_id FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
	CONSTRAINT fk1_course_code FOREIGN KEY (CourseCode) REFERENCES Course(CourseCode),
	PRIMARY KEY (StudentID, CourseCode)
);
--CONSTRAINT:
	--2. Students may not take courses simultaneously
	--if their combined points total exceeds 180 points.
CREATE FUNCTION check_points2()
RETURNS INT
AS
BEGIN
	DECLARE @ret INT
	IF EXISTS(
		SELECT e.StudentID, sum(Credit)
		FROM Course c 
			INNER JOIN Enrollment e on c.CourseCode = e.CourseCode
		GROUP BY e.StudentID
		HAVING sum(Credit) > 180
	) SET @ret = 0
	ELSE SET @ret = 1
	RETURN @ret
END;

ALTER TABLE Enrollment
ADD CONSTRAINT check_point2 CHECK (dbo.check_points2() = 1)

select * from Enrollment
select * from Course

insert into Enrollment
values (7, 2, GETDATE(), NULL),
		(7, 3, GETDATE(), NULL),
		(7, 4, GETDATE(), NULL),
		(7, 6, GETDATE(), NULL),
		(7, 7, GETDATE(), NULL)

delete from Enrollment
where StudentID = 7 and CourseCode = 5 

insert into Enrollment
values (7, 5, GETDATE(), NULL)


CREATE TABLE Assignment(
	StudentID int NOT NULL,
	CourseCode int NOT NULL,
	AssignmentNo int NOT NULL,
	Grade int NULL CONSTRAINT check_grade CHECK (Grade BETWEEN 0 AND 100),
	CONSTRAINT fk_student_course FOREIGN KEY (StudentID, CourseCode) REFERENCES Enrollment(StudentID, CourseCode),
	PRIMARY KEY (StudentID, CourseCode, AssignmentNo)
);

-- Insert at least 5 records into each table.
INSERT INTO Staff
VALUES  ('James', 'Smith', 'England'),
		('Maria', 'Hernandez', 'Scotland'),
		('Robert', 'Rodriguez', 'Wales'),
		('Maria', 'Garcia', 'Northern Ireland'),
		('David', 'Smith', 'Northern Ireland'),
		('David', 'Smith', 'Wales');

select *
from staff

INSERT INTO Student
VALUES  ('Nicholas', 'Cage', '2020-10-10','Wales',3),
		('Morgan', 'Freeman', '2020-10-10','Scotland',2),
		('Jim', 'Carrey', '2020-10-05','England',1),
		('Robin', 'Williams', '2019-09-09','Northern Ireland',4),
		('Will', 'Smith', '2019-09-01','Northern Ireland',4),
		('Denzel', 'Washington', '2020-10-01','England',1);

select *
from student

INSERT INTO Course
VALUES  ('Mathematics', 15, 5, 1),
		('History', 30, 4, 2),
		('Physics', 15, 5, 3),
		('Psychology', 30, 4,4),
		('Sociology', 30, 3, 5),
		('Philosophy', 15, 5, 3),
		('Linguistics', 15, 2, 6);

select *
from Course

INSERT INTO Enrollment
VALUES (1, 2, '2020-10-20', 20),
	   (1, 6, '2020-10-21', 55),
	   (1, 7, '2020-10-22', 75),
	   (2, 3, '2020-10-23', 95),
	   (2, 5, '2020-10-24', 90),
	   (3, 5, '2020-10-25', 65),
	   (3, 6, '2020-10-26', 45),
	   (4, 1, '2020-10-27', 80),
	   (4, 2, '2020-10-28', 75),
	   (4, 5, '2020-10-29', 75),
	   (5, 1, '2020-10-29', 75);

INSERT INTO Assignment
VALUES (1, 2, 1, 30),
	   (1, 2, 2, 10),
	   (1, 6, 1, 65),
	   (1, 6, 2, 45),
	   (1, 7, 1, 75),
	   (1, 7, 2, 75),
	   (2, 3, 1, 90),
	   (2, 3, 2, 100),
	   (2, 5, 1, 95),
	   (2, 5, 2, 85),
	   (3, 5, 1, 70),
	   (3, 5, 2, 60),
	   (3, 6, 1, 50),
	   (3, 6, 2, 40),
	   (4, 1, 1, 75),
	   (4, 1, 2, 85),
	   (4, 2, 1, 75),
	   (4, 2, 2, 75),
	   (4, 5, 1, 80),
	   (4, 5, 2, 70);

-- Change a student's grade by creating a SQL script that updates a student's grade in the assignment table.
select * from Assignment
update Assignment
set Grade = 50
where StudentID = 1 and CourseCode = 2 and AssignmentNo=2;

-- Update the credit for a course.
select * from Course

update Course
set Credit = 30
where Title = 'Mathematics';

-- Swap the responsible staff of two students with each other in the student table.
select * from Student
update Student set StaffNo = 2 where StudentID = 1
update Student set StaffNo = 3 where StudentID = 2

-- Remove a staff member who is not assigned to any student from the staff table.
select * from Staff
select *from Course

ALTER TABLE Course
ALTER COLUMN StaffNo int NULL;

update Course
set StaffNo = NULL
where StaffNo not in
	(select distinct(StaffNo)
	from Student)

delete from Staff
where StaffNo not in
	(select distinct(StaffNo)
	from Student)

-- Add a student to the student table and enroll the student you added to any course.
select * from Student
select * from Staff

insert into Student
values('Numan', 'Yilmaz', GETDATE(), 'Wales', 3)

update Student
set StaffNo = 2
where StudentID = 2

select * from Enrollment

insert into Enrollment
values(7, 5, GETDATE(), null)

delete from Student
where StudentFirstName = 'Zeynep'
delete from Student
where StudentFirstName = 'Numan'

update Student
set StaffNo = 3
where StudentID = 3