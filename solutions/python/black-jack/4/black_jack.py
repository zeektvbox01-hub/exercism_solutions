""" Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card: str) -> str:
    """Determine the scoring value of a card.

    Parameters:
        card: The given card.

    Returns:
        The value of a given card.
    """

    if card in {'J','Q','K'}:
        return 10
    if card == 'A':
        return 1
    return int(card)


def higher_card(card_one: str, card_two: str) -> str | tuple:
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one: First card dealt in the hand.
        card_two: Second card dealt in the hand.

    Returns:
        The resulting tuple contains both cards if they are of equal value.
    """

    value_of_card_one = value_of_card(card_one)
    value_of_card_two = value_of_card(card_two)
    if value_of_card_one > value_of_card_two:
        return card_one 
    if value_of_card_two > value_of_card_one:
        return card_two
    return (card_one,card_two)


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one: First card dealt in the hand.
        card_two: Second card dealt in the hand.

    Returns:
        Either 1 or 11, which is the value of the upcoming ace card.
    """

    if card_one == 'A' or card_two == 'A':
        return 1
    value_of_card_one = value_of_card(card_one)
    value_of_card_two = value_of_card(card_two)
    if value_of_card_one + value_of_card_two <= 10:
        return 11
    return 1    


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one: First card dealt in the hand.
        card_two: Second card dealt in the hand.

    Returns:
        Is the hand a blackjack? (i.e. two cards worth 21)
    """

    return all([any([card_one in {'J','K','Q','10'},card_two in {'J','K','Q','10'}]),any([card_one == 'A' or card_two == 'A'])])


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

   Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value)
    """

    value_of_card_one = value_of_card(card_one)
    value_of_card_two = value_of_card(card_two)
    return value_of_card_one == value_of_card_two



def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one: First card in the hand.
        card_two: Second card in the hand.

    Returns:
        Can the hand be doubled down? (i.e. totals 9, 10 or 11 points)
    """

    value_of_card_one = value_of_card(card_one)
    value_of_card_two = value_of_card(card_two)
    return value_of_card_one + value_of_card_two in {9,10,11}
