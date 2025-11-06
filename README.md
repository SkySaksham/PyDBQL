# PyDBQL — Python Based DataBase & Query Language
##  - Encrypted Local Database Engine (Work in Progress)

**PyDBQL** is a lightweight, local, file-based database engine built from scratch in Python.
It features a terminal user interface (TUI), encrypted storage, and a custom mini query language for managing tables.

> ⚠️ **Work in Progress:** The project structure, database format, and features may change as development continues.
> The repository currently contains sample database files for testing only.

---

## 🚀 Features (Planned / In Development)

* **Encrypted Storage:** Password-protected databases using key wrapping and PBKDF2.
* **Custom Query Language:** Basic commands like `SELECT`, `INSERT`, and `DELETE`.
* **Terminal UI:** ASCII table display and interactive table navigation.
* **Python Library Mode:** Can be imported and used as a Python module.
* **Folder-Based Storage:** Each database has its own folder with tables stored in binary format.

---

## 📂 Current Structure

```
PyCQL/
├── main.py                # Current implementation & testing
├── Sky/                   # Example database folder
│   ├── tables.txt         # Table list
│   └── tables/
│       └── student.txt    # Sample table
```

*(This structure will be updated as the engine matures.)*

---


## 🔒 Notes

* This repo contains **example databases only**.
* Real encryption & security features are under development.
* Contributions are welcome once core features are stabilized.
