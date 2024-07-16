def part_a(yearly_salary, portion_saved, cost_of_dream_home):
	#########################################################################
	portion_down_payment = 0.25
	r = 0.05
	amount_saved = 0
	months = 0
	down_payment = cost_of_dream_home * portion_down_payment
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ##
	###############################################################################################
	while amount_saved <= down_payment:
	    amount_saved += amount_saved * (r / 12)
	    amount_saved += yearly_salary * (portion_saved / 12)
	    months += 1
	
	print("Number of months:", months)
	return months