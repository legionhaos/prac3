"""Испытание восстановления после перегрузки (ПЗ 03, Вариант Б, Б-10)."""
from time import perf_counter
from service import check
from check import N, K, report


def main():
    start = perf_counter()
    res_overload = check([30] * (1000 * K), K)
    res_recovery = check([30] * K, K)
    elapsed_ms = (perf_counter() - start) * 1000

    actual = (res_overload, res_recovery)
    report("Б-10", ("OVERLOAD", "OK"), actual)
    print(f"Время одного прогона Б-10 (N={N}, K={K}): {elapsed_ms:.4f} мс")


if __name__ == "__main__":
    main()
