def candyStoreminimum(no_of_candies,prices,  free_candies):
	var1 = 0
	var2 = 0
	while(no_of_candies>1):
		var1 += prices[var2]
		no_of_candies = no_of_candies-free_candies
		var2 += 1
	return var1
def candyStoremaximum(no_of_candies,prices,  free_candies):
	var1 = 0
	index = 0
	var2 = no_of_candies-1
	while(var2 >= index):
		var1 += prices[var2]
		index += free_candies
		var2 -= 1
	return var1
prices = [3, 2, 1, 4]
no_of_candies = len(prices)
free_candies = 2
prices.sort()
# print("Minimum prize is----->>>",
# 	  candyStoreminimum(no_of_candies,prices, free_candies),
# 	  "\t\t\tAnd maximum prize is----->>> ",
# 	  candyStoremaximum(no_of_candies,prices,  free_candies))
if len(prices)>1 and len(prices)<100000 :
	candyStoreminimum(no_of_candies,prices, free_candies)
	candyStoremaximum(no_of_candies,prices,  free_candies)
else:
	print("variety of candies must be grater than 1 and less than 100000")