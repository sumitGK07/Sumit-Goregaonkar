# ====================================================================
# INVENTORY MANAGEMENT SYSTEM
# CREATED BY SUMIT GOREGAONKAR
# ====================================================================

DATA_FILE = "inventory.txt"

def initialize_database():
    """Creates the data file if it does not exist yet."""
    try:
        with open(DATA_FILE, "a") as file:
            pass  # Just ensure file exists without overwriting contents
    except IOError:
        print("Database connection error.")

def sync_inventory_sets():
    """
    Reads the file and uses Sets to extract distinct categories 
    and track out-of-stock items in real-time.
    """
    all_categories = set()
    out_of_stock_items = set()

    with open(DATA_FILE, "r") as file:
        for line in file:
            if line.strip():
                # Split comma-separated string records
                item_id, name, category, quantity, price = line.strip().split(",")
                
                # Add to unique categories set
                all_categories.add(category)
                
                # Check condition to manage out-of-stock set
                if int(quantity) == 0:
                    out_of_stock_items.add(name)
                    
    return all_categories, out_of_stock_items

# ====================================================================
# MAIN APPLICATION LOOP
# ====================================================================
initialize_database()

while True:
    # Build up-to-date analysis sets from the text file base
    categories_set, out_of_stock_set = sync_inventory_sets()

    print("\n" + "=" * 50)
    print("           INVENTORY MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add New Item to Inventory")
    print("2. View Complete Inventory File")
    print("3. Restock / Update Item Quantity")
    print("4. View Unique Product Categories (Set)")
    print("5. View Out-of-Stock Alerts (Set)")
    print("6. Exit")
    print("=" * 50)

    choice = input("Enter option (1-6): ").strip()

    # ----------------------------------------------------------------
    # 1. ADD NEW ITEM (Append to File)
    # ----------------------------------------------------------------
    if choice == "1":
        print("\n--- Add New Inventory Item ---")
        item_id = input("Enter Item ID (e.g., P100): ").strip().upper()
        
        # Check if ID already exists to prevent duplicates
        id_exists = False
        with open(DATA_FILE, "r") as file:
            for line in file:
                if line.startswith(item_id + ","):
                    id_exists = True
                    break
        
        if id_exists:
            print("❌ Error: An item with this ID already exists.")
            continue

        name = input("Enter Item Name: ").strip().title()
        category = input("Enter Category: ").strip().title()
        
        try:
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Unit Price ($): "))
            
            if quantity < 0 or price < 0:
                print("❌ Values cannot be negative.")
                continue

            # File Handling: Appending data line by line
            with open(DATA_FILE, "a") as file:
                file.write(f"{item_id},{name},{category},{quantity},{price:.2f}\n")
            
            print(f"✔️ Success: '{name}' recorded to file storage.")

        except ValueError:
            print("❌ Invalid type conversion. Quantity must be int, Price must be float.")

    # ----------------------------------------------------------------
    # 2. VIEW ALL INVENTORY (Read from File)
    # ----------------------------------------------------------------
    elif choice == "2":
        print("\n--- Current Inventory Database ---")
        
        with open(DATA_FILE, "r") as file:
            lines = file.readlines()
            
        if not lines:
            print("The inventory file database is completely empty.")
        else:
            print(f"{'ID':<8} | {'Item Name':<18} | {'Category':<15} | {'Qty':<5} | {'Price'}")
            print("-" * 60)
            for line in lines:
                if line.strip():
                    item_id, name, category, quantity, price = line.strip().split(",")
                    print(f"{item_id:<8} | {name:<18} | {category:<15} | {quantity:<5} | ${price}")
            print("-" * 60)

    # ----------------------------------------------------------------
    # 3. RESTOCK / UPDATE ITEM (Read & Rewrite File)
    # ----------------------------------------------------------------
    elif choice == "3":
        print("\n--- Update Stock Quantity ---")
        search_id = input("Enter Item ID to modify: ").strip().upper()
        
        updated_lines = []
        found = False

        with open(DATA_FILE, "r") as file:
            for line in file:
                if line.strip():
                    item_id, name, category, quantity, price = line.strip().split(",")
                    if item_id == search_id:
                        found = True
                        try:
                            new_qty = int(input(f"Current stock is {quantity}. Enter new quantity: "))
                            if new_qty < 0:
                                print("❌ Stock cannot be negative.")
                                new_qty = quantity # Revert
                            else:
                                quantity = str(new_qty)
                                print("✔️ Quantity updated successfully.")
                        except ValueError:
                            print("❌ Invalid input. Stock unchanged.")
                    
                    # Store line whether modified or not
                    updated_lines.append(f"{item_id},{name},{category},{quantity},{price}\n")

        if found:
            # File Handling: Overwrite mode ("w") to flush changes to disk
            with open(DATA_FILE, "w") as file:
                file.writelines(updated_lines)
        else:
            print("❌ Item ID not found.")

    # ----------------------------------------------------------------
    # 4. VIEW UNIQUE CATEGORIES (Set Operation)
    # ----------------------------------------------------------------
    elif choice == "4":
        print("\n--- Distribution Departments ---")
        if not categories_set:
            print("No categories recorded yet.")
        else:
            print(f"Total Unique Departments: {len(categories_set)}")
            print("-" * 35)
            # Iterating cleanly sorted set
            for index, cat in enumerate(sorted(categories_set), start=1):
                print(f"{index}. {cat}")

    # ----------------------------------------------------------------
    # 5. VIEW OUT-OF-STOCK ALERTS (Set Operation)
    # ----------------------------------------------------------------
    elif choice == "5":
        print("\n--- Critical Refill Alerts ---")
        if not out_of_stock_set:
            print("🎉 Excellent! All cataloged items are safely in stock.")
        else:
            print(f"⚠️ ALERT: {len(out_of_stock_set)} item(s) are completely depleted!")
            print("-" * 45)
            for item in out_of_stock_set:
                print(f"• REFILL NEEDED: {item}")

    # ----------------------------------------------------------------
    # 6. EXIT
    # ----------------------------------------------------------------
    elif choice == "6":
        print("\nClosing core database stream. Data safely synced to disk!")
        break

    else:
        print("❌ Selection error. Type an active integer option choice (1-6).")