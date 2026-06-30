# CLI Banking System

A command-line banking application designed to handle standard financial transactions, user authentication, and persistent data storage. 

## Core Features

* **Account Management:** Generates unique, randomized account numbers and enforces 4-digit PIN authentication for new users.
* **Transactions:** Processes deposits and withdrawals with real-time balance validation.
* **Persistent Storage:** Serializes user session data locally to `data.json` for state retention across application restarts.
* **Data Mutability:** Allows secure viewing, updating, and deletion of existing account records based on authentication checks.

## Technical Specifications

* **Language:** Python 3.x
* **Architecture:** Object-Oriented Programming (OOP)
* **Core Libraries:** `json`, `random`, `string`, `pathlib`
