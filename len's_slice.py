oppings = ["pepperoni", "chicken", "cheese", "sausage", "bacon", "bbq", "mushrooms"]
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizzas!")

prices = [2, 6, 1, 3, 2, 7, 2]
prices.count(2)

pizza_and_prices = [[2, "pepperoni"], [6, "chicken"], [1, "cheese"], [3, "sausage"], [2, "bacon"], [7, "bbq"], [2, "mushrooms"]]
pizza_and_prices.pop()
pizza_and_prices.append([2.5, "sausage"])
pizza_and_prices.sort()
print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[6]
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
