# Rapport Laboratoire 0

## Questions

### Q1 : Si l'un des tests échoue à cause d'un bug, comment pytest signale-t-il l'erreur et aide-t-il à la localiser?

```bash
================================================================================= FAILURES =================================================================================
______________________________________________________________________________ test_addition _______________________________________________________________________________

    def test_addition():
        my_calculator = Calculator()
        testing_value = [
            (2, 3, 5),
            (-1, 1, 0),
            (0, 0, -1),
            (-2, -3, -5),
            (2.5, 3.5, 6.0)
        ]

        for v1, v2, expected in testing_value:
>           assert my_calculator.addition(v1, v2) == expected
E           assert 0 == -1
E            +  where 0 = addition(0, 0)
E            +    where addition = <src.calculator.Calculator object at 0x000002010BA29E50>.addition

src\tests\test_calculator.py:29: AssertionError
========================================================================= short test summary info ==========================================================================
FAILED src/tests/test_calculator.py::test_addition - assert 0 == -1
======================================================================= 1 failed, 5 passed in 0.08s ========================================================================
```
