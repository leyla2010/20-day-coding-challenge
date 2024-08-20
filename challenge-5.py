 
def main():
    try:
        temp = int(input(" What is the temp "))
        weekday = input("Is it a weekday y/n ")

        if temp > 20 :
            if weekday == "y" :
                print("I will go shopping ")

            else: 
                print("I will go to the seaside ")

        else :
             print("I will stay indoors")  


    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Call the function to run the script
main()