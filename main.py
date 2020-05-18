from web3 import Web3
import urllib.request, json
import decimal

w3 = Web3(Web3.HTTPProvider("https://rpc.ether1.cloud"))

# Replace the address below with your own
balance = w3.eth.getBalance('0xefa3DbfDD4d9a14B9F0dc3F6c06582C7eAfe3066')

balance_formatted = w3.fromWei(balance, 'ether')

pizza_cost = 4.99

with urllib.request.urlopen(
        "https://min-api.cryptocompare.com/data/price?fsym=ETHO&tsyms=USD"
) as url:
    data = json.loads(url.read().decode())

wallet_value = balance_formatted * decimal.Decimal(data["USD"])

pizza_count = wallet_value / decimal.Decimal(pizza_cost)

print("Balance in Wei: " + str(balance))
print("Price of a Pizza: $" + str(pizza_cost))
print("Balance in ETHO: " + str(balance_formatted))
print("Value of 1 ETHO in USD: $" + str(data["USD"]))
print("Current Value of your Ether-1 Wallet in USD: $" +
      str(format(wallet_value, '.2f')))
print("You can currently afford " + str(format(pizza_count, '.2f')) +
      " pizzas from Little Ceasars")
