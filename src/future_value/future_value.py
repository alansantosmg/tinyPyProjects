"""Future calc"""

from os import system


def calculate_future_value(monthly_investiment, yearly_interest, years):
    """Calculate the future value"""
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    future_value = 0.0
    for _ in range(0, months):
        future_value += monthly_investiment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
    return future_value


def main():
    """the main function"""
    system("clear")
    choice = "y"
    while choice.lower() == "y":
        monthly_investiment = float(input("Enter monthly investiment:\t"))
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        years = int(input("Enter number of the years:\t"))

        future_value = calculate_future_value(
            monthly_investiment, yearly_interest_rate, years)

        print("Future_value:\t\t\t" + str(round(future_value, 2)))
        print()

        choice = input("Continue? (y/n): ")

    print("Bye!")


if __name__ == "__main__":
    main()
