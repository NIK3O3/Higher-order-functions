from __future__ import annotations

import argparse
from typing import Any, Callable, Iterable, TypeVar


T = TypeVar("T")
R = TypeVar("R")
A = TypeVar("A")


# ---------------------------------------------------------------------------
# Допоміжні функції
# ---------------------------------------------------------------------------

def print_header(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


# ---------------------------------------------------------------------------
# Завдання 1. Визначення функції вищого порядку
# ---------------------------------------------------------------------------

def apply(func: Callable[[T], R], x: T) -> R:
    """
    Функція вищого порядку.

    Вона приймає іншу функцію func як аргумент і застосовує її до x.
    """
    return func(x)


def task_1_apply() -> None:
    print_header("Завдання 1. Визначення функції вищого порядку")

    result_1 = apply(lambda x: x * 2, 5)
    result_2 = apply(lambda x: x + 10, 5)

    print(f"apply(lambda x: x * 2, 5) = {result_1}")
    print(f"apply(lambda x: x + 10, 5) = {result_2}")

    print(
        "\nПояснення:\n"
        "- apply є функцією вищого порядку, бо приймає іншу функцію як аргумент.\n"
        "- Поведінка apply залежить від того, яку функцію передати в параметр func."
    )


# ---------------------------------------------------------------------------
# Завдання 2. Передача поведінки
# ---------------------------------------------------------------------------

def calculate(
    operation: Callable[[int | float, int | float], int | float],
    a: int | float,
    b: int | float,
) -> int | float:
    """
    Виконує операцію над двома числами.

    operation — це поведінка, яку ми передаємо ззовні.
    """
    return operation(a, b)


def task_2_calculate() -> None:
    print_header("Завдання 2. Передача поведінки")

    addition = lambda a, b: a + b
    multiplication = lambda a, b: a * b
    power = lambda a, b: a ** b

    print(f"calculate(addition, 2, 3) = {calculate(addition, 2, 3)}")
    print(f"calculate(multiplication, 4, 5) = {calculate(multiplication, 4, 5)}")
    print(f"calculate(power, 2, 4) = {calculate(power, 2, 4)}")

    print(
        "\nПояснення:\n"
        "- calculate не знає наперед, яку саме операцію виконувати.\n"
        "- Конкретна поведінка передається через параметр operation."
    )


# ---------------------------------------------------------------------------
# Завдання 3. Узагальнення обробки списку
# ---------------------------------------------------------------------------

def transform(data: Iterable[T], func: Callable[[T], R]) -> list[R]:
    """
    Універсальна функція перетворення колекції.

    Замість жорстко прописаного x * 2 використовується func.
    """
    result = []

    for x in data:
        result.append(func(x))

    return result


def task_3_transform() -> None:
    print_header("Завдання 3. Узагальнення обробки списку")

    data = [1, 2, 3, 4, 5]

    doubled = transform(data, lambda x: x * 2)
    squared = transform(data, lambda x: x * x)
    as_strings = transform(data, lambda x: str(x))

    print(f"data = {data}")
    print(f"Подвоєння: {doubled}")
    print(f"Квадрати: {squared}")
    print(f"Рядки: {as_strings}")

    print(
        "\nПояснення:\n"
        "- Початковий код був прив'язаний тільки до x * 2.\n"
        "- transform приймає функцію func, тому може виконувати будь-яке перетворення."
    )


# ---------------------------------------------------------------------------
# Завдання 4. Універсальна функція обробки
# ---------------------------------------------------------------------------

def process(
    data: Iterable[T],
    transform_func: Callable[[T], R],
    predicate: Callable[[T], bool],
) -> list[R]:
    """
    Спочатку фільтрує елементи через predicate, потім перетворює через transform_func.
    """
    result = []

    for x in data:
        if predicate(x):
            result.append(transform_func(x))

    return result


def task_4_process() -> None:
    print_header("Завдання 4. Універсальна функція обробки")

    data = [1, 2, 3, 4, 5, 6]

    result = process(
        data,
        transform_func=lambda x: x * x,
        predicate=lambda x: x % 2 == 0,
    )

    print(f"data = {data}")
    print("predicate: парні числа")
    print("transform: квадрат значення")
    print(f"Результат: {result}")

    print(
        "\nПояснення:\n"
        "- predicate вирішує, які елементи залишити.\n"
        "- transform_func вирішує, як перетворити залишені елементи.\n"
        "- process є функцією вищого порядку, бо приймає дві функції."
    )


# ---------------------------------------------------------------------------
# Завдання 5. Реалізація map
# ---------------------------------------------------------------------------

def map_custom(func: Callable[[T], R], data: Iterable[T]) -> list[R]:
    """Власна реалізація map."""
    result = []

    for x in data:
        result.append(func(x))

    return result


def task_5_map_custom() -> None:
    print_header("Завдання 5. Реалізація map")

    data = [1, 2, 3, 4, 5]

    print(f"data = {data}")
    print(f"map_custom(lambda x: x * 2, data) = {map_custom(lambda x: x * 2, data)}")
    print(f"map_custom(lambda x: x * x, data) = {map_custom(lambda x: x * x, data)}")

    print(
        "\nПояснення:\n"
        "- map_custom проходить по кожному елементу data.\n"
        "- До кожного елемента застосовується func.\n"
        "- Результати збираються в новий список."
    )


# ---------------------------------------------------------------------------
# Завдання 6. Реалізація filter
# ---------------------------------------------------------------------------

def filter_custom(func: Callable[[T], bool], data: Iterable[T]) -> list[T]:
    """Власна реалізація filter."""
    result = []

    for x in data:
        if func(x):
            result.append(x)

    return result


def task_6_filter_custom() -> None:
    print_header("Завдання 6. Реалізація filter")

    data = [1, 2, 3, 4, 5, 6]

    print(f"data = {data}")
    print(f"filter_custom(lambda x: x % 2 == 0, data) = {filter_custom(lambda x: x % 2 == 0, data)}")
    print(f"filter_custom(lambda x: x > 3, data) = {filter_custom(lambda x: x > 3, data)}")

    print(
        "\nПояснення:\n"
        "- filter_custom залишає тільки ті елементи, для яких func(x) повертає True."
    )


# ---------------------------------------------------------------------------
# Завдання 7. Реалізація reduce
# ---------------------------------------------------------------------------

def reduce_custom(func: Callable[[A, T], A], data: Iterable[T], initial: A) -> A:
    """Власна реалізація reduce."""
    accumulator = initial

    for x in data:
        accumulator = func(accumulator, x)

    return accumulator


def task_7_reduce_custom() -> None:
    print_header("Завдання 7. Реалізація reduce")

    data = [1, 2, 3, 4, 5]

    total = reduce_custom(lambda acc, x: acc + x, data, 0)
    product = reduce_custom(lambda acc, x: acc * x, data, 1)
    maximum = reduce_custom(lambda acc, x: acc if acc > x else x, data, data[0])

    print(f"data = {data}")
    print(f"Сума: {total}")
    print(f"Добуток: {product}")
    print(f"Максимум: {maximum}")

    print(
        "\nПояснення:\n"
        "- reduce_custom зводить колекцію до одного значення.\n"
        "- accumulator зберігає проміжний результат."
    )


# ---------------------------------------------------------------------------
# Завдання 8. Комбінування
# ---------------------------------------------------------------------------

def task_8_combination() -> None:
    print_header("Завдання 8. Комбінування")

    result = reduce_custom(
        lambda acc, x: acc + x,
        map_custom(lambda x: x * x, [1, 2, 3, 4]),
        0,
    )

    print("reduce_custom(lambda acc, x: acc + x, map_custom(lambda x: x*x, [1,2,3,4]), 0)")
    print(f"Результат: {result}")

    print(
        "\nПояснення:\n"
        "- map_custom спочатку створює список квадратів: [1, 4, 9, 16].\n"
        "- reduce_custom потім підсумовує ці значення.\n"
        "- Загальний результат: 30."
    )


# ---------------------------------------------------------------------------
# Завдання 9. Генератор функцій
# ---------------------------------------------------------------------------

def multiplier(n: int | float) -> Callable[[int | float], int | float]:
    """
    Повертає нову функцію, яка множить значення на n.
    """
    def inner(x: int | float) -> int | float:
        return x * n

    return inner


def task_9_function_generator() -> None:
    print_header("Завдання 9. Генератор функцій")

    double = multiplier(2)
    triple = multiplier(3)
    multiply_by_10 = multiplier(10)

    print(f"double(5) = {double(5)}")
    print(f"triple(5) = {triple(5)}")
    print(f"multiply_by_10(7) = {multiply_by_10(7)}")

    numbers = [1, 2, 3, 4, 5]

    print(f"\nnumbers = {numbers}")
    print(f"list(map(double, numbers)) = {list(map(double, numbers))}")
    print(f"list(map(triple, numbers)) = {list(map(triple, numbers))}")

    print(
        "\nПояснення:\n"
        "- multiplier є функцією вищого порядку, бо повертає іншу функцію.\n"
        "- inner пам'ятає n завдяки замиканню."
    )


# ---------------------------------------------------------------------------
# Завдання 10. Closure
# ---------------------------------------------------------------------------

def make_filter(n: int | float) -> Callable[[int | float], bool]:
    """
    Повертає predicate-функцію, яка перевіряє value > n.
    """
    def inner(value: int | float) -> bool:
        return value > n

    return inner


def task_10_closure() -> None:
    print_header("Завдання 10. Closure")

    greater_than_10 = make_filter(10)
    greater_than_100 = make_filter(100)

    numbers = [5, 10, 15, 50, 100, 150]

    print(f"numbers = {numbers}")
    print(f"greater_than_10(15) = {greater_than_10(15)}")
    print(f"greater_than_10(5) = {greater_than_10(5)}")
    print(f"list(filter(greater_than_10, numbers)) = {list(filter(greater_than_10, numbers))}")
    print(f"list(filter(greater_than_100, numbers)) = {list(filter(greater_than_100, numbers))}")

    print(
        "\nПояснення:\n"
        "- make_filter(10) повертає функцію inner.\n"
        "- inner пам'ятає n = 10 навіть після завершення make_filter.\n"
        "- Це називається замиканням."
    )


# ---------------------------------------------------------------------------
# Завдання 11. Compose
# ---------------------------------------------------------------------------

def compose(f: Callable[[R], A], g: Callable[[T], R]) -> Callable[[T], A]:
    """
    Повертає композицію двох функцій.

    compose(f, g)(x) == f(g(x))
    """
    def composed(x: T) -> A:
        return f(g(x))

    return composed


def task_11_compose() -> None:
    print_header("Завдання 11. Compose")

    double = lambda x: x * 2
    square = lambda x: x * x

    square_then_double = compose(double, square)
    double_then_square = compose(square, double)

    print(f"square_then_double = compose(double, square)")
    print(f"square_then_double(3) = {square_then_double(3)}")
    print(f"double_then_square = compose(square, double)")
    print(f"double_then_square(3) = {double_then_square(3)}")

    print(
        "\nПояснення:\n"
        "- compose(f, g) створює нову функцію.\n"
        "- Спочатку виконується g(x), потім f(result).\n"
        "- Порядок має значення: compose(double, square) і compose(square, double) можуть давати різні результати."
    )


# ---------------------------------------------------------------------------
# Завдання 12. Розширена композиція
# ---------------------------------------------------------------------------

def compose_many(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """
    Композиція багатьох функцій справа наліво.

    compose_many(f3, f2, f1)(x) == f3(f2(f1(x)))
    """
    def composed(x: Any) -> Any:
        result = x

        for func in reversed(funcs):
            result = func(result)

        return result

    return composed


def task_12_compose_many() -> None:
    print_header("Завдання 12. Розширена композиція")

    add_1 = lambda x: x + 1
    double = lambda x: x * 2
    square = lambda x: x * x

    combined = compose_many(square, double, add_1)

    print("combined = compose_many(square, double, add_1)")
    print("Це означає: square(double(add_1(x)))")
    print(f"combined(3) = {combined(3)}")

    print(
        "\nПояснення:\n"
        "- Для x = 3 спочатку add_1: 4.\n"
        "- Потім double: 8.\n"
        "- Потім square: 64."
    )


# ---------------------------------------------------------------------------
# Завдання 13. Pipeline
# ---------------------------------------------------------------------------

def pipeline(data: Any, steps: list[Callable[[Any], Any]]) -> Any:
    """
    Послідовно застосовує steps зліва направо.

    На відміну від compose_many, pipeline зазвичай читається як послідовність етапів обробки.
    """
    result = data

    for step in steps:
        result = step(result)

    return result


def task_13_pipeline() -> None:
    print_header("Завдання 13. Pipeline")

    result = pipeline(
        [1, 2, 3, 4, 5],
        [
            lambda xs: list(filter(lambda x: x % 2 == 0, xs)),
            lambda xs: list(map(lambda x: x * x, xs)),
        ],
    )

    print(
        "pipeline(\n"
        "    [1,2,3,4,5],\n"
        "    [\n"
        "        lambda xs: list(filter(lambda x: x%2==0, xs)),\n"
        "        lambda xs: list(map(lambda x: x*x, xs))\n"
        "    ]\n"
        ")"
    )
    print(f"Результат: {result}")

    print(
        "\nПояснення:\n"
        "- Перший крок залишає тільки парні числа: [2, 4].\n"
        "- Другий крок підносить їх до квадрату: [4, 16].\n"
        "- pipeline є функцією вищого порядку, бо приймає список функцій steps."
    )


# ---------------------------------------------------------------------------
# Фінальний висновок
# ---------------------------------------------------------------------------

def print_final_conclusion() -> None:
    print_header("Висновок")

    print(
        "Функція вищого порядку — це функція, яка приймає іншу функцію як аргумент "
        "або повертає функцію як результат.\n\n"
        "Приклади з роботи:\n"
        "- apply(func, x) приймає функцію func;\n"
        "- calculate(operation, a, b) приймає операцію як параметр;\n"
        "- multiplier(n) повертає нову функцію;\n"
        "- compose(f, g) створює нову функцію з двох інших;\n"
        "- pipeline(data, steps) приймає список функцій і виконує їх послідовно.\n\n"
        "Функції вищого порядку дозволяють передавати поведінку як дані, "
        "будувати гнучкі pipeline і зменшувати дублювання коду."
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_selected_task(task_number: str) -> None:
    tasks: dict[str, Callable[[], None]] = {
        "1": task_1_apply,
        "2": task_2_calculate,
        "3": task_3_transform,
        "4": task_4_process,
        "5": task_5_map_custom,
        "6": task_6_filter_custom,
        "7": task_7_reduce_custom,
        "8": task_8_combination,
        "9": task_9_function_generator,
        "10": task_10_closure,
        "11": task_11_compose,
        "12": task_12_compose_many,
        "13": task_13_pipeline,
    }

    if task_number == "all":
        for number in map(str, range(1, 14)):
            tasks[number]()
        print_final_conclusion()
        return

    if task_number not in tasks:
        available = ", ".join(["all"] + list(tasks.keys()))
        raise ValueError(f"Невідоме завдання: {task_number}. Доступні варіанти: {available}")

    tasks[task_number]()


def main() -> None:
    parser = argparse.ArgumentParser(description="Завдання з функцій вищого порядку у Python")
    parser.add_argument(
        "--task",
        default="all",
        help="Номер завдання: 1..13 або all. За замовчуванням: all",
    )

    args = parser.parse_args()
    run_selected_task(args.task)


if __name__ == "__main__":
    main()
