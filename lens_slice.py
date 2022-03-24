# https://www.codecademy.com/courses/learn-python-3/projects/python-lens-slice
# Q1
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Q2
prices = [2, 6, 1, 3, 2, 7, 2]

# Q3
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Q4
num_pizzas = len(toppings)

# Q5
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# Q6
pizza_and_prices = [
  [2,	"pepperoni"],
  [6,	"pineapple"],
  [1,	"cheese"],
  [3,	"sausage"],
  [2,	"olives"],
  [7,	"anchovies"],
  [2,	"mushrooms"]
]

# Q7
print(pizza_and_prices)

# Q8
pizza_and_prices.sort()

# Q9
cheapest_pizza = pizza_and_prices[0]

# Q10
priciest_pizza = pizza_and_prices[-1]

# Q11
# works with remove method
# pizza_and_prices.remove(priciest_pizza)
# but exercise says use pop and remove the last element
pizza_and_prices.pop()

# Q12
# print("\n", pizza_and_prices)
pizza_and_prices.insert(4, [2.5, "peppers"])
print("\n", pizza_and_prices)

# Q13
three_cheapest = pizza_and_prices[:3]

# Q14
print("\n", three_cheapest)