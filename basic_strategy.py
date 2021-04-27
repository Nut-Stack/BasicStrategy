from basic_strategy_dict import *
#created by Nut-Stack
'''
https://www.blackjackclassroom.com/wp-content/uploads/2017/02/Double-Deck-Basic-Strategy-Chart.png
'''

def split(s):
    return [char for char in s]
face_cards = ['j','q','k']
plays = ["hit","stand","DD","split"]
def identical(lst):
    ele = lst[0]
    chk = True
    for item in lst:
        if ele != item:
            chk = False
            break
    if (chk == True):
        return True
    else:
        return False


while True:
    dealer_hand_raw = input("dealer's hand: ")
    try:
        if dealer_hand_raw in face_cards:
            dealer_hand = 10
        elif dealer_hand_raw == 'a':
            dealer_hand = 'a'
        else:
            dealer_hand = int(dealer_hand_raw)
        broken = False
    except:
        print("{} is not a valid card".format(dealer_hand_raw))
        broken = True
    if broken == False:
        player_hand_raw = input("player's hand: ")
        inner_dict = (big_dict.get(dealer_hand))
        try:
            player_hand_split = split(player_hand_raw)
            player_hand_split = [10 if i in face_cards else i for i in player_hand_split]
            player_hand_split = [10 if i == '1' else i for i in player_hand_split]
            try:
                player_hand_split.remove('0')
            except:
                pass
            player_hand = []
            
            if player_hand_split[0] != 'a':
                first_card = int(player_hand_split[0])
                player_hand.append(first_card)
            else:
                first_card = 'a'
                player_hand.append(first_card)
            if player_hand_split[1] != 'a':
                second_card = int(player_hand_split[1])
                player_hand.append(second_card)
            else:
                second_card = 'a'
                player_hand.append(second_card)

            if 'a' in player_hand:
                player_hand.clear()
                if first_card == 'a':
                    player_hand.append(first_card)
                    player_hand.append(str(second_card))
                if second_card == 'a':
                    player_hand.append(second_card)
                    player_hand.append(str(first_card))
                lookup = player_hand[0]+player_hand[1]
                dict_val = inner_dict.get(lookup)
                print(plays[dict_val])

            elif player_hand[0] == player_hand[1]:
                lookup = str(player_hand[0]) + str(player_hand[1])
                dict_val = inner_dict.get(lookup)
                print(plays[dict_val])

            elif not 'a' in player_hand:
                hand_value = sum(player_hand)
                dict_val = inner_dict.get(hand_value)
                if dict_val != None:
                    print(plays[dict_val])
                if dict_val == None:
                    print("ERROR ON :{}".format(player_hand))
            else:
                print("ERROR IN IF's")
        except:
            print("Player hand error")
    print("-------------------------------------------------------------------")



