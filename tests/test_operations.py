from prueba1_gha.operations import sum_


def test_sum_nums():
    nums = [1, 2, 3]
    assert sum_(nums) == 6


def test_sum_empty():
    nums = []
    assert sum_(nums) == 0


def test_sum_none():
    nums = None
    assert sum_(nums) == 0
