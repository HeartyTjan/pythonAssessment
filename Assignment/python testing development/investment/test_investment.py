import unittest
import investment

class TestInvestment(unittest.TestCase) :
	
	def test_investment_function_exist(self):
		investment.get_future_investment(100,12,3)

	def test_investment_function__raise_error_with_negative_amount(self) :
		self.assertRaises(ValueError, investment.get_future_investment, -100.00, -10,-5)

	def test_investment_function__raise_error_for_month_and_year_with_non_integer(self):
		self.assertRaises(TypeError,investment.get_future_investment,"100",10.2,5.0)
	
	def test_investment_function_return_floating_value_and_result(self) :
		
		self.assertEqual(investment.get_future_investment(10000,5,3), 11614.72)
