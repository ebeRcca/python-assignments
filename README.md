# Requisition System Prototype

## Overview
This repository contains a prototype of a simple staff requisition system developed in two parts:

- Part A: functional (procedural) stage  
- Part B: object-oriented (OOP) stage  

Each part implements the requisition workflow using a different software design approach. 

---

## Part A — Functional stage

**File:** `requisition_system_part_a.py`

The functional stage uses stand-alone functions that each perform one part of the workflow. Each function returns the values needed for the next step, so the requisition is built using local variables passed through the function chain.

### Key Features
- Collect staff information
- Generate a unique requisition ID
- Enter items and calculate totals
- Automatically approve requisitions under $500
- Display requisition details    

### How Part A Works
- A global counter generates unique requisition IDs
- Each function performs one part of the workflow
- Returned values are passed to the next function
- The requisition is processed step‑by‑step using local variables

---

## Part B — Object-Oriented Version

**File:** `requisition_system_part_b.py`

The OOP stage restructures the system using a single class that stores requisition information and provides methods to manage it.

### Key Features
- Store requisition details inside an object
- Collect staff information
- Record multiple items and calculate totals
- Apply automatic approval
- Process manager decisions
- Display requisition details
- Generate statistics across multiple requisitions

### How Part B Works
- Each requisition is represented by an object
- The object stores its own data (staff details, items, total, status, approval reference)
- Methods update the object step‑by‑step
- A list inside the object stores item/price pairs
- Multiple objects represent multiple requisitions
- A statistics method counts approved, pending, and not‑approved requisitions
  
---

## Software Design Principles Demonstrated

### Modularity
Part A separates the workflow into individual functions.
Part B uses one class where all methods relate to managing a requisition.
  
Both approaches break the system into smaller, manageable parts.

### Cohesion
Part A functions each perform related steps in the requisition process.
Part B’s class has high cohesion because all its methods contribute to the overall purpose of handling a requisition.
  
### Coupling
Part A shows low coupling because each function only receives the data it needs and does not rely on other functions' internal workings. The only shared element is the global counter, which is used solely for generating unique IDs.
Part B shows low coupling because the testing code interacts with the class only through method calls, so internal changes do not affect other parts of the program.
  
### Abstraction
Part A hides how data is stored by using simple functions that return values.
Part B hides internal details by storing requisition information inside the object and updating it through methods such as `staff_info()`, `requisitions_details()`, and `requisition_approval()`. 

### Encapsulation
Encapsulation applies only to Part B.
Part B stores requisition details inside the object and updates them only through methods. The program does not directly modify attributes such as status or total; each method manages its own part of the data. 

### KISS (Keep It Simple)
Both parts use straightforward logic and clear naming.
Part A uses simple functions.
Part B uses a single class with readable methods.

### Separation of Concerns
Part A separates tasks into individual functions.
Part B keeps all requisition‑related behaviour inside one class, while the testing code handles running scenarios and manager decisions.

### Reusability
Reusability applies only to Part B.
The RequisitionSystem class can be reused in other simple prototypes because it contains all the logic needed to store, approve, and display a requisition.

### DRY (Don’t Repeat Yourself)
Both parts avoid repeating logic by using functions (Part A) and methods (Part B) to handle repeated actions such as collecting staff information, calculating totals, approving requisitions, and displaying results. This reduces duplication and keeps the workflow consistent.

### Single Source of Truth
Both parts use a single counter to generate unique requisition IDs. This ensures that ID generation is consistent and prevents duplication or conflicting values across multiple requisitions.
