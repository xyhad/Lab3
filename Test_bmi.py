import Lab2.bmi
def test_bmi_under_weight():
    height = 1.90
    weight = 50
    result = Lab2.bmi.calculate_bmi(height, weight)
    test_value = -1
    assert (result == test_value)
def test_bmi_normal_weight():
    height = 1.90
    weight = 70
    result = Lab2.bmi.calculate_bmi(height, weight)
    test_value = 0
    assert (result == test_value)
def test_bmi_over_weight():
    height = 1.90
    weight = 100
    result = Lab2.bmi.calculate_bmi(height, weight)
    test_value = 1
    assert (result == test_value)