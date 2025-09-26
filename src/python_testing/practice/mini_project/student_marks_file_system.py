file_name = "students.txt"
PASS_MARKS = 40  # threshold for pass
MAX_MARKS = 100  # assume marks are out of 100
# Step 1: Write data
try:
    with open(file_name, "w") as f:
        n = int(input("Enter number of students: "))
        for i in range(n):
            name = input(f"Enter name of student {i + 1}: ")
            try:
                marks = int(input(f"Enter marks of {name}: "))
                f.write(f"{name}: {marks}\n")
            except ValueError:
                print("Invalid marks! Skipping...")
except Exception as e:
    print("Error while writing:", e)

# Step 2: Read & Sort data
try:
    print("\nStudent Records (sorted by marks):")
    students = []
    with open(file_name, "r") as f:
        for line in f:
            parts = line.strip().split(":")
            if len(parts) == 2:
                name, marks = parts[0].strip(), parts[1].strip()
                try:
                    students.append((name, int(marks)))
                except ValueError:
                    continue  # skip invalid marks

    # Sort by marks (highest first)
    students.sort(key=lambda x: x[1], reverse=True)

    # Display sorted
    total_marks = 0
    for name, marks in students:
        percentage = (marks / MAX_MARKS) * 100
        result = "Pass" if marks >= PASS_MARKS else "Fail"
        # Grading system
        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"
        # print(f"Name: {name} | Marks: {marks} | Result: {result} | Grade: {grade}")
        print(f"Name: {name:<10} | Marks: {marks:<3} | Result: {result:<4} | Grade: {grade}")
        total_marks = total_marks + marks

    if students :
        topper_name, topper_marks = students[0]
        print(f"Topper of the batch is: {topper_name} with {topper_marks} marks")
        print('Average marks in class are : ',(total_marks/len(students)))
    else:
        print("No student records found!")
except FileNotFoundError:
    print("File not found!")