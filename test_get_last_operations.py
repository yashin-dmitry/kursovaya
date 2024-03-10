import json
from io import StringIO
import pytest

from get_last_operations import get_last_operations, mask_card_number, mask_account_number

@pytest.fixture
def operations_data():
    with open('operations.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def test_get_last_operations(capsys, operations_data):
    get_last_operations('operations.json')
    captured = capsys.readouterr()
    assert captured.out.count('\n\n') == 4

def test_mask_card_number():
    assert mask_card_number('5500 00** **** 0123') == '5500 00** **** 0123'
    assert mask_card_number('4000 00** **** 0123') == '4000 00** **** 0123'
    assert mask_card_number('400000****01234567') == '400000****01234567'
    assert mask_card_number('510000****01234567') == '510000****01234567'
    assert mask_card_number('6011 00** **** 0123') == '6011 00** **** 0123'
    assert mask_card_number('3782 82** **** 0123') == '3782 82** **** 0123'

def test_mask_account_number():
    assert mask_account_number('40817810101000000000') == ' **0000'
    assert mask_account_number('') == ''

def test_detect_card_type():
    assert detect_card_type('5500 00** **** 0123') == 'Maestro'
    assert detect_card_type('4000 00** **** 0123') == 'Visa Classic'
    assert detect_card_type('400000****01234567') == 'Visa Classic'
    assert detect_card_type('510000****01234567') == 'Master Card'
    assert detect_card_type('6011 00** **** 0123') == None
    assert detect_card_type('3782 82** **** 0123') == None
