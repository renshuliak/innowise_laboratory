def generate_profile(age: int) -> str:
    """
    Determine the user's life stage based on age.
    
    Args:
        age: The user's age as an integer
        
    Returns:
        A string describing the life stage: "Child", "Teenager", or "Adult"
    """
    if age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <= 19:
        return "Teenager"
    else:
        return "Adult"


# Get user input
user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year

# Collect hobbies
hobbies = []
while True:
    hobby_input = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby_input.lower() == "stop":
        break
    hobbies.append(hobby_input)
