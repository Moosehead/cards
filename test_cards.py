from cards import *
import pytest
from copy import deepcopy

def test_does_draw_work():
	deck = Deck()
	old_len = len(deck.cards)
	expected_card = deck.cards[len(deck.cards) - 1]
	card = deck.draw()
	assert expected_card.value == card.value
	assert expected_card.suit == card.suit
	assert old_len == len(deck.cards) + 1

# YES there is a very small percentage of times this will fail but is is very unlikely
def test_does_shuffle_work():
	deck = Deck()
	old_deck = deepcopy(deck)
	deck.shuffle()
	for i in range(0, len(deck.cards)):
		if deck.cards[i] != old_deck.cards[i]:
			pass