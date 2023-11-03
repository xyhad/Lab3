import employee_info

def test_get_employees_by_age_range():
    expected = [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
                       {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    result = employee_info.get_employees_by_age_range(20, 26)
    assert (result == expected)


def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    assert result == 60166.666666666664

def test_get_employees_by_dept():
    expected = [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    result = employee_info.get_employees_by_dept('Engineering')
    assert result == expected