# data-base 
# Library Management System

## Description
This project implements a **Library Management System** using **MySQL** and **FastAPI** for creating a CRUD API. The system allows you to manage books, members, and loans in a library. It tracks which books are borrowed by which members, the loan dates, and the return dates.

## Project Features
- **MySQL Database** to store books, members, and loan data.
- **FastAPI** for a RESTful CRUD API to interact with the database.
- Create, read, update, and delete operations on books and members.

## How to Run/Setup the Project

### Setup MySQL Database

1. Ensure that you have MySQL installed on your machine.
2. Open MySQL Workbench or another MySQL client and run the `library_management.sql` script to create the database and tables.
3. Insert the sample data provided in the SQL file.

### Install Dependencies

1. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # For macOS/Linux
   venv\Scripts\activate      # For Windows
   
#### 2. **`library_management.sql`**

This file will contain your database schema and sample data.

```sql
-- Library Management System Database Schema

-- Creating Books Table
CREATE TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY,  -- Primary Key
    Title VARCHAR(255) NOT NULL,            -- Book title
    Author VARCHAR(100) NOT NULL,           -- Author's name
    ISBN VARCHAR(20) UNIQUE,                -- Unique ISBN for each book
    PublishedYear INT,                      -- Year of publication
    Genre VARCHAR(50)                       -- Genre of the book
);

-- Creating Members Table
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY, -- Primary Key
    FirstName VARCHAR(100) NOT NULL,         -- Member's first name
    LastName VARCHAR(100) NOT NULL,          -- Member's last name
    Email VARCHAR(100) UNIQUE,               -- Unique email address
    PhoneNumber VARCHAR(15),                 -- Contact number
    MembershipDate DATE NOT NULL             -- Date of membership
);

-- Creating Loans Table (many-to-many relationship between Books and Members)
CREATE TABLE Loans (
    LoanID INT AUTO_INCREMENT PRIMARY KEY,   -- Primary Key
    BookID INT,                               -- Foreign Key referencing Books
    MemberID INT,                             -- Foreign Key referencing Members
    LoanDate DATE NOT NULL,                   -- Date the book was borrowed
    ReturnDate DATE,                          -- Date the book was returned
    FOREIGN KEY (BookID) REFERENCES Books(BookID) ON DELETE CASCADE,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE
);

-- Sample Data Insertion

-- Inserting Books
INSERT INTO Books (Title, Author, ISBN, PublishedYear, Genre)
VALUES 
('The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565', 1925, 'Fiction'),
('1984', 'George Orwell', '9780451524935', 1949, 'Dystopian'),
('To Kill a Mockingbird', 'Harper Lee', '9780061120084', 1960, 'Fiction');

-- Inserting Members
INSERT INTO Members (FirstName, LastName, Email, PhoneNumber, MembershipDate)
VALUES 
('John', 'Doe', 'john.doe@example.com', '555-1234', '2021-01-15'),
('Jane', 'Smith', 'jane.smith@example.com', '555-5678', '2022-05-22'),
('Emily', 'Clark', 'emily.clark@example.com', '555-8765', '2021-09-30');

-- Inserting Loans
INSERT INTO Loans (BookID, MemberID, LoanDate, ReturnDate)
VALUES 
(1, 1, '2023-04-10', '2023-04-20'),
(2, 2, '2023-04-12', '2023-04-22'),
(3, 3, '2023-04-15', NULL);

