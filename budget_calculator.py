



def main_method():
	# each data has 3 fields a description and a value +/- , and a date
	TEST_DATA = [('paycheck', 1150, '07-20-2018'), ('rent', -850, "08-1-2018")]

	def calculate_net_cashflow(financial_data):
		net_cash = 0

		for data in financial_data:
			net_cash += data[1]
		return net_cash

	monthly_net_cashflow = calculate_net_cashflow(TEST_DATA)

	def calculate_percent_saved(financial_data):
		total_income = 0
		for data in financial_data:
			if data[0] == 'paycheck':
				total_income += data[1]

		percent_remaining = (monthly_net_cashflow * 100.0)/ total_income
		print monthly_net_cashflow, total_income
		return percent_remaining

	print calculate_percent_saved(TEST_DATA)

if __name__ == "__main__":
	main_method()
