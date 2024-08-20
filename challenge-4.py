 
def main():
    try:
       
      temp = int(input(" What is the temp "))

      if temp > 20 :
          print("I need to wear a T-Shirt ")

      elif temp > 0 :
        print("I need to wear a hoodie ")

      else:  
        print("I need to wear a duffle jacket and gloves ")

    
      
     



       
 
        
    except ValueError as e:
        # Handle the ValueError and print a custom error message
        print(f"Error: {e}")

    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Call the function to run the script
main()