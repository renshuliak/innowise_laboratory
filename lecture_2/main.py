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

def main():
    age = int(input("Enter your age: "))
    profile = generate_profile(age)
    print(f"You are a {profile}")

if __name__ == "__main__":
    main()
    