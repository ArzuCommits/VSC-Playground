import faker
import random as rand
import forex_python.converter

# user = input('Enter a data: ')
# rateimport forex_python.converter

usd_inr = forex_python.converter.convert(1,'USD', 'INR')

print(f"1 USD = {usd_inr} INR")
# rate  = forex_python.converter.CurrencyRates()
# value = rate.get_rates('USD','INR')
# print(value)
# sdfchear