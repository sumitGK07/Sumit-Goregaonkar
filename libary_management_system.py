# ====================================================================
# LIBRARY MANAGEMENT SYSTEM
# CREATED BY SUMIT GOREGAONKAR
# ====================================================================

# Initial library data
library = {
    "B001": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "status": "Available",
    },
    "B002": {
        "title": "1984",
        "author": "George Orwell",
        "status": "Borrowed",
    },
    "B003": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "status": "Available",
    },
}

# ====================================================================
# MAIN APPLICATION LOOP
# ====================================================================
while True:
    print("\n" + "=" * 40)
    print("      LIBRARY MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add New Book")
    print("2. View All Books")
    print("3. Search for a Book")
    print("4. Issue / Borrow a Book")
    print("5. Return a Book")
    print("6. Delete a Book Record")
    print("7. Exit")
    print("=" * 40)

    choice = input("Enter your choice (1-7): ").strip()

    # ----------------------------------------------------------------
    # 1. ADD NEW BOOK
    # ----------------------------------------------------------------
    if choice == "1":
        print("\n--- Add New Book ---")
        book_id = input("Enter Book ID (e.g., B004): ").strip().upper()

        if book_id in library:
            print("❌ Error: A book with this ID already exists.")
        else:
            title = input("Enter Book Title: ").strip()
            author = input("Enter Author Name: ").strip()

            # Adding inner dictionary to the master library dictionary
            library[book_id] = {
                "title": title,
                "author": author,
                "status": "Available",
            }
            print(f"✔️ Success: '{title}' added to the library.")

    # ----------------------------------------------------------------
    # 2. VIEW ALL BOOKS (Looping through Nested Dictionary)
    # ----------------------------------------------------------------
    elif choice == "2":
        print("\n--- Library Inventory ---")
        if not library:
            print("The library is currently empty.")
        else:
            print(
                f"{'ID':<8} | {'Title':<30} | {'Author':<25} | {'Status':<10}"
            )
            print("-" * 78)
            # Loop through outer dictionary keys and values
            for book_id, info in library.items():
                print(
                    f"{book_id:<8} | {info['title']:<30} | {info['author']:<25} | {info['status']:<10}"
                )

    # ----------------------------------------------------------------
    # 3. SEARCH FOR A BOOK (Looping & Conditional Search)
    # ----------------------------------------------------------------
    elif choice == "3":
        print("\n--- Search Books ---")
        keyword = input("Enter Title or Author to search: ").strip().lower()
        found = False

        print(
            f"\n{'ID':<8} | {'Title':<30} | {'Author':<25} | {'Status':<10}"
        )
        print("-" * 78)

        # Loop to inspect internal dictionary contents dynamically
        for book_id, info in library.items():
            if (
                keyword in info["title"].lower()
                or keyword in info["author"].lower()
            ):
                print(
                    f"{book_id:<8} | {info['title']:<30} | {info['author']:<25} | {info['status']:<10}"
                )
                found = True

        if not found:
            print("No matching books discovered.")

    # ----------------------------------------------------------------
    # 4. ISSUE / BORROW A BOOK (Updating inner dictionary value)
    # ----------------------------------------------------------------
    elif choice == "4":
        print("\n--- Issue Book ---")
        book_id = input("Enter Book ID to issue: ").strip().upper()

        if book_id in library:
            if library[book_id]["status"] == "Available":
                library[book_id]["status"] = "Borrowed"
                print(
                    f"✔️ Success: '{library[book_id]['title']}' has been issued."
                )
            else:
                print("❌ This book is already borrowed by someone else.")
        else:
            print("❌ Error: Book ID not found.")

    # ----------------------------------------------------------------
    # 5. RETURN A BOOK
    # ----------------------------------------------------------------
    elif choice == "5":
        print("\n--- Return Book ---")
        book_id = input("Enter Book ID to return: ").strip().upper()

        if book_id in library:
            if library[book_id]["status"] == "Borrowed":
                library[book_id]["status"] = "Available"
                print(
                    f"✔️ Success: '{library[book_id]['title']}' returned safely."
                )
            else:
                print("❌ This book is already flagged as Available.")
        else:
            print("❌ Error: Book ID not found.")

    # ----------------------------------------------------------------
    # 6. DELETE A BOOK RECORD
    # ----------------------------------------------------------------
    elif choice == "6":
        print("\n--- Remove Book Record ---")
        book_id = input("Enter Book ID to remove: ").strip().upper()

        if book_id in library:
            removed_title = library[book_id]["title"]
            del library[book_id]  # Deletes entire sub-dictionary element
            print(f"✔️ Success: '{removed_title}' removed from database.")
        else:
            print("❌ Error: Book ID not found.")

    # ----------------------------------------------------------------
    # 7. EXIT
    # ----------------------------------------------------------------
    elif choice == "7":
        print("\nExiting System... Goodbye!")
        break

    else:
        print("Invalid entry. Please enter a number between 1 and 7.")