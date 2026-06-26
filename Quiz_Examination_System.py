# ====================================================================
# QUIZ & EXAMINATION SYSTEM
# CREATED BY SUMIT GOREGAONKAR
# ====================================================================
exam_questions = (
    (
        "Which programming language is known for its readability and use of indentation?",
        ("Java", "Python", "C++", "JavaScript"),
        "B"
    ),
    (
        "What is the primary purpose of an 'if' statement in programming?",
        ("To loop code", "To declare variables", "To make decisions", "To import libraries"),
        "C"
    ),
    (
        "Which of the following is an immutable data structure in Python?",
        ("List", "Dictionary", "Set", "Tuple"),
        "D"
    ),
    (
        "What does 'HTML' stand for?",
        ("Hyper Text Markup Language", "High Tech Multi Language", "Hyperlink and Text Management Law", "Home Tool Markup Language"),
        "A"
    )
)

# Registered students tracking list
students_records = []

# ====================================================================
# MAIN APPLICATION LOOP
# ====================================================================
while True:
    # String formatting operation to center-align the application headers
    print("\n" + "=" * 55)
    print("ONLINE EXAMINATION SYSTEM".center(55))
    print("=" * 55)
    print("1. Take Examination (Students)")
    print("2. View Performance & Analysis (Admin)")
    print("3. Exit Portal")
    print("=" * 55)

    choice = input("Select an option (1-3): ").strip()

    # ----------------------------------------------------------------
    # 1. TAKE EXAMINATION
    # ----------------------------------------------------------------
    if choice == "1":
        print("\n" + "-" * 55)
        print(" STUDENT REGISTRATION & EXAM PORTAL ".center(55, "-"))
        print("-" * 55)
        
        # String cleanup operations
        raw_name = input("Enter your Full Name: ")
        student_name = raw_name.strip().title() # Sanitizes spaces and capitalizes names
        
        if not student_name:
            print("❌ Error: Name field cannot be left blank.")
            continue

        print(f"\nWelcome, {student_name}! Your exam is starting now.")
        print("Type the letter (A, B, C, or D) corresponding to your answer.\n")
        
        score = 0
        total_questions = len(exam_questions)
        
        # Iterating through the master question tuple
        for index, q_bank in enumerate(exam_questions, start=1):
            question_text, options, correct_answer = q_bank
            
            # Using string manipulation to pad question numbers (e.g., 01, 02)
            q_num_str = str(index).zfill(2)
            print(f"Q{q_num_str}: {question_text}")
            
            # Printing options dynamically mapped to option letters
            print(f"   A) {options[0]}")
            print(f"   B) {options[1]}")
            print(f"   C) {options[2]}")
            print(f"   D) {options[3]}")
            
            # Process student input string
            user_ans = input("Your Answer: ").strip().upper()
            
            # String matching comparison
            if user_ans == correct_answer:
                score += 1
                
            print("-" * 50) # Section divider line string
        
        # Arithmetic calculations for performance percentage
        percentage = (score / total_questions) * 100
        
        # Assigning academic pass status based on outcome
        status = "PASSED" if percentage >= 50 else "FAILED"
        
        # Store results as a record tuple inside our tracking list
        students_records.append((student_name, score, total_questions, percentage, status))
        
        print("\n" + "*" * 55)
        print(" EXAM COMPLETE ".center(55, "*"))
        print(f"Student Name : {student_name}")
        print(f"Final Score  : {score} / {total_questions}")
        print(f"Percentage   : {percentage:.1f}%")
        print(f"Exam Status  : {status}")
        print("*" * 55)

    # ----------------------------------------------------------------
    # 2. VIEW PERFORMANCE & ANALYSIS
    # ----------------------------------------------------------------
    elif choice == "2":
        print("\n" + "-" * 65)
        print(" GLOBAL PERFORMANCE GRADEBOOK ".center(65, "-"))
        print("-" * 65)
        
        if not students_records:
            print("No examination logs found in the session database.")
        else:
            # String alignment manipulation formatting for pristine column structure
            print(f"{'Student Name':<20} | {'Score':<8} | {'Percentage':<12} | {'Status'}")
            print("-" * 65)
            
            # Parsing recorded historical tuples
            for record in students_records:
                s_name, s_score, total_q, s_perc, s_stat = record
                
                # Check if student passed or failed to append a text decorator string
                alert = "🎉 " if s_stat == "PASSED" else "❌ "
                
                print(f"{s_name:<20} | {s_score}/{total_q:<6} | {s_perc:<10.1f}% | {alert}{s_stat}")
                
            print("-" * 65)
            print(f"Total Completed Attempts: {len(students_records)}")

    # ----------------------------------------------------------------
    # 3. EXIT PORTAL
    # ----------------------------------------------------------------
    elif choice == "3":
        print("\n" + " Shutting down examination portal servers... ".center(55, "="))
        break

    else:
        print("❌ Action rejected. Enter a valid menu selection (1, 2, or 3).")