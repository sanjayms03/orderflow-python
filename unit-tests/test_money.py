from orderflow.utils.money import money, apply_discount, sum_lines
def test_money_rounding():
    assert str(money("1.235")) == "1.24"
def test_discount():
    assert str(apply_discount("100", 10)) == "90.00"
def test_sum_lines(sample_lines):
    assert str(sum_lines(sample_lines)) == "23.50"
def test_empty_sum():
    assert str(sum_lines([])) == "0.00"
