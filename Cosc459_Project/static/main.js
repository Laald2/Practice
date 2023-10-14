function addTicket(event) {

    event.preventDefault(); // prevent default form submission behavior

    // Get values from form inputs
    var name = document.getElementById("ticketName").value;
    var id = document.getElementById("ticketID").value;
    var employee = document.getElementById("assignedEmployee").value;
    var status = document.getElementById("ticketStatus").value;
    var ticketLocation = document.getElementById("ticketLocation").value;
    var priorityNumber = document.getElementById("priorityNumber").value;
    var departmentNumber = document.getElementById("departmentNumber").value;
    var hours = document.getElementById("hours").value;
    var today = new Date().toLocaleDateString();
    const [month, day, year] = today.split('/');

    // Generate yyyy-mm-dd date string
    var formattedDate = year + "-" + month + "-" + day;
    console.log(formattedDate);

    // Create new table row
    var table = document.getElementById("ticketTable");
    var newRow = table.insertRow(-1);
    var newRowWorksOn = document.getElementById("WorksOnTable")
    var newRowWorksOn = worksOnTable.insertRow(-1);

    // Add cells to new row
    var nameCell = newRow.insertCell(0);
    var idCell = newRow.insertCell(1);
    var employeeCell = newRow.insertCell(2);
    var statusCell = newRow.insertCell(3);
    var locationCell = newRow.insertCell(4);
    var priorityCell = newRow.insertCell(5);
    var departmentCell = newRow.insertCell(6);
    var dateCell = newRow.insertCell(7);

    //works on cells
    var empIdCell = newRowWorksOn.insertCell(0);
    var ticketNumWorksOnCell = newRowWorksOn.insertCell(1);
    var hoursCell = newRowWorksOn.insertCell(2);

    // Add values to new row cells
    nameCell.innerHTML = name;
    idCell.innerHTML = id;
    employeeCell.innerHTML = employee;
    statusCell.innerHTML = status;
    locationCell.innerHTML = ticketLocation;
    priorityCell.innerHTML = priorityNumber;
    departmentCell.innerHTML = departmentNumber;
    dateCell.innerHTML = formattedDate;

    //add values to new work on cell
    empIdCell.innerHTML = name;
    ticketNumWorksOnCell.innerHTML = id;
    hoursCell.innerHTML = hours;

    // Clear form inputs
    document.getElementById("ticketName").value = "";
    document.getElementById("ticketID").value = "";
    document.getElementById("assignedEmployee").value = "";
    document.getElementById("ticketStatus").value = "";
    document.getElementById("ticketLocation").value = "";
    document.getElementById("priorityNumber").value = "";
    document.getElementById("departmentNumber").value = "";
    document.getElementById("hours").value = "";
}



function updateTicket(event) {
    event.preventDefault(); // prevent default form submission behavior

    //get inputs
    var id = document.getElementById("ticketIDLookupChange").value;
    var status = document.getElementById("ticketStatusChange").value;

    var table = document.getElementById("ticketTable");

    //clear inputs
    document.getElementById("ticketIDLookupChange").value = "";
    document.getElementById("ticketStatusChange").value = "";

    // iterate through each row in the table
    for (var i = 1; i < table.rows.length; i++) {
        var row = table.rows[i];
        // check if the id in the row matches the input id
        if (row.cells[1].innerHTML === id) {
            // if the id matches, update the status column with the new value
            row.cells[3].innerHTML = status;
        }
    }
}

function update_assigned_employee(event) {
    event.preventDefault(); // prevent default form submission behavior

    //get inputs
    var id = document.getElementById("ticketIDLookupEmp").value;
    var employee = document.getElementById("assignedEmployeeChange").value;

    var table = document.getElementById("ticketTable");
    var empTable = document.getElementById("EmployeeTable");

    //clear inputs
    document.getElementById("ticketIDLookupEmp").value = "";
    document.getElementById("assignedEmployeeChange").value = "";

    // iterate through each row in the table
    for (var i = 1; i < table.rows.length; i++) {
        var row = table.rows[i];
        // check if the id in the row matches the input id
        if (row.cells[1].innerHTML === id) {
            // if the ticket id matches, update the employee id column with the new value
            row.cells[2].innerHTML = employee;
        }

    }
}
document.addEventListener("DOMContentLoaded", () => {
    const tableSelect = document.getElementById("search-table");
    const columnSelect = document.getElementById("column-name");
    addOptions(["employeeName", "ID", "SSN", "SEX", "StartDate", "Address", "departmentNumber", "Salary", "birthday"]);
    tableSelect.addEventListener("change", () => {
        if (!columnSelect) {
            console.error("columnSelect is null");
            return;
        }
        const selectedTable = tableSelect.value;
        columnSelect.innerHTML = "";
        switch (selectedTable) {
            case "Employee":
                addOptions(["employeeName", "ID", "SSN", "SEX", "StartDate", "Address", "departmentNumber", "Salary", "birthday"]);
                break;
            case "Tickets":
                addOptions(["ticketName", "ticketNumber", "assignedEmployee", "ticketStatus", "ticketLocation", "priorityNumber", "departmentNumber", "createdDate"]);
                break;
            case "department":
                addOptions(["departmentName", "departmentNumber", "mgrSSN", "numEmployees"]);
                break;
            case "department_locations":
                addOptions(["departmentNumber", "departmentLocation"]);
                break;
            case "works_on":
                addOptions(["employeeSSN", "ticketNumber", "HOURS"]);
                break;
            case "dependent":
                addOptions(["employeeSSN", "dependentName", "SEX", "Birthday", "Relationship"]);
                break;
            default:
                break;
        }
    });

    function addOptions(options) {
        if (!columnSelect) {
            console.error('columnSelect is null');
            return;
        }
        options.forEach(option => {
            const newOption = document.createElement("option");
            newOption.value = option;
            newOption.text = option;
            columnSelect.add(newOption);
        });
    }
});