import sqlite3  # used for inserting and reading the database
import pandas as pd  # used for reading the csv files


df = pd.read_csv("data/shipping_data_0.csv")  # for sheet 0
conn = sqlite3.connect("shipment_database.db") # Connect to your SQLite database
cursor = conn.cursor()  # Create a cursor object to interact with the database


for index, row in df.iterrows():  # for sheet 0
    lst = []
    for col_name in["origin_warehouse","destination_store","product","product_quantity"]:
        lst.append(row[col_name])

    # inseting prduct into the product table if it doesn't exist, and getting its id
    cursor.execute("SELECT id FROM product WHERE name = ?", (lst[2],))
    result = cursor.fetchone()  # Fetch one record

    if result:  # if product exists
        product_id = result[0]
    else:  # product doesnt exist
        # Insert new product
        cursor.execute("INSERT INTO product (name) VALUES (?)", (lst[2],))
        product_id = cursor.lastrowid


    cursor.execute(f"INSERT INTO shipment (origin, destination, product_id, quantity) VALUES (?, ?, ?, ?)", (lst[0], lst[1], product_id, lst[3]))

del df # delete sheet 0, since i am done


df1 = pd.read_csv("data/shipping_data_1.csv")  # working with sheet 1
df2 = pd.read_csv("data/shipping_data_2.csv")  # working with sheet 2


for index,row in df2.iterrows():  # for sheet 2
    lst = []
    count = {}
    lst.append(row["shipment_identifier"])
    lst.append(row["origin_warehouse"])
    lst.append(row["destination_store"])

    filtered = df1[df1['shipment_identifier'] == lst[0]]  # where rows have the same shipping id

    for i,row in filtered.iterrows():
        if row["product"] in count:
            count[row["product"]] += 1
        else:
            count[row["product"]] = 1

    for key,value in count.items():

        # inserting product into the product table if it doesn't exist, and getting its id
        cursor.execute("SELECT id FROM product WHERE name = ?", (key,))
        result = cursor.fetchone()

        if result:  # if product exists
            product_id = result[0]
        else:  # product doesnt exist
            # Step 2: Insert new product
            cursor.execute("INSERT INTO product (name) VALUES (?)", (key,))
            product_id = cursor.lastrowid


        cursor.execute(f"INSERT INTO shipment (origin, destination, product_id, quantity) VALUES (?, ?, ?, ?)", (lst[1], lst[2], product_id, value))


# testing by printing the db

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [table[0] for table in cursor.fetchall()]

# Loop through each table and print columns + rows
for table_name in tables:
    print(f"\nTable: {table_name}")

    # Get column names
    cursor.execute(f"PRAGMA table_info({table_name})")  # Get column info
    columns = [col[1] for col in cursor.fetchall()]
    print("Columns:", columns)


    # Get all rows
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    print("Rows:")
    for row in rows:
        print(row)

conn.close()  # Close connection
