# store-management-system

Store Management System in Python with secuirty system, data persistence and seamlessly updates item quantity when purchased by customer.

## Dependencies

Python Version- Python 3.x
Libraries used - PySimpleGUI

    pip install PySimpleGUI

## Running the Program

Ensure PySimpleGUI is installed and on your python path and run main.py.

## Setting Up

1. login with credentials 

   Username - ABC

   Password - password (very secure I know)

2. Click on Add New User and enter with the same credentials
3. Create your own username and password

You can now use the program with your account.

## Using the Billing feature

Open the Billing Window under the Billing tab.

Enter your product name. Click on the autofill button to fill in all details or type in your product name. Then enter the quantity the customer wants.

If the product is added to the item list, then the product was successfully billed.

When you're done with the entire order, press Print Bill and you'll be done. There will be text file with the date and time of the billing saved in the same directory of the program.

## Using the Inventory Management System

### View Stock Window

You can view all items and their quantity in inventory 

### Edit Stock Window

Change product details such as Product ID, Procurment Cost, Retail Cost or Quantity.

#### Usage

Enter product name, either through autofill or by typing it in and press Get Data.

Change details you wish to change and press Save to save edited details, or press Undo to reset changes.

### Add Stock Window

Add a new product to your store. Enter details into the window and save. Make sure ID is not repeated.

## Security Features

### Add User

Create user to login with.

### Incorrect Attempts

If you make 3 incorrect login attempts with a user, they are blocked and cannot login until another user unblock them. 

### Unblock User

The unblock user page is used to unblock a user with too many failed attempts to login. This requires an unblocked user to log into the unblock user page, select the blocked user and press on the unblock user button.

## Inspiration for the project

This project was made for my Grade 12 Final Project for Computer Science. This seemed interesting and was a bigger project than I'd ever done at the time. It also allowed me to tinker with GUIs and was a fun learning experience.

## Improvements

- I recognize this project is not well commented, and the structure isn't very well done.
- The project also uses csv files to store data, which isn't very secure or scalable. A DBMS system would be better suited for this.
- No tests or OOP prinicple implemented.
- The GUI looks dated, and if I'd do this again I'd use a better template and spend more time on the GUI.
