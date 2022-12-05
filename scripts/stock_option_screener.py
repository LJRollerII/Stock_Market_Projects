# Let's Define Options

# Call Option: Rights but not obligation to buy a certian assest up to a certain date.
# Put Option: Rights but not obligation to sell a certian assest up to a certain date.

from yahoo_fin import options
import pandas as pd

# Use the code for the company you are interested in seeing stock options in.
stock = 'AAPL'

print(options.get_expiration_dates(stock))

pd.set_option('display.max_columns', None)
chain = options.get_options_chain(stock)
print(chain)

# If we wanted to just see the call options you would use this code in the above print statement:
# print(chain['calls'])
# You can also do chain = options.get_calls(stock) then print(chain) on the line below as an alternative.

# If we wanted to just see the put options you would use this code in the above print statement:
# print(chain['puts'])
# You can also do chain = options.get_puts(stock) then print(chain) on the line below as an alternative.

#If we wanted to see the options that expire on a certain date, you would use this example of code where the chain variable is defined:
# chain = options.get_options_chain(stock, 'January 10, 2023')

# We can customize what you want to print in the chain.
# Example if we wanted to know what options have a strike price less than $100 we would use:
# print(chain[chain['Strike'] < 100])
# Example 2  print(chain[chain['Ask'] < 100][chain['Strike'] < 100])
