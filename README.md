# Dash-Honey-Dash

A 98% automated method of finding the best DoorDash/DashPass coupons/discounts.

## Important Notes
Project Status: Incomplete.

As it stands right now, this python program will do the heavy lifting and automate the boring tedious tasks such as signing up for a new account and filling the cart up. The user currently will need to intervene towards the very end of the program where the checkout cart page is loaded to click the pop-up button 'Apply Coupons.' 

This program can be especially be helpful on the go, running through a replit on your phone should be able to help a user obtain some very nice coupon/promo codes without needing to log onto a computer and wait for execution.

## Installation
The bot can be run using Python.
### Python Script
1. Clone this repository, cd into it, and install dependancies:
```sh
   git clone https://github.com/sazncode/Dash-Honey-Dash.git
   cd Dash-Honey-Dash
   pip install -r requirements.txt
   ```
2. Configure your `.env` file (See below and example for options)
3. Run the script:
```sh
   python main.py
```


## Environment Variables:

To run this project, you will need to add the following environment variables to your `.env` file. Variables are necessary due to certain DoorDash coupons being targeted towards certain parts of the country. You're welcome to put an address outside of your city or state, but I cannot guarantee whether a promo code will work for your main account if you choose to go that route.

`LOCAL_REST` = A string representing any local DoorDash resturant.

`LOCAL_ADDRESS` = A local address in your area. Does not have to be your own necessairly, just make sure it is within the `LOCAL_REST`'s delivery range.

`LOGIN` = Existing DoorDash Email/Password Credentials, seperated by ':', see .env for an example.