"""Модуль приёма пакета телеметрии давления (ПЗ 03, Вариант Б)."""


def check(values, capacity):
    """Проверяет пакет отсчётов давления и возвращает код статуса."""
    if not isinstance(values, list):
        return "TYPE"
    if not values:
        return "EMPTY"
    if len(values) > capacity:
        return "OVERLOAD"
    for x in values:
        if type(x) not in (int, float) or not 0 <= x <= 60:
            return "BAD_ITEM"
    return "OK"
