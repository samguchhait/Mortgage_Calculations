from argparse import ArgumentParser
import math
import sys


def get_min_payment(principal, annual_interest_rate, term=30, payments_per_year=12):
    """
    Calculates the minimum mortgage payment to the next greatest integer and rounds.

    Args:
    principal(float): the total amount of the mortgage (positive number).
    annual_interest_rate(float): the annual interest rate (float between 0 and 1).
    term(int): the term of the mortgage in years (positive integer, default is 30).
    payments_per_year(int): the number of payments per year (positive integer, default is 12).

    Returns:
        raised_payments(float): the rounded-up minimum mortgage payment.
    """
    interest_per_payment = annual_interest_rate / payments_per_year
    total_payments = term * payments_per_year
    payment = principal * interest_per_payment * (1 + interest_per_payment) ** total_payments
    payment = payment / ((1 + interest_per_payment) ** total_payments - 1)
    raised_payment = math.ceil(payment)

    return raised_payment

def interest_due(balance_mortgage, annual_interest_rate, payments_per_year=12):
    """Calculates the amount of interest due in the next payment.

    Args:
    balance_mortgage(float): The balance of the mortgage (positive number).
    annual_interest_rate(float): The annual interest rate (float between 0 and 1).
    payments_per_year(int): The number of payments per year (positive integer, default is 12).

    Returns:
        i(float): the amount of interest due in the next payment.
    """

    interest_per_payment = annual_interest_rate / payments_per_year
    i = balance_mortgage * interest_per_payment

    return i

def remaining_payments(balance_mortgage, annual_interest_rate, target_payment, payments_per_year=12):
    """
    Calculates how many payments will be necessary to pay off the mortgage.

    Args:
    balance_mortgage(float): the balance of the mortgage.
    annual_interest_rate(float): the annual interest rate.
    target_payment(float): the target payment per payment.
    payments_per_year(int): the number of payments per year.

    Returns:
        number_of_payments(int): the number of payments are necessary to pay off the mortgage.
    """
    number_of_payments = 0
    while balance_mortgage > 0:
        next_payment_of_interest = interest_due(balance_mortgage, annual_interest_rate, payments_per_year)
        balance_principal = (target_payment - next_payment_of_interest)
        balance_mortgage= balance_mortgage - balance_principal
        number_of_payments += 1

    return number_of_payments

def main(principal, annual_interest_rate, term=30, payments_per_year=12, target_payment=None):
    """
    Compute information about mortgages and show it to the user.

    Args:
    principal(float): the total amount of the mortgage.
    annual_interest_rate(float): the annual interest rate.
    term(int): the term of the mortgage in years.
    payments_per_year(int): the number of payments per year.
    target_payment(float): the target payment per payment.

    Side effects:
        The four prints statements in the function use f strings that exist beyond the function.
    """
    min_payment = get_min_payment(principal, annual_interest_rate, term, payments_per_year)
    print(f"Minimum Mortgage Payment: ${min_payment}")
    if target_payment is None:
        target_payment = min_payment
    if target_payment < min_payment:
        print("Your target payment is less than the minimum payment for this mortgage.")
    else:
        number_of_payments = remaining_payments(principal, annual_interest_rate, target_payment, payments_per_year)
        print(f"If you make payments of ${target_payment}, you will pay off the mortgage in {number_of_payments} payments.")

def parse_args(arglist):
    """Parse and validate command-line arguments.

        This function expects the following required arguments, in this order:

        mortgage_amount (float): total amount of a mortgage
        annual_interest_rate (float): the annual interest rate as a value
            between 0 and 1 (e.g., 0.035 == 3.5%)

        This function also allows the following optional arguments:

            -y / --years (int): the term of the mortgage in years (default is 30)
            -n / --num_annual_payments (int): the number of annual payments
                (default is 12)
            -p / --target_payment (float): the amount the user wants to pay per
                payment (default is the minimum payment)

        Args:
            arglist (list of str): list of command-line arguments.

        Returns:
            namespace: the parsed arguments (see argparse documentation for
            more information)

        Raises:
            ValueError: encountered an invalid argument.
        """
        # set up argument parser
    parser = ArgumentParser()
    parser.add_argument("mortgage_amount", type=float,
                        help="the total amount of the mortgage")
    parser.add_argument("annual_interest_rate", type=float,
                        help="the annual interest rate, as a float"
                                " between 0 and 1")
    parser.add_argument("-y", "--years", type=int, default=30,
                        help="the term of the mortgage in years (default: 30)")
    parser.add_argument("-n", "--num_annual_payments", type=int, default=12,
                        help="the number of payments per year (default: 12)")
    parser.add_argument("-p", "--target_payment", type=float,
                        help="the amount you want to pay per payment"
                                " (default: the minimum payment)")
        # parse and validate arguments
    args = parser.parse_args()
    if args.mortgage_amount < 0:
        raise ValueError("mortgage amount must be positive")
    if not 0 <= args.annual_interest_rate <= 1:
        raise ValueError("annual interest rate must be between 0 and 1")
    if args.years < 1:
        raise ValueError("years must be positive")
    if args.num_annual_payments < 0:
        raise ValueError("number of payments per year must be positive")
    if args.target_payment and args.target_payment < 0:
        raise ValueError("target payment must be positive")

    return args

if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    main(args.mortgage_amount, args.annual_interest_rate, args.years,
            args.num_annual_payments, args.target_payment)
