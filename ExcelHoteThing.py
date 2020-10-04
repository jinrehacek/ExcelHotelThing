# Criteria:
# 1. june - september, november - february => + 40%
# 2. march - may, october => + 0%
# 3. night Sunday - Friday => +0%
# 4. night friday - sunday => +20%

# base price is 2500 czk/night

from datetime import date, timedelta

def hotel(checkin: str, checkout: str, base_price:int = 2500) -> int:
	EXPENSIVE_MONTHS = [6, 7, 8, 9, 11, 12, 1, 2]
	
	checkin = date(
		int(checkin[-4:]), 
		int(checkin[3:5]), 
		int(checkin[0:2]))
	
	checkout = date(
		int(checkout[-4:]), 
		int(checkout[3:5]), 
		int(checkout[0:2]))

	n_days = checkout - checkin
	n_days = n_days.days

	price = 0

	for x in range(0, n_days):
		day = checkin + timedelta(days=x)
		if day.weekday() == 4 or day.weekday() == 5:
			price += base_price + (base_price//5)
		else:
			price += base_price

	if checkin.month in EXPENSIVE_MONTHS:
		price += (price//100)*40

	return price

print(hotel("03.11.2020", "04.11.2020", 2500))
