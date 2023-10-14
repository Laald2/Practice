'''
This script is the interface between the database 
and the website
'''
# pylint disable
from flask import Flask, make_response, redirect, render_template, request
import mysql.connector
#  plint enable

#needed for handling connection issues
#pylint disable=broad-exception--caught
app = Flask(__name__)
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="La9030",
        database="project"
    )
mycursor = mydb.cursor()

@app.route('/')
def index():
    '''
    starts page on html script
    '''
    return render_template('index.html')

@app.route('/logout')
def logout():
    '''
    Allows  to logout
    '''
    # Redirect to the login page
    return render_template('index.html')
@app.route('/search_employee', methods=['GET', 'POST'])
def search_employee():

    value = request.form.get("search-input")
    column = request.form.get("search-option-column")
    table = request.form.get("search-option-table")

    # Fetch column names from the table
    mycursor.execute("SHOW COLUMNS FROM " + table)
    columns = [column[0] for column
               in mycursor.fetchall() if column[0] not in
               ['mgrSSN', 'EmployeeSSN', 'SSN']]

    mycursor.execute(f"SELECT {','.join([col for col in columns if col not in ['mgrSSN', 'EmployeeSSN', 'SSN']])} FROM {table} WHERE {column} = %s", (value,))

    rows = mycursor.fetchall()
    return render_template('search.html', columns=columns, rows=rows)

@app.route('/search', methods=['POST'])
def search():
    '''
    Allow searching through tables
    '''
    value = request.form.get("search-input")
    column = request.form.get("search-option-column")
    table = request.form.get("search-option-table")

    # Fetch column names from the table
    mycursor.execute("SHOW COLUMNS FROM " + table)
    columns = [column[0] for column in mycursor.fetchall()]

    sql = "SELECT * FROM " + table + " WHERE " + column + " = %s"
    val = (value,)

    mycursor.execute(sql, val)
    rows = mycursor.fetchall()
    return render_template('search.html', columns=columns, rows=rows)

@app.route('/login', methods=['POST'])
def login():
    '''
    Handle log in page of website
    '''
    username = request.form['username']
    password = request.form['password']
    #manager
    if username == 'manager' and password == 'manager':
        mycursor.execute("SELECT * FROM Tickets")
        rows = mycursor.fetchall()
        #employee rows
        mycursor.execute("SELECT * FROM Employee")
        e_row = mycursor.fetchall()
        #department
        mycursor.execute("SELECT * FROM Department")
        department_row = mycursor.fetchall()
        #department locations
        mycursor.execute("SELECT * FROM department_locations")
        dl_row = mycursor.fetchall()
        #works on
        mycursor.execute("""DELETE FROM WORKS_ON
            WHERE ticketNumber IN (
            SELECT ticketNumber FROM Tickets
            WHERE ticketStatus = 'closed')
        """)
        mycursor.execute("SELECT * FROM works_on")
        w_row = mycursor.fetchall()
        #dependent
        mycursor.execute("SELECT * FROM dependent")
        dependent_row = mycursor.fetchall()

        return render_template('mainPage.html', rows=rows, e_row=e_row, department_row=department_row,
        dl_row=dl_row, w_row=w_row, dependent_row=dependent_row)
    if username == 'employee' and password == 'employee':
        mycursor.execute("SELECT * FROM Tickets")
        rows = mycursor.fetchall()
        #employee rows
        mycursor.execute("SELECT * FROM Employee")
        e_row = mycursor.fetchall()
        #department
        mycursor.execute("SELECT * FROM Department")
        department_row = mycursor.fetchall()
        #department locations
        mycursor.execute("SELECT * FROM department_locations")
        dl_row = mycursor.fetchall()
        #works on
        mycursor.execute("""DELETE FROM WORKS_ON
            WHERE ticketNumber IN (
            SELECT ticketNumber FROM Tickets
            WHERE ticketStatus = 'closed')
        """)
        mycursor.execute("SELECT * FROM works_on")
        w_row = mycursor.fetchall()
        #dependent
        mycursor.execute("SELECT * FROM dependent")
        dependent_row = mycursor.fetchall()

        return render_template('employeePage.html',
                rows=rows, e_row=e_row, department_row=department_row,
                dl_row=dl_row, w_row=w_row, dependent_row=dependent_row)
    # If the username or password are incorrect, display an error message
    return render_template('index.html', error='Invalid username or password')

@app.route('/add_ticket', methods=['POST'])
def add_ticket():
    '''
    add a ticket into the database
    '''
   # Get the form data
    employee_id = ''
    ticket_name = request.form["ticketName"]
    assigned_employee = request.form["assignedEmployee"]
    ticket_status = request.form["ticketStatus"]
    ticket_id = request.form["ticketID"]
    ticket_location = request.form["ticketLocation"]
    priority_number = int(request.form["priorityNumber"])
    department_number = request.form["departmentNumber"]
    created_date = datetime.date.today()

    hours = request.form["hours"]

    # Search for employeeSSN using employeeID
    mycursor.execute("SELECT ID FROM Employee WHERE SSN = %s", (assigned_employee,))
    result = mycursor.fetchone()
    if result:
        employee_id = result[0]
    else:
        # handle the case where no employeeSSN is found for the given employeeID
        return render_template('error.html', message='Employee not found')

    # Insert the data into the database
    try:
        # Note that ticketNumber is omitted from the
        # column list because it is an auto_increment field
        sql = """INSERT INTO Tickets (ticketName, assignedEmployee,
        ticketStatus, ticketLocation, priorityNumber, departmentNumber, 
        createdDate) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        val = (ticket_name, employee_id, ticket_status, ticket_location,
               priority_number, department_number, created_date)
        mycursor.execute(sql, val)
        mydb.commit()

        sql = "INSERT INTO WORKS_ON (EmployeeSSN, ticketNumber, HOURS) VALUES (%s, %s, %s)"
        val = (assigned_employee, ticket_id, hours)
        mycursor.execute(sql, val)
        mydb.commit()

        mycursor.execute("""DELETE FROM WORKS_ON
            WHERE ticketNumber IN (
            SELECT ticketNumber FROM Tickets
            WHERE ticketStatus = 'closed')
        """)
        mydb.commit()
        mycursor.execute("SELECT * FROM Tickets")
        rows = mycursor.fetchall()
        #employee rows
        mycursor.execute("SELECT * FROM Employee")
        e_row = mycursor.fetchall()
        #department
        mycursor.execute("SELECT * FROM Department")
        department_row = mycursor.fetchall()
        #department locations
        mycursor.execute("SELECT * FROM department_locations")
        dl_row = mycursor.fetchall()
        #works on
        mycursor.execute("SELECT * FROM works_on")
        w_row = mycursor.fetchall()
        #dependent
        mycursor.execute("SELECT * FROM dependent")
        dependent_row = mycursor.fetchall()

        return render_template('mainPage.html', rows=rows, e_row=e_row, department_row=department_row,
        dl_row=dl_row, w_row=w_row, dependent_row=dependent_row)
    except Exception as e:
        return render_template('error.html', message=str(e))


@app.route('/update_status', methods=['POST'])
def update_status():
    '''
    Update the ticket status in the database
    '''
    employee_id = ''
   # Get the form data
    ticket_status = request.form["ticketStatus"]
    ticket_id = request.form["ticketID"]
    assigned_employee = request.form["assigned_employee"]
    hours = request.form["hours"]

    # Update the data in the database
    try:
        # Note that ticketNumber is omitted from the column
        # list because it is an auto_increment field
        sql = """UPDATE TICKETS
        SET ticketStatus = %s
        WHERE ticketNumber = %s"""

        mycursor.execute(sql, (ticket_status, ticket_id))
        mydb.commit()

        if ticket_status.lower() == "open":
            # Search for employeeSSN using employeeID
            mycursor.execute("SELECT ID FROM Employee WHERE SSN = %s", (assigned_employee,))
            result = mycursor.fetchone()

            if result:
                employee_id = result[0]
            else:
                # handle the case where no employeeSSN is found for the given employeeID
                return render_template('error.html', message='Employee not found')
            sql = """UPDATE TICKETS
            SET assignedEmployee = %s
            WHERE ticketNumber = %s"""
            mycursor.execute(sql, (employee_id, ticket_id))
            mydb.commit()
        mycursor.execute("SELECT * FROM Tickets")
        rows = mycursor.fetchall()
        #employee rows
        mycursor.execute("SELECT * FROM Employee")
        e_row = mycursor.fetchall()
        #department
        mycursor.execute("SELECT * FROM Department")
        department_row = mycursor.fetchall()
        #department locations
        mycursor.execute("SELECT * FROM department_locations")
        dl_row = mycursor.fetchall()
        #works on
        mycursor.execute("""DELETE FROM WORKS_ON
            WHERE ticketNumber IN (
            SELECT ticketNumber FROM Tickets
            WHERE ticketStatus = 'closed')
        """)

        if ticket_status.lower() == "open":
            sql = """INSERT INTO WORKS_ON
                VALUES (%s, %s, %s)"""
            mycursor.execute(sql, (assigned_employee, ticket_id, hours))
            mydb.commit()

        mycursor.execute("SELECT * FROM works_on")
        w_row = mycursor.fetchall()
        #dependent
        mycursor.execute("SELECT * FROM dependent")
        dependent_row = mycursor.fetchall()

        return render_template('mainPage.html', rows=rows, e_row=e_row, department_row=department_row,
        dl_row=dl_row, w_row=w_row, dependent_row=dependent_row)
    except Exception as e:
        return render_template('error.html', message=str(e))

@app.route('/update_assigned_employee', methods=['POST'])
def update_assigned_employee():
    employee_id = ''
   # Get the form data
    ticket_id = request.form["ticketID"]
    newAssignedEmployee = request.form["assignedEmployeeChange"]

    # Search for employeeSSN using employeeID
    mycursor.execute("SELECT ID FROM Employee WHERE SSN = %s", (newAssignedEmployee,))
    result = mycursor.fetchone()
    if result:
        employee_id = result[0]
    else:
        # handle the case where no employeeSSN is found for the given employeeID
        return render_template('error.html', message='Employee not found')

    # Update the data in the database
    try:
        # Note that ticketNumber is omitted from the column
        # list because it is an auto_increment field
        sql = """UPDATE TICKETS
        SET assignedEmployee = %s
        WHERE ticketNumber = %s"""
        mycursor.execute(sql, (employee_id, ticket_id))
        mydb.commit()
        sql = """UPDATE Works_On
        SET EmployeeSSN = %s
        WHERE ticketNumber = %s"""
        mycursor.execute(sql, (newAssignedEmployee, ticket_id))
        mydb.commit()

        mycursor.execute("SELECT * FROM Tickets")
        rows = mycursor.fetchall()
        #employee rows
        mycursor.execute("SELECT * FROM Employee")
        e_row = mycursor.fetchall()
        #department
        mycursor.execute("SELECT * FROM Department")
        department_row = mycursor.fetchall()
        #department locations
        mycursor.execute("SELECT * FROM department_locations")
        dl_row = mycursor.fetchall()
        #works on
        mycursor.execute("""DELETE FROM WORKS_ON
            WHERE ticketNumber IN (
            SELECT ticketNumber FROM Tickets
            WHERE ticketStatus = 'closed' OR ticketStatus = 'Closed')
        """
        mydb.commit()
        mycursor.execute("SELECT * FROM works_on")
        w_row = mycursor.fetchall()
        #dependent
        mycursor.execute("SELECT * FROM dependent")
        dependent_row = mycursor.fetchall()

        return render_template('mainPage.html', rows=rows, e_row=e_row, department_row=department_row,
        dl_row=dl_row, w_row=w_row, dependent_row=dependent_row)
    except Exception as e:
        return render_template('error.html', message=str(e))

if __name__ == '__main__':
    app.run()
