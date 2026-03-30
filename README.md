# ATM System - OOP Flow Diagram

## 📌 Overview

This project represents the **Object-Oriented Programming (OOP)** design of an ATM (Automated Teller Machine) system using a flow diagram.

It demonstrates how core OOP principles like **Encapsulation, Abstraction, Inheritance, and Polymorphism** are applied in a real-world system.

---

## Objectives

* Understand OOP concepts using a practical example
* Visualize system design using flow diagrams
* Represent ATM operations in a structured way

---

##  OOP Concepts Used

###  Encapsulation

* Sensitive data like **PIN** and **balance** are hidden inside the `Account` class
* Access is controlled through methods like `validatePIN()` and `getBalance()`

---

### Abstraction

* The ATM interface shows only necessary options:

  * Withdraw Cash
  * Check Balance
  * Deposit Money
* Internal implementation is hidden from the user

---

### Inheritance

* A base class `Transaction` is extended by:

  * `Withdraw`
  * `Deposit`
  * `CheckBalance`

---

### Polymorphism

* A common method like `execute()` behaves differently depending on the transaction type

---

##  System Components (Classes)

* **ATM**
* **User**
* **Card**
* **Account**
* **Transaction**

---

## Flow of the System

1. Start
2. Insert Card
3. Enter PIN
4. Validate PIN

   * If invalid → Retry
   * If valid → Continue
5. Show Menu
6. Select Transaction
7. Process Transaction
8. Display Result
9. End

---

## Flow Diagram

<img width="1217" height="568" alt="Oops 1" src="https://github.com/user-attachments/assets/8803c226-b678-4802-ad0e-2af43968dce0" />

 Open the diagram here:
https://excalidraw.com/#json=XxS2HUP5E1HLvasiGfXzA,3eJSUVjU197zv-vrZ4JgTQ

---

## 🛠️ Tools Used

* Excalidraw (for diagram creation)

---

##  How to Use

1. Open the diagram link
2. Study the flow and class relationships
3. Use it as a reference for learning OOP design

---


