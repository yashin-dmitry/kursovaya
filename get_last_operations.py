import json
import re

def get_last_operations(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    executed_operations = [op for op in data if 'state' in op and op['state'] == 'EXECUTED']
    sorted_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)
    last_operations = sorted_operations[:5]

    for op in last_operations:
        date = op['date'].split('T')[0]
        description = op['description']
        from_field = op.get('from', '')
        to_field = op['to']
        amount = op['operationAmount']['amount']
        currency = op['operationAmount']['currency']['name']

        print(f"{date} {description}")
        print(f"{mask_card_number(from_field)} -> {mask_account_number(to_field)}")
        print(f"{amount} {currency}\n")

def mask_card_number(card_number, card_type=None):
    if card_type is None:
        card_type = detect_card_type(card_number)

    if card_type in ['Maestro', 'Visa Classic', 'Visa Platinum', 'Visa Gold', 'Master Card']:
        return card_number

    masked_number = re.sub(r'\d(?=\d{4}\D*\d{4}\b)', '*', card_number)

    return masked_number




def detect_card_type(card_number):
    if card_number.startswith('5') and len(card_number) == 16:
        return 'Maestro'
    elif card_number.startswith('4') and (len(card_number) == 13 or len(card_number) == 16):
        return 'Visa Classic'
    elif card_number.startswith('4') and len(card_number) == 16:
        return 'Visa Platinum'
    elif card_number.startswith('4') and len(card_number) == 16:
        return 'Visa Gold'
    elif card_number.startswith('51') and len(card_number) == 16:
        return 'Master Card'
    else:
        return None

def mask_account_number(account_number):
    if account_number:
        return ' **' + account_number[-4:]
    return ''

if __name__ == '__main__':
    get_last_operations('operations.json')
