Виджет истории операций

Это backend-алгоритм для новой функции в личном кабинете банка - виджета, который отображает последние успешные операции клиента.

ЗАДАЧА:

Реализуйте функцию, которая отображает список последних 5 операций клиента в следующем формате:

<дата перевода> <описание перевода>
<откуда> -> <куда>
<сумма перевода> <валюта>

ТРЕБОВАНИЯ:

-На экране отображаются последние 5 выполненных (EXECUTED) операций.
-Операции разделены пустой строкой.
-Дата перевода представлена в формате ДД.ММ.ГГГГ (например: 14.10.2018).
-Верхняя часть списка содержит последние операции (по дате).
-Номер карты замаскирован и не отображается полностью в формате XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбитые на блоки по 4 цифры, разделенные пробелом).
-Номер счета замаскирован и не отображается полностью в формате **XXXX (видны только последние 4 цифры номера счета).

ДАННЫЕ:

Файл со списком операций, выполненных клиентом банка:
operations.zip

Для каждой операции доступны следующие данные:

id - идентификатор транзакции
date - информация о дате операции
state - статус перевода:
EXECUTED - выполнено,
CANCELED - отменено.
operationAmount - сумма операции и валюта
description - описание типа перевода
from - откуда (может отсутствовать)
to - куда

РЕАЛИЗАЦИЯ:

Функция get_last_operations считывает данные из файла operations.json, фильтрует выполненные операции, сортирует их по дате в порядке убывания и отображает информацию о первых 5 операциях в указанном формате.
Функция mask_card_number замаскировывает номер карты в указанном формате.
Функция mask_account_number замаскировывает номер счета в указанном формате.

ПРИМЕР ВЫЗОВА ФУНКЦИИ get_last_operations:

if __name__ == '__main__':
    get_last_operations('operations.json')

ПРИМЕР ВЫХОДНЫХ ДАННЫХ ФУНКЦИИ get_last_operations:

14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.

14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.

14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.

14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.

14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.
