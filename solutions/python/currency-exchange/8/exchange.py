""" Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget: float, exchange_rate: float) -> float:
    """ Calculate estimated value after exchange.

    Parameters:
        budget: The amount of money you are planning to exchange.
        exchange_rate: The unit value of the foreign currency.

    Returns:
        The exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """ Calculate currency left after an exchange.

    Parameters:
        budget: The amount of money you own.
        exchanging_value: The amount of your money you want to exchange now.

    Returns:
        The amount left of your starting currency after the exchange
    """

    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """ Calculate the total value of currency at the current denomination.

    Parameters:
        denomination: The value of a single unit (bill).
        number_of_bill: The total number of units (bills).

    Returns:
        Calculated value of the units (bills).

    """

    return denomination * number_of_bills


def get_number_of_bills(amount: float, denomination: int) -> int:
    """ Calculate the number of currency units (bills) within the amount.

    Parameters:
        amount: The total starting value.
        denomination: The value of a single unit (bill).

    Returns:
        The number of units (bills) that can be obtained from the amount.

    """

    return int( amount // denomination)


def get_leftover_of_bills(amount: float, denomination : int) -> float:
    """ Calculate the leftover amount after exchanging into bills.

    Parameters:
        amount: The total starting value.
        denomination: The value of a single unit (bill).

    Returns:
        The amount that is "leftover", given the current denomination.

    """

    return amount % denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    """ Calculate the maximum value of the new currency.

    Parameters:
        budget: The amount of your money you are planning to exchange.
        exchange_rate: The unit value of the foreign currency.
        spread: The percentage that is taken as an exchange fee.
        denomination: The value of a single unit (bill).

    Returns:
        The maximum value you can get in the new currency.

    """

    adjusted_exchange_rate = exchange_rate * (1 + (spread / 100))
    exchanged_amount = exchange_money(budget, adjusted_exchange_rate)
    number_of_bills = get_number_of_bills(exchanged_amount,denomination)
    return get_value_of_bills(denomination,number_of_bills)