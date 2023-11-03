import price_info
from price_info import total_cost_shopping
from price_info import cost_of_fruits

price_list = {'apple': 1.50, 'orange': 2.50, 'watermelon': 3.50}
quantity_list = {'apple': 1, 'orange': 2, 'watermelon': 3}


def test_total_cost_shopping():
    total_cost = total_cost_shopping(price_list, quantity_list)
    assert (total_cost == 17)
def test_cost_of_fruit():
    price = cost_of_fruits('papaya', 10)
    assert (price == 29.50)
