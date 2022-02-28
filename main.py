hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#print(prices)

total_price = 0

for price in prices:
  total_price += price
# print(total_price)

average_price = total_price / (len(prices))

print("Average Hairstyle Price: " + str(average_price))

new_prices = [price - 5 for price in prices]
print(new_prices)

# Revenue portion of the Project


total_revenue = 0

# This goes through last weeks revenue
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print("Total Revenue: $" + str(total_revenue))

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# This goes through the new prices and print out the hairstyles that are 30 or lower
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] <= 30]

print(cuts_under_30)