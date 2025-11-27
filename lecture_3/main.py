"""
Student Grades Management System

A program that manages and analyzes student grades with type hints,
clean code practices, and modular function structure.
"""

import statistics
from typing import List, Dict, Optional, Any, Tuple


def calculate_student_average(grades: List[int]) -> Optional[float]:
    """
    Calculate the average of a list of grades.
    
    Args:
        grades: List of integer grades
        
    Returns:
        The average as a float, or None if the grades list is empty
    """
    if not grades:  # If grades list is empty
        return None
    
    try:
        return statistics.mean(grades)
    except (ZeroDivisionError, ValueError):
        # Handle any potential errors (though statistics.mean shouldn't raise ZeroDivisionError for non-empty lists)
        return None


def find_student(students: List[Dict[str, Any]], name: str) -> Optional[Dict[str, Any]]:
    """
    Search for a student by name in the students list.
    
    Args:
        students: The list of student dictionaries
        name: The name of the student to search for
        
    Returns:
        The student dictionary if found, or None if not found
    """
    for student in students:
        if student["name"] == name:
            return student
    return None


def add_student(students: List[Dict[str, Any]]) -> None:
    """
    Add a new student to the students list.
    
    Args:
        students: The list of student dictionaries (modified in place)
    """
    student_name = input("Enter student name: ")
    
    # Check if student already exists
    if find_student(students, student_name) is not None:
        print("Student with this name already exists.")
        return
    
    # Create new student dictionary and append to list
    new_student = {"name": student_name, "grades": []}
    students.append(new_student)
    print("Student added successfully.")


def add_grade(students: List[Dict[str, Any]]) -> None:
    """
    Add grades to an existing student.
    
    Args:
        students: The list of student dictionaries
    """
    student_name = input("Enter student name: ")
    
    # Find the student
    student = find_student(students, student_name)
    if student is None:
        print("Student not found.")
        return
    
    # Loop to collect grades
    while True:
        grade_input = input("Enter a grade (0-100) or 'done' to finish: ")
        
        # Check if user wants to finish
        if grade_input.lower() == "done":
            break
        
        # Try to convert input to integer
        try:
            grade = int(grade_input)
            
            # Check if grade is in valid range (0-100 inclusive)
            if 0 <= grade <= 100:
                student["grades"].append(grade)
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    
    print("Grades added successfully.")


def show_report(students: List[Dict[str, Any]]) -> None:
    """
    Display a report of all students with their averages and statistics.
    
    Args:
        students: The list of student dictionaries
    """
    # Check if students list is empty
    if not students:
        print("No students in the system.")
        return
    
    # Create list to store calculated averages
    student_averages: List[float] = []
    
    # Iterate through each student
    for student in students:
        print(student["name"])
        
        # Calculate student's average
        average = calculate_student_average(student["grades"])
        
        if average is None:
            # Student has no grades
            print("  Average: N/A")
        else:
            # Student has grades, print formatted average
            print(f"  Average: {average:.2f}")
            # Append to list for statistics calculation
            student_averages.append(average)
    
    # Calculate statistics on student averages (avg(avg_i) formula)
    if student_averages:
        # Calculate max, min, and overall average
        max_average = max(student_averages)
        min_average = min(student_averages)
        overall_average = statistics.mean(student_averages)
        
        # Print statistics
        print(f"Max average: {max_average:.2f}")
        print(f"Min average: {min_average:.2f}")
        print(f"Overall average: {overall_average:.2f}")
    else:
        # No valid averages to calculate statistics
        print("No valid averages to calculate statistics.")


def find_top_performer(students: List[Dict[str, Any]]) -> None:
    """
    Find and display the student with the highest average.
    
    Args:
        students: The list of student dictionaries
    """
    # Check if students list is empty
    if not students:
        print("No students in the system.")
        return
    
    # Create list to store tuples of (average, student_name) for students with valid averages
    students_with_averages: List[Tuple[float, str]] = []
    
    # Iterate through each student
    for student in students:
        average = calculate_student_average(student["grades"])
        
        # If average is not None, add to list
        if average is not None:
            students_with_averages.append((average, student["name"]))
    
    # Check if any students have valid averages
    if not students_with_averages:
        print("No students with grades found.")
        return
    
    # Use max() with lambda function to find the student with the highest average
    top_student = max(students_with_averages, key=lambda x: x[0])
    
    # Print the result
    print(f"Top performer: {top_student[1]} with average {top_student[0]:.2f}")


def display_menu() -> None:
    """
    Display the menu options to the user.
    """
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Show report (all students)")
    print("4. Find top performer")
    print("5. Exit")


def handle_menu_choice(choice: str, students: List[Dict[str, Any]]) -> bool:
    """
    Handle the user's menu choice and execute the corresponding action.
    
    Args:
        choice: The user's menu choice as a string
        students: The list of student dictionaries
        
    Returns:
        True to continue the menu loop, False to exit
    """
    if choice == "1":
        add_student(students)
        return True
    elif choice == "2":
        add_grade(students)
        return True
    elif choice == "3":
        show_report(students)
        return True
    elif choice == "4":
        find_top_performer(students)
        return True
    elif choice == "5":
        print("Exiting program.")
        return False
    else:
        print("Invalid choice. Please try again.")
        return True


def main() -> None:
    """
    Main program loop that runs the student grades management system.
    """
    # Initialize the students list
    # Each student is a dictionary with "name" (str) and "grades" (List[int])
    students: List[Dict[str, Any]] = []
    
    # Main menu loop
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        # Handle the menu choice
        if not handle_menu_choice(choice, students):
            break
    
    print("Program ended.")


if __name__ == "__main__":
    main()

