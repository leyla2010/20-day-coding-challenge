 
def main():
    try:
        # Ask the user for their name
        name = input("Please enter your name: ").upper()
        
        # Check if the name is empty or contains only spaces
        if not name.strip():
            raise ValueError("Name cannot be empty. Please enter a valid name.")
        
      

        hours = int(input("Hi " + name + " how many hours have you been working?" ))

        #60 secoonds in a minuite - 3600 seconds in an hour 
        seconds = hours * 3600

        print("That is great " + name + " you were working for " + str(seconds)+ " seconds")

        
        
    except ValueError as e:
        # Handle the ValueError and print a custom error message
        print(f"Error: {e}")

    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Call the function to run the script
main()