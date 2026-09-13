# Scenario: Requisition System Prototype

# TASK 1: Collects staff details and generates a unique ID for each requisition.

# Counter is set to generate the requisition ID.
# Starts at 10001 for the first requisition as specified in the sample output. 
# Each time the function runs, the counter increases to give the next unique ID.
counter = 10001

def staff_info():
     
    print("------------------------------")
    # Adds a separator line between each requisition.

    global counter  
    # The counter is global to remember its value every time the function runs.
    # Allows each new requisition to get a unique ID instead of resetting.

    # Asks user for staff information
    date = input("Enter date (DD/MM/YYYY): ")
    staff_id = input("Enter Staff ID: ")
    staff_name = input("Enter Staff Name: ")

    requisition_id = counter
    counter += 1  # Counter = counter + 1 -> increases the counter by 1 for the next requisition.

    # Displays the staff information in the correct format.
    print("\nStaff Information:")
    print("Date:", date)
    print("Staff ID:", staff_id)
    print("Staff Name:", staff_name)
    print("Requisition ID:", requisition_id, "\n")

    # Returns all values for the following task.
    return date, staff_id, staff_name, requisition_id


# TASK 2: Collects item prices + calculates total cost of requisition.

def requisitions_total():

    # Calls staff_info() so the values can be used in this function.
    date, staff_id, staff_name, requisition_id = staff_info()

    # Instructs user for requisition input.
    print("Enter items, including name and price.")
    print("Press Enter without an item name to finish.\n")

    total = 0  # Running total starts at 0.

    # Creates a loop to add multiple items.
    while True:
        item = input("Item name: ")
        if item == "":  # Empty input ends the loop.
            break

        # Converts price to float for decimal and adds to running total.
        price = float(input(f"Price for {item}: $"))
        total += price  # Total = total + price -> each item is added to the running total.

    # Displays the final total cost with 2 decimal places for currency.
    print(f"Total Cost: ${total:.2f}")

    # Returns all values for following task.
    return date, staff_id, staff_name, requisition_id, total


# TASK 3: Makes approval decision based on total cost.

def requisition_approval():

   # Calls requisitions_total() so the values can be used in this function (includes values from staff_info()).
    date, staff_id, staff_name, requisition_id, total = requisitions_total()

    status = "Pending"  # Sets the default status for all requisitions
    approval_ref = ""   # Empty unless approved

    # Approval condition: under $500 = approved
    if total < 500:
        status = "Approved"
        approval_ref = staff_id + str(requisition_id)[-3:]
        # Creates approval reference using staff_id + last 3 digits of requisition_id.
        # requisition_id is created as an integer in staff_info(), but integers can't be sliced (to take part of it) like strings.
        # approval_ref is converted to a string here to extract the last 3 digits.

    # Displays approval status
    print(f"Status: {status}")

    # approval_reference only generated if requisition is approved.
    if approval_ref != "":
        print(f"Approval Reference Number: {approval_ref}")

    # Returns all values for following task.
    return date, staff_id, staff_name, requisition_id, total, status, approval_ref


# TASK 4: Displays requisition summary.

# Task 4 receives all final values as parameters so the function can use them when printing the requisition details.
def display_requisitions(date, requisition_id, staff_id, staff_name, total, status, approval_ref):
    print("\nPrinting Requisitions:")
    print(f"Date: {date}")
    print(f"Requisition ID: {requisition_id}")
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name: {staff_name}")
    print(f"Total: ${total:.2f}")
    print(f"Status: {status}")

    if approval_ref != "": 
        print(f"Approval Reference Number: {approval_ref}")
        # If there was an approval reference number generated, it is printed.


# RUN ALL TASKS TOGETHER

# Calls requisition_approval() and provide the variables that will receive its returned values.
# The function is on the right because it returns the values for these variables.
date, staff_id, staff_name, requisition_id, total, status, approval_ref = requisition_approval()

# Calls display_requisitions() with the arguments it needs to print the requisition details.
display_requisitions(date, requisition_id, staff_id, staff_name, total, status, approval_ref)


# Copy and paste following lines to run the requisition process multiple times.
# Demonstrates that each new requisition receives a unique ID.
date, staff_id, staff_name, requisition_id, total, status, approval_ref = requisition_approval()
display_requisitions(date, requisition_id, staff_id, staff_name, total, status, approval_ref)




