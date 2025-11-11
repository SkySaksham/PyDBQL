PyDBQL — A Lightweight Database CLI in Python
=============================================

PyDBQL (Python Database Query Language) is a custom-built command-line interface designed to simulate database operations using simple commands. It allows you to create, manage, and interact with databases stored in plain text — all through your own SQL-like syntax.

------------------------------------------------------------
Features
------------------------------------------------------------
- Command-line based mini query language
- Create, drop, and view databases easily
- Fetch and display tables dynamically
- Works entirely on local files
- Interactive prompt:

  PyDBQL>>

------------------------------------------------------------
Commands Supported
------------------------------------------------------------
Command                                | Example
-------------------------------------- | -----------------------------
checkout :<database_name>              | checkout :students
checkout                               | (shows current database)
create :database :<name>               | create :database :library
drop :database :<name>                 | drop :database :testdb
show :database                         | show :database
get :<table_name>                      | get :students
get :<table_name> :where :<column> :is :<value> | get :students :where :class :is :12A

------------------------------------------------------------
Project Structure
------------------------------------------------------------
PyDBQL/
├── db/                   (Database folders and files)
├── src/                  (Source code modules)
│   ├── parser.py
│   ├── add_data.py
│   ├── create_table.py
│   ├── draw_table.py
│   └── drop_and_create_db.py
├── main.py               (CLI entry point)
├── pydbql.bat            (Windows launcher)
└── README.md             (Documentation)

------------------------------------------------------------
How to Run
------------------------------------------------------------
Option 1 — From the project folder
    cd C:\Users\Saksham Yadav\Desktop\Projects\PyDBQL
    python main.py

Option 2 — From anywhere (recommended)
    pydbql

------------------------------------------------------------
Example Session
------------------------------------------------------------
PyDBQL>> create :database :school
        DATABASE 'school' CREATED SUCCESSFULLY

PyDBQL>> checkout :school
        SELECTED DATABASE : school

PyDBQL>> show :database
+------+-----------+----------+
| S.no | Database  | Selected |
+------+-----------+----------+
| 1    | school    | TRUE     |
+------+-----------+----------+

------------------------------------------------------------
Requirements
------------------------------------------------------------
- Python 3.8 or higher
- Works on Windows (CLI compatible via pydbql.bat)

------------------------------------------------------------
Future Plans
------------------------------------------------------------
- Add insert, update, and delete commands
- Support nested query operations
- Add JSON and CSV export options
- Build a cross-platform launcher (Linux/Mac)

