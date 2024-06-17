#========The beginning of the class==========

# Import os library 
import os

# Get the path to the inventory 
script_dir = os.path.dirname(os.path.abspath(__file__))
inventory_file_path = os.path.join(script_dir, "inventory.txt")
print(inventory_file_path)

'''
This is a comment for my git task on a new branch task 7
Change the class Shoe to sneaker 
Add dispatch and Recieving for the store manager
Add courier services to the inventory 
'''

class Shoe:

    def __init__(self, country, code, product, price, quantity):
        self.country = country
        self.code = code 
        self.product = product
        self.price = price  
        self.quantity = quantity
     
    def get_cost(self):
        return self.price
 
    def get_quantity(self):
        return self.quantity 
 
    def __str__(self):
        return f"Country:{self.country}, Code:{self.code}, Product:{self.product},"\
           f"Cost:{self.price}, Quantity:{self.quantity}"
        
#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
''' 
shoe_list = []

#==========Functions outside the class==============

# Function to read shoe data from a file 
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            next(file)
            for line in file:
                data = line.strip().split(",")
                country, code, product, price, quantity = data
                shoe = Shoe(country, code, product, int(price), int(quantity))
                shoe_list.append(shoe)
        print("Shoe data has been read successfully.")
    except FileNotFoundError:
        print("Error: File not found.")

# Function to capture shoe data from user input
def capture_shoes():
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = int(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))
    new_varnew_var = shoe = Shoe(country, code, product, price, quantity)
    
    shoe_list.append(shoe)
    print("Shoe data has been captured successfully.")
    
# Function to view deatils of all shoes
def view_all():
    """
    Capture shoe data from user input and add it to the shoe list.
    """
    if shoe_list:
        for index, shoe in enumerate(shoe_list, start=1):
            print(f"\nShoe {index}")
            print(shoe)
    else:
        print("No shoe data available.")
        
# Function to restock shoes with low quantity 
def re_stock():
    if shoe_list:
        lowest_quantity_shoe = min(shoe_list, key=lambda x: x.get_quantity())
        print("Shoe with lowest quantity:", lowest_quantity_shoe)
        restock_quantity = int(input("Enter quantity to restock:"))
        lowest_quantity_shoe.quantity += restock_quantity
        print("Shoe restcoked successfully.")
    else:
        print("No shoe data available.")
        
        
# Function to search for a shoe by its code
def search_shoe():
    code_to_search = input("Enter code to search:")
    found = False
    for shoe in shoe_list:
        if shoe.code == code_to_search:
            print("Shoe found")
            print(Shoe)
            found = True 
            break
    if not found:
        print("Shoe not found.")
            
# Function to calculate the total value for each item 
def value_per_item():
    if shoe_list:
        print("\nValue per item:")
        for shoe in shoe_list:
            print(f"{shoe.product}: {shoe.cost*shoe.quantity}")
    else:
        print("No shoe data available.")
        
# Function to find the product with the highest quantity
def highest_qty():
    if shoe_list:
        max_quantity_shoe = max(shoe_list, key=lambda x: x.get_quantity())
        print("Product with highest quantity:", max_quantity_shoe.product)
    else:
        print("No shoe data available.")
        
# Main menu loop 
while True:
      print(
          "\n===== Main Menu =====",
    "1. Read Shoes Data from File",
    "2. Capture Shoes Data",
    "3. View All Shoes",
    "4. Re-stock Shoes",
    "5. Search for Shoe",
    "6. Calculate Value per Item", 
    "7. Find Product with Highest Quantity",
    "8. Exit"  
            )
      choice = input("Enter your choice:")
      if choice == "1":
          read_shoes_data()
      elif choice == "2":
          capture_shoes()
      elif choice == "3":
          view_all()
      elif choice == "4":
          re_stock()
      elif choice == "5": 
          search_shoe()
      elif choice == "6":
          value_per_item()
      elif choice == "7":
          highest_qty()
      elif choice == "8":
          print("Exiting the program. Goodbye")
          break
      else:
          print("Invalid choice. Please enter a valid option.")
            
#*******************************************End**********************************************