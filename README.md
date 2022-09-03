# Dash-Honey-Dash

A 98% automated method of finding the best DoorDash/DashPass coupons/discounts.

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

To run this project, you will need to add the following environment variables to your `.env` file. 

`LOCAL_REST` = A string representing any local DoorDash resturant.

`LOCAL_ADDRESS` = A local address in your area. Does not have to be your own necessairly, just make sure it is within the `LOCAL_REST`'s delivery range.
