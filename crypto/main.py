import requests
import json
api_request=requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=100&convert=USD&CMC_PRO_API_KEY=d4736c89-f405-436f-8969-e6e4380c46ce')
api=json.loads(api_request.content)
# hi 

coinss=[
    {
        'symbol':'BTC',
        'amount_owned':2,
        'price_per_coin':3200
    },
    {
        'symbol': 'EOS',
        'amount_owned':100,
        'price_per_coin':2.05
    }
]

over_all_profit_loss=0
for i in range(0,50):
    for coin in coinss:
        if(api['data'][i]['symbol'])==coin['symbol']:

            total_amount=coin['amount_owned']*coin['price_per_coin']

            current_value=coin['amount_owned']*api['data'][i]['quote']['USD']['price']

            print(api['data'][i]['name'] +'-'+ api['data'][i]['symbol'])

            print('price-${0:.2f}'.format(api['data'][i]['quote']['USD']['price']))
            print('total_number_of_coins',coin['amount_owned'])
            print('total_amount_paid','${0:.2f}'.format(total_amount))
            print('current_value-',current_value)

            profit_loss=(api['data'][i]['quote']['USD']['price']-coin['price_per_coin'])

            total_profit_loss=(profit_loss*coin['amount_owned'])

            print('profit_loss','${0:.2f}'.format(profit_loss))

            print("total_profit_loss",'${0:.2f}'.format(total_profit_loss))

            over_all_profit_loss=over_all_profit_loss+total_profit_loss

            print('-----------------')

print("OVER_ALL_PROFIT_LOSS",'${0:.2f}'.format(over_all_profit_loss))
