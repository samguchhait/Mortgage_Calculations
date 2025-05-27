# Mortgage Calculator

## Features
- Computes minimum monthly payment using the amortization formula. 
- Handles arbitrary mortgage terms and payment frequencies.
- Warns users if their payment is too low.
- Accepts user input from the command line with validation.

---

## How to Run

- Make sure you have Python 3 installed.
- No external libraries required (only argparse, math, and sys).
- My program is designed to run from the terminal.
- To run it, open a terminal and ensure you are in the directory where your script is saved.

The program takes two required command-line arguments:  
- **mortgage amount** (e.g., 300000)  
- **interest rate** (expressed as a float between 0 and 1, e.g., 0.03)  

It also allows the following optional arguments:  
- `-y` (the term of the mortgage in years)  
- `-n` (the number of annual payments)  
- `-p` (the target payment)  

The examples below assume you are using macOS and your program is called `mortgage.py`.  
If you are using Windows, replace `python3` with `python`.

## Example Command-line Arguments

**Basic usage:**  
`python3 mortgage.py 300000 0.03`

**With one optional parameter:**  
`python3 mortgage.py 300000 0.03 -y 15`

**With multiple optional parameters:**  
`python3 mortgage.py 300000 0.03 -y 15 -p 4000`
