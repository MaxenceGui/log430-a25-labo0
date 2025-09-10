"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    assert "Calculatrice" in my_calculator.get_hello_message()

def test_get_hello_message():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

def test_addition():
    my_calculator = Calculator()
    testing_value = [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (-2, -3, -5),
        (2.5, 3.5, 6.0)
    ]

    for v1, v2, expected in testing_value:
        assert my_calculator.addition(v1, v2) == expected

def test_substraction():
    my_calculator = Calculator()
    testing_value = [
        (5, 3, 2),
        (3, 5, -2),
        (0, 0, 0),
        (-2, -3, 1),
        (2.5, 1.5, 1.0)
    ]

    for v1, v2, expected in testing_value:
        assert my_calculator.subtraction(v1, v2) == expected

def test_multiplication():
    my_calculator = Calculator()
    testing_value = [
        (2, 3, 6),
        (-1, 1, -1),
        (0, 5, 0),
        (-2, -3, 6),
        (2.5, 4, 10.0)
    ]

    for v1, v2, expected in testing_value:
        assert my_calculator.multiplication(v1, v2) == expected

def test_division():
    my_calculator = Calculator()
    testing_value = [
        (6, 3, 2),
        (5, 2, 2.5),
        (-6, -3, 2),
        (-6, 3, -2),
        (5, 0, "Erreur : division par zéro")
    ]

    for v1, v2, expected in testing_value:
        assert my_calculator.division(v1, v2) == expected
