# Requisition System Prototype

## Overview
This repository contains a prototype of a simple staff requisition system developed in two parts:

- Part A: functional (procedural) stage  
- Part B: object-oriented (OOP) stage  

Each version implements the requisition workflow using a different software design approach. Part A uses a functional structure with stand‑alone functions, while Part B uses an object‑oriented class structure that also extends the workflow with additional features.

---

## Part A — Functional 

**File:** `requisition_system_part_a.py`

The functional version uses stand-alone functions that each perform one step of the workflow. Each function returns the values needed for the next step, so the requisition is built by passing local variables sequentially from one function to the next.

### Key Features
- Collects staff information
- Generates a unique requisition ID
- Collects items and prices then calculates the total
- Applies automatic approval for requisitions < $500
- Displays requisition details    

### How Part A Works
- A global `counter` generates a unique requisition ID
- Each function performs a specific step in the workflow
- Returned values are passed to the next function
- The requisition is processed step‑by‑step using local variables

---

## Part B — Object-Oriented

**File:** `requisition_system_part_b.py`

The OOP stage restructures the system using a single class that stores requisition information and provides methods to manage each step of the workflow.

### Key Features
- Stores requisition details inside an object
- Collects staff information
- Records items, prices and the calculated total
- Applies automatic approval for requisitions < $500
- Processes manager decisions
- Displays requisition details
- Generates statistics across multiple requisitions using `requisition_statistic()` 

### How Part B Works
- The object stores its own data (staff details, items, total, status, approval reference)
- A list inside the object stores item/price pairs in `items`
- Methods such as `staff_info()`, `requisitions_details()`, and `requisition_approval()` update the object step‑by‑step through the workflow
- Each object represents one requisition, and multiple objects allow the system to process multiple requisitions.
- A statistics method counts approved, pending, and not‑approved requisitions
  
---

## Purpose
The requisition system prototype was chosen to demonstrate how software design principles apply in both functional and object oriented programming approaches. Part A shows how a workflow can be built using small, single purpose functions, while Part B shows how the same workflow can be expanded and organised using a class that stores its own data and methods. Together, they highlight how design principles such as modularity, cohesion, abstraction, and encapsulation influence the structure and behaviour of a program.

---

## Software Design Principles Demonstrated

### Modularity
Part A separates the workflow into individual functions.
Part B uses one class where all methods relate to managing a requisition. 
Both approaches break the system into smaller, manageable parts.

### Cohesion
Part A has functional cohesion because each function performs one related step in the overall requisition workflow.
Part B’s class has high cohesion because every method contributes to the overall purpose of processing a requisition.
  
### Coupling
Part A shows low coupling because each function only receives the data it needs and does not depend on how other functions work. 
The only shared element is the global `counter`, which is used solely for generating a unique ID for each requisition.
Part B shows low coupling because the testing code interacts with the class only through calling its methods, so internal changes to the class do not affect other parts of the program.
  
### Abstraction
Part A uses abstraction because the functions hide how requisition data is collected and processed. The user only calls the functions and does not need to know how totals, approval, or staff details are handled internally.
Part B uses abstraction because it hides internal details by storing requisition information inside the object and updating it only through methods such as `staff_info()`, `requisitions_details()`, and `requisition_approval()`. 

### Encapsulation
Encapsulation applies only to Part B.
The class stores requisition details inside the object and updates them exclusively through its methods. The program does not directly modify attributes such as `status` or `total`; each method manages its own part of the data. 

### KISS (Keep It Simple)
Both parts follow the KISS principle by using straightforward logic and clear naming. 
Part A keeps the workflow simple by using small, focused functions. 
Part B keeps the design simple by using one class with easy‑to‑read methods that handle each step of the process.

### Separation of Concerns
Part A separates concerns by placing each step of the workflow into individual functions.
Part B separates concerns by keeping all requisition‑related logic inside one class, while the testing code is responsible for running scenarios and manager decisions.

### Reusability
Reusability applies mainly to Part B because the entire class can be imported and used in other similar programs. It stores its own data and provides methods that manage a requisition process.
Part A is less reusable because its functions rely on direct user input and are tied to a single specific workflow.

### DRY (Don’t Repeat Yourself)
Both parts follow the DRY principle by placing repeated actions into functions (Part A) and methods (Part B). Tasks such as collecting staff information, calculating totals, approving requisitions, and displaying results are written once and reused, which reduces duplication and keeps the workflow consistent.

### Single Source of Truth
Both parts follow the Single Source of Truth principle by using one counter to generate unique requisition IDs. This keeps the numbering consistent and prevents duplication or conflicting IDs across multiple requisitions.
