import sys, os
import webbrowser as web
import Sal


# Personal Assistant Bot - Opens up daily charts and information about crypto-currency
# Version 1.4.0.
# -----------------------Beginning of Program ------------------
name = 'Tyler'
greeting = 'Hello Master {}, and what can I assist you with today?\n'.format(name)
affirm = ('Your wish is my command, sir.\n')

print(greeting)

# URL dictionary
url_dict = {'tradingViewURL': 'https://www.tradingview.com/chart/MXFuP9og/',
                'coinMarketCapURL': 'https://coinmarketcap.com/charts/',
                'nanexURL': 'https://nanex.co/exchange/BTCPNANO/',
                'twitterURL': 'https://twitter.com/?lang=en',
                'coinDeskURL': 'https://www.coindesk.com/'}

while True:
    order = input().lower()
    if 'chart' in order:
        if 'twitter' in order:
            print(affirm)
            web.open(url_dict['tradingViewURL'])
            web.open(url_dict['nanexURL'])
            web.open(url_dict['twitterURL'])
            print('Charts & Twitter Task Complete.\n')
            break
        
        elif 'news' in order:
            print(affirm)
            web.open(url_dict['tradingViewURL'])
            web.open(url_dict['nanexURL'])
            web.open(url_dict['twitterURL'])
            web.open(url_dict['coinDeskURL'])
            print('Charts & News Task Complete.\n')
            break
        
        else:
            print(affirm)
            web.open(url_dict['tradingViewURL'])
            web.open(url_dict['nanexURL'])
            web.open(url_dict['coinMarketCapURL'])
            print('Charts Task Complete.\n')
            break

    elif 'twitter' in order:
        print(affirm)
        web.open(url_dict['twitterURL'])
        print('Twitter Task Complete.\n')
        break

    elif 'news' in order:
        print(affirm)
        web.open(url_dict['twitterURL'])
        web.open(url_dict['coinDeskURL'])
        print('News Task Complete.\n')
        break

    elif 'quit' in order:
        print('Goodbye, Master {}.'.format(name))
        break

    else:
        print('I am waiting for a command, Master {}.'.format(name))
    # Must contain Sal.py in same directory
    if 'sync' in order:
        print('Repeat Command')
        os.system('Sal.py')

print('Closing....')
print('Done.')
sys.exit()
print('FAULT')
