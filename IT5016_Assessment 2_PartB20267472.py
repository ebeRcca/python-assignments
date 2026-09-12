# Author: Rebecca Pene
# Date: 04/09/2026
# Description: Staff Requisition System Prototype

# TASK 1: Create a class called RequisitionSystem

# Global requisition counter used to generate a unique ID for each requisition
requisition_counter = 10000


class RequisitionSystem:

    def __init__(self):
        # Increments the global requisition counter by 1 to generate a unique ID
        global requisition_counter
        requisition_counter += 1

        # Sets the starting values for each requisition
        self.date = ""
        self.staff_id = ""
        self.staff_name = ""
        self.requisition_id = requisition_counter
        self.items = []  # Creates an empty list to store items and prices
        self.total = 0  # Stores running total of items 

        # Sets the initial status of the requisition to 'Pending'
        self.status = "Pending"
        # The approval reference is set at 'Not available' until the requisition is approved
        self.approval_ref = "Not available"


    # a. Staff information
    # ----------------------
    # Collects staff details for the requisition
    def staff_info(self):
        self.date = input("Enter date (DD/MM/YYYY): ")
        self.staff_id = input("Enter Staff ID: ")
        self.staff_name = input("Enter Staff Name: ")
        print()


    # b. Requisition details
    # ------------------------
    # Allows the user to enter multiple items and the prices
    def requisitions_details(self):
        # Instructs user for requisition item input
        print("Enter items, including name and price")
        print("Leave item name empty and press Enter to finish\n")

        # Creates a loop to add multiple items.
        while True:
            item = input("Item name: ")
            if item == "":   # Empty input ends the loop.
                break
            price = float(input(f"Price for {item}: $"))
            self.items.append((item, price))   # Stores the item and price
            self.total += price                # Adds the price to the running total


    # c. Automatic approval
    # -----------------------
    # Automatically approves requisitions under $500
    def requisition_approval(self):
        if self.total < 500:
            self.status = "Approved"

            # Generates an approval reference using staff ID + last 3 digits of requisition ID
            last_three = str(self.requisition_id)[-3:]
            self.approval_ref = f"{self.staff_id}{last_three}"

        else:
            # Requisitions ≥ $500 remain 'Pending'
            self.status = "Pending"
            self.approval_ref = "Not available"


    # d. Manager response
    # ---------------------
    # Updates the requisition status based on the manager's decision 
    def respond_requisition(self, decision):
        # Converts the manager's input to lowercase so the program accepts any case configuration
        decision = decision.lower()
        if decision == "approved":
            # Updates status to 'Approved' and generates an approval reference
            self.status = "Approved"
            last_three = str(self.requisition_id)[-3:]
            self.approval_ref = f"{self.staff_id}{last_three}"
        elif decision == "not approved":
            # Updates status to 'Not approved' and sets the approval reference to 'Not available'
            self.status = "Not approved"
            self.approval_ref = "Not available"


    # e. Display requisition
    # ------------------------
    # Prints all stored requisition details
    def display_requisitions(self):
        print("\nDate:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print(f"Total: ${self.total:.2f}")
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_ref)


    # f. Statistics 
    # ---------------
    # Calculates and displays counts of requisitions and the statuses
    def requisition_statistic(self, requisition_list):
        # Calculates the total number of requisitions submitted
        total = len(requisition_list)
        # Calculates the total number of approved requisitions
        approved = sum(r.status == "Approved" for r in requisition_list)
        # Calculates the total number of pending requisitions
        pending = sum(r.status == "Pending" for r in requisition_list)
        # Calculates the total number of not approved requisitions
        not_approved = sum(r.status == "Not approved" for r in requisition_list)

        # These counts automatically update because they are based on each requisition's status.
        # When a manager approves or does not approve a pending requisition:
        # - Pending decreases by 1
        # - Approved or Not approved increases by 1

        print("\nStatistics:")
        print("The total number of requisitions submitted:", total)
        print("The total number of approved requisitions:", approved)
        print("The total number of pending requisitions:", pending)
        print("The total number of not approved requisitions:", not_approved)


# --- Requisition Testing ---

# Creates 5 requisitions for input of different scenarios (e.g. totals < $500 and totals ≥ $500)
# Applies automatic approval, allows manager decisions, and displays statistics before and after.

print("\n=== Staff Requisition System Prototype Testing ===")

print("\n--- Requisitions ---")

print("\nRequisition 1:")
req1 = RequisitionSystem()
req1.staff_info()
req1.requisitions_details()
req1.requisition_approval()
req1.display_requisitions()

print("\n--------------------")

print("\nRequisition 2:")
req2 = RequisitionSystem()
req2.staff_info()
req2.requisitions_details()
req2.requisition_approval()
req2.display_requisitions()

print("\n--------------------")

print("\nRequisition 3:")
req3 = RequisitionSystem()
req3.staff_info()
req3.requisitions_details()
req3.requisition_approval()
req3.display_requisitions()

print("\n--------------------")

print("\nRequisition 4:")
req4 = RequisitionSystem()
req4.staff_info()
req4.requisitions_details()
req4.requisition_approval()
req4.display_requisitions()

print("\n--------------------")

print("\nRequisition 5:")
req5 = RequisitionSystem()
req5.staff_info()
req5.requisitions_details()
req5.requisition_approval()
req5.display_requisitions()

# Displays statistics BEFORE manager decisions
print("\n--- Statistics BEFORE Manager Decisions ---")
req1.requisition_statistic([req1, req2, req3, req4, req5])

# Manager decisions
print("\n--- Manager Decisions ---")
for req in [req1, req2, req3, req4, req5]:
    if req.status == "Pending":
        print(f"\nRequisition submitted by: {req.staff_name}")
        print("Requisition items:")
        for name, price in req.items:
            print(f"  - {name}: ${price:.2f}")

        print(f"Total cost: ${req.total:.2f}")
        decision = input(f"Enter approval decision for requisition {req.requisition_id} (approved/not approved): ")
        req.respond_requisition(decision)

# Displays updated requisitions AFTER manager decisions
print("\n--- Requisitions AFTER Manager Decisions ---")
req1.display_requisitions()
req2.display_requisitions()
req3.display_requisitions()
req4.display_requisitions()
req5.display_requisitions()

# Displays updated statistics AFTER manager decisions
print("\n--- Statistics AFTER Manager Decisions ---")
req1.requisition_statistic([req1, req2, req3, req4, req5])



