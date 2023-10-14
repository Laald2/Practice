
CREATE TABLE IF NOT EXISTS EMPLOYEE(
	employeeName VARCHAR(20),
    ID VARCHAR(20),
    SSN VARCHAR(9),
    SEX CHAR(6),
    StartDate DATE,
    Address VARCHAR(20),
    departmentNumber VARCHAR(20),
    Salary FLOAT,
    birthday DATE,
    primary key(ID, SSN),
    INDEX(SSN)
);
CREATE TABLE IF NOT EXISTS DEPARTMENT(
	departmentName VARCHAR(20),
    departmentNumber VARCHAR(20),
    mgrSSN VARCHAR(9),
    numEmployees int,
    primary key(departmentNumber),
    foreign key(mgrSSN) references employee(SSN)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS DEPARTMENT_LOCATIONS(
	departmentNumber VARCHAR(20) references department(departmentNumber),
    departmentLocation VARCHAR(20),
    primary key(departmentNumber, departmentLocation)
);
CREATE TABLE IF NOT EXISTS Tickets(
	ticketName VARCHAR(50),
    ticketNumber INT auto_increment,
    assignedEmployee VARCHAR(20),
    ticketStatus CHAR(20),
    ticketLocation varchar(20),
    priorityNumber int,
    departmentNumber VARCHAR(20),
    createdDate date,
    UNIQUE(ticketNumber),
    primary key(ticketNumber, ticketLocation),
    foreign key(assignedEmployee) references employee(ID),
    foreign key(departmentNumber) references department_locations(departmentNumber)
);

CREATE TABLE IF NOT EXISTS WORKS_ON(
	EmployeeSSN varchar(9) references employee(SSN),
    ticketNumber INT references Tickets(ticketNumber),
    HOURS int,
    UNIQUE(ticketNumber),
    primary key(EmployeeSSN, ticketNumber)
);
CREATE TABLE IF NOT EXISTS DEPENDENT(
	EmployeeSSN VARCHAR(9) references employee(SSN),
    DependentName VARCHAR(20),
    SEX CHAR(6),
    Birthday DATE,
    RELATIONSHIP CHAR(12),
    primary key(EmployeeSSN, DependentName)
);

CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT ON project.Tickets TO 'newuser'@'localhost';
GRANT INSERT, UPDATE ON project.Tickets TO 'newuser'@'localhost';
FLUSH PRIVILEGES;
