import json
blackjack_hand = (8, "Q")
print(type(blackjack_hand))
encoded_hand = json.dumps(blackjack_hand)
print(type(encoded_hand))
print (encoded_hand)
# print(type(blackjack_hand))
# decoded_hand = json.loads(encoded_hand)
# print(type(decoded_hand))
