"""Functions to help play and score a game of blackjack.
"""

def value_of_card(card):
    """Determine the scoring value of a card.
    """
    faces = ["J", "Q", "K"]
    if card in faces:
        return 10
    if card == "A":
        return 1
    return int(card)

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.
    """
    one_value = value_of_card(card_one)
    two_value = value_of_card(card_two)
    if one_value > two_value:
        return card_one
    if one_value < two_value:
        return card_two
    return card_one, card_two

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.
    """
    if card_one != "A" and card_two != "A":
        if value_of_card(card_one) + value_of_card(card_two) <= 10:
            return 11
    return 1

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.
    """
    tens = ["10", "J", "Q", "K"]
    return (card_one in tens and card_two == "A") or (card_one == "A" and card_two in tens)

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.
    """
    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.
    """
    return (value_of_card(card_one) + value_of_card(card_two)) in range(9,12)