import json
import pytest

from get_last_operations import get_last_operations, mask_card_number, mask_account_number, detect_card_type

@pytest.fixture
def operations_data():
    with open('operations.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def test_get_last_operations(capsys, operations_data):
    get_last_operations('operations.json')
    captured = capsys.readouterr()
    assert captured.out.count('\n\n') == 5

def test_mask_card_number():
    assert mask_card_number('55000000000001234567') == 'Счет **4567'
    assert mask_card_number('4000000000000123') == '4000 00** **** 0123'
    assert mask_card_number('4000004567012345') == '4000 00** **** 2345'
    assert mask_card_number('5100004567012345') == '5100 00** **** 2345'
    assert mask_card_number('Счет 40817810101000000000') == 'Счет **0000'
    assert mask_card_number('Неверный формат номера карты') != ('Неверный '
                                                                'формат '
                                                                'номера карты')

def test_detect_card_type():
    assert detect_card_type('5500000000000123') == 'Maestro'
    assert detect_card_type('4000000000000123') == 'Visa Classic'
    assert detect_card_type('4000004567012345') == 'Visa Classic'
    assert detect_card_type('5100004567012345') == 'Maestro'
    assert detect_card_type('6011000000000123') == None
    assert detect_card_type('3782820000000123') == None

def test_mask_account_number():
    assert mask_account_number('40817810101000000000') == ' **0000'
    assert mask_account_number('') == ''
