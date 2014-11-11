Salary = input("your salary: ")
Price = input("Dolcy price: ")
Offer = input("how many papers do you need to get a free Dolcy: ")


tot = Salary/Price
papers = tot
while papers >= Offer:
	free_dolcy = papers/Offer
	tot = tot + free_dolcy
	papers = papers + free_dolcy - (free_dolcy*Offer)

print tot
