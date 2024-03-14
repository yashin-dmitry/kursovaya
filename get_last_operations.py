import json


def get_last_operations(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    executed_operations = [op for op in data if 'state' in op and op['state']
                           == 'EXECUTED']
    sorted_operations = sorted(executed_operations, key=lambda x: x['date'],
                               reverse=True)
    last_operations = sorted_operations[:5]

    for op in last_operations:
        date = op['date'].split('T')[0].split('-')
        date = f"{date[2]}.{date[1]}.{date[0]}"
        description = op['description']
        from_field = op.get('from', '')
        to_field = op['to']
        amount = op['operationAmount']['amount']
        currency = op['operationAmount']['currency']['name']

        print(f"{date} {description}")
        if from_field:
            print(f"{mask_card_number(from_field)} -> "
              f"{mask_card_number(to_field)}")
        else:
            print(f"{mask_card_number(to_field)}")
        print(f"{amount} {currency}\n")


def mask_card_number(card_number):
    count = 0
    for number in card_number:
        if number.isdigit():
            count += 1
    if count == 16:
        symbol = card_number[-16:]
        first_block = f'{symbol[:4]}'
        second_block = f'{symbol[4:6]}**'
        third_block = '****'
        fourth_block = f'{symbol[-4:]}'
        return (f'{card_number[:-16]}{first_block} {second_block} '
                f'{third_block} {fourth_block}')
    elif count == 20:
        return f'Счет **{card_number[-4:]}'


def detect_card_type(card_number):
    if card_number.startswith('5') and len(card_number) == 16:
        return 'Maestro'
    elif card_number.startswith('4') and (len(card_number) == 13 or
                                          len(card_number) == 16):
        return 'Visa Classic'
    elif card_number.startswith('4') and len(card_number) == 16:
        return 'Visa Platinum'
    elif card_number.startswith('4') and len(card_number) == 16:
        return 'Visa Gold'
    elif card_number.startswith('51') and len(card_number) == 16:
        return 'Master Card'
    else:
        return None


if __name__ == '__main__':
    get_last_operations('operations.json')
