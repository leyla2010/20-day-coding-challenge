 
def main():
    try:
       
       freind1name = "Emily"
       freind2name = "Poppy"
       
       freind1height = int(input("Hi " + freind1name + " what is your height in cm? "))   
       freind2height = int(input("Hi " + freind2name +   " what is your height in cm? "))  

       if freind1height > freind2height :
         diff = freind1height - freind2height
         print(freind1name + " is taller by " + str(diff) + "cm " )

       elif freind2height > freind1height :
        diff = freind2height - freind1height
        print(freind2name + " is taller by " + str(diff) + "cm " )

       else: 
          print("You are the same height")
       
 
        
    except ValueError as e:
        # Handle the ValueError and print a custom error message
        print(f"Error: {e}")

    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Call the function to run the script
main()