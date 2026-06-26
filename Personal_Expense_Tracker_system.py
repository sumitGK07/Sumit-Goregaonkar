# ====================================================================
# PERSONAL EXPENSE TRACKER
# CREATED BY SUMIT GOREGAONKAR
# ====================================================================

expenses = {
    1: {"amount": 567.00, "category": "Food", "tags": {"groceries", "supermarket"}},
    2: {"amount": 1200.00, "category": "Rent", "tags": {"housing", "fixed"}},
    3: {"amount": 150.00, "category": "Food", "tags": {"restaurant", "leisure"}},
    4: {"amount": 350.00, "category": "Utilities", "tags": {"electricity", "bills"}},
}

# Pre-populating unique categories using a Set
categories = {"Food", "Rent", "Utilities", "Entertainment", "Transport"}
monthly_budget = 3000.00
expense_id_counter = 5

# ====================================================================
# MAIN APPLICATION LOOP
# ====================================================================
while True:
    print("\n" + "=" * 45)
    print("          PERSONAL EXPENSE TRACKER")
    print("=" * 45)
    print("1. Add New Expense")
    print("2. View All Expenses & Budget Status")
    print("3. Categorized Expense Summary")
    print("4. Search Expenses by Tag")
    print("5. Delete an Expense")
    print("6. Update Monthly Budget")
    print("7. Exit")
    print("=" * 45)

    choice = input("Enter your choice (1-7): ").strip()

    # ----------------------------------------------------------------
    # 1. ADD NEW EXPENSE
    # ----------------------------------------------------------------
    if choice == "1":
        print("\n--- Add New Expense ---")
        try:
            amount = float(input("Enter expense amount ($): "))
            if amount <= 0:
                print("❌ Amount must be greater than zero.")
                continue
            
            category = input("Enter category (e.g., Food, Rent, Transport): ").strip().capitalize()
            # Adding category to our master Set dynamically
            categories.add(category)

            # Creating a Set for custom tags
            tags_input = input("Enter descriptive tags (comma-separated): ")
            # Loop + Set comprehension to strip spacing and clean tags
            tags_set = {tag.strip().lower() for tag in tags_input.split(",") if tag.strip()}

            # Storing structural data inside the nested dictionary
            expenses[expense_id_counter] = {
                "amount": amount,
                "category": category,
                "tags": tags_set
            }
            print(f"✔️ Added Expense ID {expense_id_counter} successfully!")
            expense_id_counter += 1 # Arithmetic increment

        except ValueError:
            print("❌ Invalid input. Please enter a valid number for amount.")

    # ----------------------------------------------------------------
    # 2. VIEW ALL EXPENSES & BUDGET STATUS (Arithmetic Totals)
    # ----------------------------------------------------------------
    elif choice == "2":
        print("\n--- Expense Inventory ---")
        if not expenses:
            print("No expense records found.")
        else:
            print(f"{'ID':<5} | {'Amount':<10} | {'Category':<15} | {'Tags'}")
            print("-" * 60)
            
            total_spent = 0.0 # Initial accumulator
            for exp_id, details in expenses.items():
                # Extracting Set elements into a readable string format
                tags_str = ", ".join(details["tags"])
                print(f"{exp_id:<5} | ${details['amount']:<9.2f} | {details['category']:<15} | {tags_str}")
                
                # Arithmetic addition
                total_spent += details["amount"]
            
            # Budget Arithmetic Calculations
            remaining_budget = monthly_budget - total_spent
            budget_used_percentage = (total_spent / monthly_budget) * 100

            print("-" * 60)
            print(f"Total Expenditure : ${total_spent:.2f}")
            print(f"Allocated Budget  : ${monthly_budget:.2f}")
            print(f"Remaining Balance : ${remaining_budget:.2f}")
            print(f"Budget Utilization: {budget_used_percentage:.1f}%")
            
            if remaining_budget < 0:
                print("⚠️ WARNING: You have exceeded your budget allocations!")

    # ----------------------------------------------------------------
    # 3. CATEGORIZED SUMMARY (Iterating Sets and Dicts)
    # ----------------------------------------------------------------
    elif choice == "3":
        print("\n--- Summary By Category ---")
        if not expenses:
            print("No expense records found.")
        else:
            # We iterate through our unique category Set to guarantee clean breakdowns
            for cat in sorted(categories):
                cat_total = 0.0
                for details in expenses.values():
                    if details["category"] == cat:
                        cat_total += details["amount"]
                
                # Only show categories that actually have money spent
                if cat_total > 0:
                    print(f"• {cat:<15}: ${cat_total:.2f}")

    # ----------------------------------------------------------------
    # 4. SEARCH EXPENSES BY TAG (Set Intersections/Membership)
    # ----------------------------------------------------------------
    elif choice == "4":
        print("\n--- Search by Tag ---")
        search_tag = input("Enter tag to filter by: ").strip().lower()
        found = False

        print(f"\n{'ID':<5} | {'Amount':<10} | {'Category':<15} | {'Tags'}")
        print("-" * 60)

        for exp_id, details in expenses.items():
            # Using Set membership execution ('in') to scan tags
            if search_tag in details["tags"]:
                tags_str = ", ".join(details["tags"])
                print(f"{exp_id:<5} | ${details['amount']:<9.2f} | {details['category']:<15} | {tags_str}")
                found = True
        
        if not found:
            print(f"No expenses found holding the tag '{search_tag}'.")

    # ----------------------------------------------------------------
    # 5. DELETE AN EXPENSE
    # ----------------------------------------------------------------
    elif choice == "5":
        print("\n--- Delete Expense Record ---")
        try:
            del_id = int(input("Enter Expense ID to delete: "))
            if del_id in expenses:
                removed_item = expenses.pop(del_id) # Deletes nested dictionary item
                print(f"✔️ Removed Expense ID {del_id} (${removed_item['amount']:.2f}) successfully.")
            else:
                print("❌ Expense ID not found.")
        except ValueError:
            print("❌ Invalid input. ID must be an integer.")

    # ----------------------------------------------------------------
    # 6. UPDATE MONTHLY BUDGET
    # ----------------------------------------------------------------
    elif choice == "6":
        print("\n--- Adjust Allocation Baseline ---")
        try:
            new_budget = float(input(f"Current budget is ${monthly_budget:.2f}. Enter new budget: $"))
            if new_budget > 0:
                monthly_budget = new_budget
                print("✔️ Budget ceiling updated successfully.")
            else:
                print("❌ Budget must be a positive number.")
        except ValueError:
            print("❌ Invalid entry. Please input standard numerical digits.")

    # ----------------------------------------------------------------
    # 7. EXIT
    # ----------------------------------------------------------------
    elif choice == "7":
        print("\nClosing Tracker. Stay financially savvy!")
        break

    else:
        print("❌ Command selection out of scope. Enter numbers 1 through 7.")