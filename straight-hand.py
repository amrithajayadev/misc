from typing import List


def isNStraightHand(hand: List[int], groupSize: int) -> bool:
    def _is_group_straight(idx):
        for i in range(idx + groupSize - 1, idx, -1):
            if hand[i] - hand[i - 1] != 1:
                return False
        return True

    n = len(hand)
    if n % groupSize != 0:
        return False

    # create a map of the cards with key as the card value and frequency as the map value.
    # get the min value in the cards map.
    # start from the min value and keep checking if +1 is there in the map until groupSize.
    # continue until all the cards freq is reduced to 0.

    cards = {}
    for c in hand:
        cards[c] = cards.get(c, 0) + 1

    hand.sort()
    i = 0
    while i < len(hand):
        if cards[hand[i]] == 0:
            print(f"No more cards for {hand[i]}")
            i += 1
            continue
        for j in range(hand[i], hand[i] + groupSize):
            print(f"Checking cards for {j}, Num cards left :{cards[j]}")
            if cards.get(j) > 0:
                cards[j] -= 1
            else:
                return False
        i += 1

    return True

# hand = [1,2,4,2,3,5,3,4]
# groupSize = 4

# hand = [1,2,3,4,2,5,6,7]
# groupSize = 4

hand = [1,1,1,1,2,3,4,5]
groupSize = 4

print(isNStraightHand(hand, groupSize))