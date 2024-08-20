 
def challenge_1():
    try:
        # Ask the user for their name
        name = input("Please enter your name: ")
        
        # Check if the name is empty or contains only spaces
        if not name.strip():
            raise ValueError("Name cannot be empty. Please enter a valid name.")
        
        age = int(input("What is your age " + name + "?"))
        
    except ValueError as e:
        # Handle the ValueError and print a custom error message
        print(f"Error: {e}")

    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Call the function to run the script
challenge_1()