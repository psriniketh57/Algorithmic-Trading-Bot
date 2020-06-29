import requests, json
from chalice import Chalice

app = Chalice(app_name='tradingview-webhook-alert')

API_KEY = 'PKZAFNPXEIA6ULM2L4V3'
SECRET_KEY = 'e3Rxik4NAta0uCqFrxjON9ZOOvfyJi34I3LwjBnX'
BASE_URL = "https://paper-api.alpaca.markets"
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}

@app.route('/buy_stock', methods=['POST'])
def buy_stock():
    request = app.current_request
    webhook_message = request.json_body

    data = {
        "symbol": webhook_message['ticker'],
        "qty": 10,
        "side": "buy",
        "type": "market",
        #"type": "limit",
        #"limit_price": webhook_message['close'],
        "time_in_force": "gtc",
        #"order_class": "bracket",
        #"take_profit": {
         #   "limit_price": webhook_message['close'] * 1.05
        #},
        "stop_loss": {
            "stop_price": webhook_message['close'] * 0.98,
        }
    }

    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)

    response = json.loads(r.content)

    return {
        'webhook_message': webhook_message,
        'id': response['id'],
        'client_order_id': response['client_order_id'],
        'response': response
    }

@app.route('/sell_stock', methods=['POST'])
def sell_stock():
    request = app.current_request
    webhook_message = request.json_body

    data = {
        "symbol": webhook_message['ticker'],
        "qty": 10,
        "side": "sell",
        "type": "market",
        "time_in_force": "gtc",
    }

    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)

    response = json.loads(r.content)

    return {
        'webhook_message': webhook_message,
        'id': response['id'],
        'client_order_id': response['client_order_id']
    }



# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#