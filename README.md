# PyDBQL — Python-Based Encrypted Database & Query Language

PyDBQL is a lightweight, file-based encrypted database engine written in Python.  
It supports creating databases, creating tables, inserting records, viewing data,  
and running simple queries with a custom human-readable query language.

---

## 🚀 Features

- 🔐 Encrypted data storage (via `encrypt_decrypt.py`)
- 📁 Create, drop, and switch databases
- 🧱 Create tables with typed columns, sizes, and keys
- ➕ Insert rows into tables
- 🔍 Retrieve tables with optional filtering (`WHERE <column> IS <value>`)
- 📜 Display all databases and all tables
- 💻 Interactive command shell: `PyDBQL>>`

---

## 📘 Supported Commands

### **1. Database Commands**
```
checkout
checkout :<database_name>
create :database :<database_name>
drop :database :<database_name>
show :databases
```

### **2. Table Commands**
```
show :tables
show :table :<table_name>
get :<table_name>
get :<table_name> :where :<column> :is :<entry>
create :table :<name> :(<col:type[size]; ...>)
insert :<table_name> :(<entry1> ;<entry2> ;...)
```

### Example — Create a Table
```
create :table :users :(id:key int; name:str[30]; age:int)
```

---

## 📁 Project Structure

```
src/
    add_data.py
    create_table.py
    draw_table.py
    drop_and_create_db.py
    encrypt_decrypt.py

db/
    (Encrypted databases stored here)

main.py
README.md
```

---

## ▶️ How to Run

Run the main program:

```
python main.py
```

You will enter the interactive shell:

```
PyDBQL>>
```

---

## 🧪 Examples

### Create and switch to a database
```
create :database :college
checkout :college
```

### Create a table
```
create :table :students :(id:key int; name:str[20]; age:int)
```

### Insert data
```
insert :students :(101 ;"Saksham" ;19)
```

### View table
```
get :students
```

### Filter rows
```
get :students :where :name :is :"Saksham"
```

---

## 🔐 Encryption

Table metadata and row entries are stored in encrypted form.  
Encryption/decryption functions live inside:

```
src/encrypt_decrypt.py
```

---

## 🎯 Why PyDBQL?

- Learn how databases work internally  
- Custom query parsing + encryption + file handling  
- Perfect for portfolios and learning system design  
- Fully written in Python  

---

## 📄 License

MIT License (optional — add if needed)