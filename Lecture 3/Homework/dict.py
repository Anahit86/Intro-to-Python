market = {"dairy":["yogurt", "cheese"], "fruits": ['banana', 'apple', 'orange', 'lemon', 'apple', 'banana','banana']}
market["candies"] = ['mars','kinder', 'twix']
print(market)
a1 = set(market["fruits"])
market["fruits"] = list(a1)
print(market)
