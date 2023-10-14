INSERT INTO Employee (employeeName, ID, SSN, SEX, StartDate, Address, departmentNumber, Salary, birthday)
VALUES
    ('Jane Smith','001', '123456789', 'female', '2023-01-01', '1 Fake Address', '4', '60000','1971-01-01'),
    ('Jane Doe', '002', '135762783', 'female', '2022-03-04', '2 Somewhere', '3', '52000', '1978-04-02'),
    ('Bob Johnson', '003', '928940109', 'male', '2021-02-18', '5 Random Place', '7', '64000', '1973-05-26');
    
INSERT INTO department (departmentName, departmentNumber, mgrSSN, numEmployees)
VALUES
    ('Name4','4', '123456789', '1'),
    ('Name3','3', '135762783', '1'),
    ('Name7','7', '928940109', '1');
    
INSERT INTO department_locations (departmentNumber, departmentLocation)
VALUES
    ('4', '4 Company Address'),
    ('3', '3 Company Address'),
    ('7', '7 Company Address');

INSERT INTO Tickets (ticketName, assignedEmployee, ticketStatus, ticketLocation, priorityNumber, departmentNumber, createdDate)
VALUES
    ('Network Issue','002', 'Open', '3 Company Address', '1', '3', '2022-01-01'),
    ('Database Error','001', 'Closed', '4 Company Address', '1', '4', '2022-01-02'),
    ('Website Bug','003', 'Open', '7 Company Address', '2','7', '2022-01-03'),
    ('Payment Problem','003', 'Closed', '7 Company Address','1', '7', '2022-01-04'),
    ('Email Not Sending','002', 'Open', '3 Company Address','3', '3', '2022-01-05');

INSERT INTO works_on (employeeSSN, ticketNumber, HOURS)
VALUES
    ('135762783', '1', '10'),
    ('135762783', '5', '10'),
    ('123456789', '2', '10'),
    ('928940109', '3', '10'),
    ('928940109', '4', '10');
    
INSERT INTO dependent(employeeSSN, dependentName, SEX, Birthday, Relationship)
VALUES
	('928940109', 'jill Jack', 'female', '2020-01-01', 'daughter');