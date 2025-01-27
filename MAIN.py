# BUS 392 Final Project
# Adam Watson and Alyx Stewart

import csv
import sys
import datetime
import random


def main():
    print("                         UPC Reader Menu                          ")
    print("------------------------------------------------------------------")
    print( "1. Record Sale")
    print( "2. Retrieve Online Orders")
    print( "3. Update Catalog")
    print( "4. Terminate Program")
    
    # Prompt user to make a menu selection
    another = input ("Would you like to make a selection? (Y or N) :" )
    while another == "Y" or "y":
        selection = input("Please make a selection (1,2,3,or 4): " )
        if selection == "1":
            # Run the Record Sale functions
            #Recordsale()
            create_order_number(upc)
            calculate_total (price)
            want_receipt ()
        elif selection == "2":
         # Run the Retrieve Online Order functions
        elif selection == "3":
        # Run the Update Catalog functions
        elif selection == "4":
          #Run the Terminate Program functions
            terminate_program()
        elif selection != "1" or selection != "2" or selection != "3" or selection != "4":
            print ("ERROR: Please enter valid selection number")
            selection = input("Please make a selection (1,2,3,or 4): " )
        
#ENTIRE PROGRAM FUNCTIONS:   
# Function to convert CVS file to a list
def cvs_to_list ():
    # Reads in the csv file to a list
    infile = open('UPC.csv', 'r',encoding='utf-8-sig')
    items = []
    for line in infile:
        items.append(line.rstrip('\n').split(','))

    for item in items:
        item.append(get_price())

    for item in items:
        print(item)

# Function to generate and return random prices for items
def get_price():
    ran_price = random.uniform(.99,4.99)
    return ran_price


#RECORD SALE FUNCTIONS: 
# Function that takes scanned UPC as an argument
def create_order_number (order_number):
    
    # Create time stamp    
    today = datetime.date.today()

    # Formate date
    date = today.strftime("%m%d%Y")
    
    # Varible to hold order number (combion count and date)
    unique_order_number = date + "-" + order_number
    return unique_order_number

# Function to calculate subtotal, tax, and grand total
def calculate_total (price):
    # Add up all the item prices
    total = price += price

    # Calculate sales tax
    sales_tax = total * .08

    # Calculate grand total
    grand_total = total + sales_tax

    # Return total
    return grand_total

#Function Prompt user to see if they want a printed receipt
def want_receipt (unique_order_number, data):
    yes_or_no = input ("Would you like to print a receipt? (Y or N) : ")
    if "Y" or "y":
        unique_order_number = receipt_file_name 
        receipt = open (receipt_file_name.txt, "w")
        receipt.write(data)
        # Change data to whatever we name the UPC file return info
        receipt.close()
        
    else:
        print ("No Receipt")
        
# ONLINE ORDER FUNCTIONS:

# UPDATE CATALOG FUNCTIONS:
        
# TERMINATE PROGRAM FUNCTION:
def terminate_program():
    exit()
    
