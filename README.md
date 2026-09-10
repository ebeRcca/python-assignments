# Python Assignments – Staff Requisition System

This repository contains two Python assignments completed for IT7522 Software Development Fundamentals.  
Both assignments are based on developing a prototype Staff Requisition System that allows staff to submit purchase requisitions and receive an approval status.

---

## Part A – Function-Based Requisition System

This version uses Python functions to build the basic requisition workflow.

### Functions implemented:
- staff_info() – collects staff details and generates a unique requisition ID  
- requisitions_total() – collects item names and prices and calculates the total  
- requisition_approval() – applies approval rules based on the total  
- display_requisitions() – prints all requisition information  

The system automatically approves requisitions under $500 and sets others to pending.

---

## Part B – Object-Oriented Requisition System

This version converts the system into a class-based design using OOP principles.

### Class: RequisitionSystem

### Methods implemented:
- staff_info() – collects staff details  
- requisitions_details() – calculates total item cost  
- requisition_approval() – applies approval rules and updates status  
- respond_requisition() – manager updates pending requisitions  
- display_requisitions() – prints all requisition objects  
- requisition_statistic() – shows counts of approved, pending, and not approved requisitions  

At least five requisitions were created to test different scenarios (totals below and above $500).

---

## Repository Structure
- partA
- partB
- README

---

This repository demonstrates both functional and OOP approaches to building a Staff Requisition System.

