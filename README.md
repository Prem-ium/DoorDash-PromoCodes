# DoorDash Auto Promo Codes

A cool python script to apply the most common promo codes to your DoorDash account. 
This repository automates the process of creating new accounts, adding items to the cart, & more.

[Check out <b>this Coupon Scraper repository</b> to scrape the internet for more DoorDash promotion codes.](https://github.com/Prem-ium/DoorDash-Coupon-Scraper)

## Important Notes
User interaction is needed ocassionally for phone/email verification due to DoorDash's two-step verification prompts. Addionally, user interaction is needed at the very end of the program at checkout where the user needs to click the button labled 'Apply Coupons.' manually, to start the process of checking through all known active promotion coupons.

This script is best paired with a repl on replit, so you may use Honey to find the best promo codes through your phone, on the go.

## Installation
The bot can be run using Python.
### Python Script
1. Clone this repository, cd into it, and install dependancies:
```sh
   git clone https://github.com/Prem-ium/DoorDash-PromoCodes.git
   cd DoorDash-PromoCodes
   pip install -r requirements.txt
   ```
2. Configure your `.env` file (See below and example for options)
3. Run the script:
```sh
   python main.py
```

## Environment Variables:

To run this project, you will need to add the following environment variables to your `.env` file. 

`AUTO_SIGNIN` = Boolean True/False whether you will provide the LOGIN in env

   `LOGIN` = Existing DoorDash Email/Password Credentials, seperated by ':', see .env for an example. Only needed if AUTO_SIGNIN is set to true.

`HANDLE_CART`= Boolean True/False, whether you want the program to automate filling a cart, or use pre-existing (only available when AUTO_SIGNIN is set to True). Default set to False unless AUTO_SIGNIN is False (in which case, HANDLE_CART defaults to True).

   `LOCAL_REST` = A string representing any local DoorDash resturant, only used if HANDLE_CART is set to True.

   `LOCAL_ADDRESS` = A local address in your area. Does not have to be your own necessairly, just make sure it is within the local resturant's delivery range, generally only needed if HANDLE_CART is set to True.

`SIGNUP_LOGIN`= Email and Password of the account you wish to create with doordash, seperated by colon, :, If none is passed-- a random email/password will be used in its place. Only used when AUTO_SIGNIN is set to False.

## Comments
Personally, I've paired this script with Replit, which enables me to check for the best discounts on the go (as I can simpily run the program on my phone through the replit app/website). This program was made so I could find the best deals and savings without needing to manually go through coupon/promo code one-by-one on my phone. 

Now... Dash Honey, Dash! 
