# Python Developer Internship — Tasks

This repository contains Python internship tasks demonstrating file handling,
API communication, and full-stack web development with Flask.

---

## Task 1: File Handling, Automation & Exception Handling

**Folder:** `task1_file_handling/`

### Description
This script demonstrates reading and writing txt and csv files, automating
file operations (rename, move, delete), and handling errors using try-except
blocks.

### Features
- Read and write text and CSV files
- Automate file operations: rename, move, delete
- try-except used throughout for error handling
- Comments explaining each step's logic

### How to Run
```
cd task1_file_handling
python file_handling_automation.py
```

### Sample Output
```
---- STEP 1: Writing a text file ----
sample.txt created and written successfully.

---- STEP 2: Reading the text file back ----
Contents of sample.txt:
Hello, this is my first file!

---- STEP 6: Automating file operations ----
Renamed 'sample.txt' to 'renamed_sample.txt'.
Moved 'renamed_sample.txt' into the 'backup' folder.
Deleted 'data.csv'.

---- Script finished successfully ----
```

---

## Task 2: API Communication and JSON Handling

**Folder:** `task2_api_json/`

### Description
This script demonstrates how Python communicates with external APIs and
handles JSON data. It uses the `requests` library to fetch data from the
JSONPlaceholder public API, parses the JSON response, applies filtering
logic, and handles API errors using try-except.

### Features
- Fetch data using the `requests` library
- Parse JSON responses into Python objects
- Apply filtering/search logic on the data
- Handle API errors (HTTP errors, connection errors, timeouts)

### How to Run
```
cd task2_api_json
pip install requests
python api_task.py
```

### Sample Output
```
Status Code: 200
Name: Leanne Graham
City: Gwenborough

--- Filtered Users (city contains 'view') ---
Chelsey Dietrich - Roscoeview
Nicholas Runolfsdottir V - Aliyaview

--- Testing Error Handling ---
HTTP Error occurred: 404 Client Error: Not Found for url: ...
```

---

## Task 3: Web Application — Task Scheduler (Flask)

**Folder:** `task3_flask_scheduler/`

### Description
A full-stack Task Scheduler web app built with Flask. Demonstrates Flask
routing, Jinja2 templates, GET/POST form handling, and complete CRUD
(Create, Read, Update, Delete) operations. Tasks include a title, category,
due date, and priority level, and are stored persistently in a JSON file.
Overdue tasks are automatically highlighted. The UI uses Bootstrap with
custom styling.

### Features
- Flask routing and templates (5 routes: home, add, edit, toggle, delete)
- Form handling using both GET and POST
- Full CRUD with persistent JSON file storage
- Clean, responsive UI built with Bootstrap + custom CSS

### How to Run
```
cd task3_flask_scheduler
pip install flask
python app.py
```
Then open `http://127.0.0.1:5000` in your browser.

### Project Structure
```
task3_flask_scheduler/
├── app.py
├── tasks.json       
└── templates/
    ├── base.html
    ├── index.html
    ├── add.html
    └── edit.html
```

---
## Author
Rajshree Potphode
Intern — Python Developer(Alfido Tech)

