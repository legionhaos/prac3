"""Проверяющая программа матрицы тест-кейсов (ПЗ 03, Вариант Б, N=17)."""
from service import check

N = 17
K = 8 + N % 5


def report(case, expected, actual):
    status = "PASS" if actual == expected else "FAIL"
    print(case, expected, actual, status, sep=" | ")


def main():
    cases = [
        ([0, 60], "OK"),
        ([30] * K, "OK"),
        (None, "TYPE"),
        ([], "EMPTY"),
        ([30, True], "BAD_ITEM"),
        ([61], "BAD_ITEM"),
        ([-1], "BAD_ITEM"),
        ([None] * (K + 1), "OVERLOAD"),
    ]
    for i, (values, expected) in enumerate(cases, 1):
        report(f"Б-{i:02}", expected, check(values, K))

    actual = (check([30] * (1000 * K), K), check([30], K))
    report("Б-09", ("OVERLOAD", "OK"), actual)


if __name__ == "__main__":
    main()
