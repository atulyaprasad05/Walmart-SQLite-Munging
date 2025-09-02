# 🧾 Walmart-SQLite-Munging — Personal Project

This project demonstrates my ability to extract, transform, and load (ETL) shipping data from multiple spreadsheets into a normalized SQLite database. It simulates a real-world logistics scenario, showcasing my skills in Python scripting, data wrangling, and schema-aware data insertion.

# 📌 Purpose

This project reflects how I approach:

- 🧠 Problem decomposition and edge-case reasoning  
- 🛠️ Clean, reproducible environment setup  
- 📊 Data normalization and relational integrity  
- 🤝 Clear documentation and maintainable code  

# 🚀 How It Works
The script populate_database.py performs the following:
- Reads spreadsheet 0 and inserts each row directly into the database.
- Processes spreadsheets 1 & 2:
  - Groups products by shipment_identifier.
  - Counts product quantities per shipment.
  - Retrieves origin/destination from spreadsheet 2.
  - Inserts each product shipment into the database.
All data is assumed to be clean and consistent (e.g., standardized product names, valid quantities).

# 🧪 Example Output
Table: product  
Columns: ['id', 'name']  
Rows:  
(1, 'Widget A')  
(2, 'Gadget B')  

Table: shipment  
Columns: ['id', 'origin', 'destination', 'product_id', 'quantity']  
Rows:  
(1, 'Warehouse 1', 'Store 5', 1, 3)  

# 🧼 Environment Setup
To run the script:  
pip install pandas  
python populate_database.py  

# 🧠 Reflections
This project gave me a chance to:
- Practice schema-aware data insertion
- Handle multi-source data dependencies
- Write beginner-friendly, maintainable code
- Think through edge cases and relational logic