import tkinter
from tkinter import Tk
import requests
import json
pycryto =Tk()

pycryto.title('MY CRYPTO')

def my_pycrpto():
    api_request = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=100&convert=USD&CMC_PRO_API_KEY=d4736c89-f405-436f-8969-e6e4380c46ce')
    api = json.loads(api_request.content)

    coinss = [
        {
            'symbol': 'BTC',
            'amount_owned': 2,
            'price_per_coin': 3200
        },
        {
            'symbol': 'EOS',
            'amount_owned': 100,
            'price_per_coin': 2.05
        }
    ]

    over_all_profit_loss = 0

    for i in range(0, 50):
        for coin in coinss:
            if (api['data'][i]['symbol']) == coin['symbol']:
                total_amount = coin['amount_owned'] * coin['price_per_coin']

                current_value = coin['amount_owned'] * api['data'][i]['quote']['USD']['price']

                print(api['data'][i]['name'] + '-' + api['data'][i]['symbol'])

                #print('price-${0:.2f}'.format(api['data'][i]['quote']['USD']['price']))
                #print('total_number_of_coins', coin['amount_owned'])
                #print('total_amount_paid', '${0:.2f}'.format(total_amount))
                #print('current_value-','${0:.2f}'.format( current_value))

                profit_loss = (api['data'][i]['quote']['USD']['price'] - coin['price_per_coin'])

                total_profit_loss = (profit_loss * coin['amount_owned'])

                #print('profit_loss', '${0:.2f}'.format(profit_loss))

                #print("total_profit_loss", '${0:.2f}'.format(total_profit_loss))

                over_all_profit_loss = over_all_profit_loss + total_profit_loss

                name = tkinter.Label(pycryto, text=api['data'][i]['symbol']), bg='black', fg='white').grid(row=0, column=0)
                price = tkinter.Label(pycryto, text='${0:.2f}'.format(api['data'][i]['quote']['USD']['price']), bg='black', fg='white').grid(row=1, column=1)
                nO_coins = tkinter.Label(pycryto, text=coin['amount_owned'], bg='black', fg='white').grid(row=2, column=2)
                amount_paid = tkinter.Label(pycryto, text='${0:.2f}'.format(total_amount), bg='black', fg='white').grid(row=3,
                                                                                                             column=3)
                current_val = tkinter.Label(pycryto, text='${0:.2f}'.format( current_value), bg='black', fg='white').grid(row=4,
                                                                                                         column=4)
                profitloss = tkinter.Label(pycryto, text='${0:.2f}'.format(profit_loss), bg='black', fg='white').grid(row=5, column=5)
                total_pl = tkinter.Label(pycryto, text='${0:.2f}'.format(total_profit_loss), bg='black', fg='white').grid(row=6,
                                                                                                          column=6)


                print('-----------------')

            my_pycrpto()
    print("OVER_ALL_PROFIT_LOSS", '${0:.2f}'.format(over_all_profit_loss))

name = tkinter.Label(pycryto, text="COIN NAME",bg='black',fg='white').grid(row=0, column=0)
price = tkinter.Label(pycryto, text="PRICE:",bg='black',fg='white').grid(row=0, column=1)
nO_coins = tkinter.Label(pycryto, text="NO.COINS:",bg='black',fg='white').grid(row=0, column=2)
amount_paid = tkinter.Label(pycryto, text="TOTAL AMOUNT PAID:",bg='black',fg='white').grid(row=0, column=3)
current_val= tkinter.Label(pycryto, text="CURRENT VALUE",bg='black',fg='white').grid(row=0, column=4)
profitloss= tkinter.Label(pycryto, text="PROFIT LOSS",bg='black',fg='white').grid(row=0, column=5)
total_pl = tkinter.Label(pycryto, text="TOTAL PROFIT LOSS",bg='black',fg='white').grid(row=0, column=6)



print('program completed')
pycryto.mainloop()
