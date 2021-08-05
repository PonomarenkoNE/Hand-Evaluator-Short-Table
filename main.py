
card_value = {
    '6': 1,
    '7': 2,
    '8': 3,
    '9': 4,
    't': 5,
    'j': 6,
    'q': 7,
    'k': 8,
    'a': 9
}

card_value2 = {
    '6': 78,
    '7': 70,
    '8': 62,
    '9': 54,
    't': 46,
    'j': 38,
    'q': 30,
    'k': 22,
    'a': 14
}


def is_flush(hand: list):
    check = [item[0] for item in hand]
    if not all(elem == check[0] for elem in check):
        return False
    royal_flush = [['st', 'sj', 'sq', 'sk', 'sa'], ['ct', 'cj', 'cq', 'ck', 'ca'],
                   ['ht', 'hj', 'hq', 'hk', 'ha'], ['dt', 'dj', 'dq', 'dk', 'da']]
    if any([hand == i for i in royal_flush]):
        return 1

    values = [card_value[item[1]] for item in hand]
    values.sort()
    if all(values[i] + 1 == values[i + 1] for i in range(len(values)-1)):
        return 10 - values[4]

    if values == [1, 2, 3, 4, 9]:
        return 6

    return 270 + values[4]


def is_kare(hand: list):
    values = [card_value[item[1]] for item in hand]
    values2 = [card_value2[item[1]] for item in hand]
    values.sort()
    if values[0] == values[1] and values[1] == values[2] and values[2] == values[3]:
        return values2[0] - values[4] + 2
    elif values[1] == values[2] and values[3] == values[2] and values[3] == values[4]:
        return values2[0] - values[0] + 1
    else:
        return False


def is_fullhouse(hand: list):
    values = [card_value[item[1]] for item in hand]
    values2 = [card_value2[item[1]] for item in hand]
    values.sort()
    if values[0] == values[1] and values[2] == values[3] and values[3] == values[4]:
        return values2[0] + 72 - values[4] + 2
    elif values[0] == values[1] and values[1] == values[2] and values[3] == values[4]:
        return values2[0] + 72 - values[0] + 1
    else:
        return False


if __name__ == '__main__':
    rank = is_flush(['ht', 'hj', 'Ahq', 'hk', 'ha'])
    rank = is_fullhouse(['ha', 'da', 'ca', 'sk', 'sk'])
    print(rank)
