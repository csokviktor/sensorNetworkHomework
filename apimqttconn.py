import time
import json
import paho.mqtt.client as mqtt
from binance.client import Client

# MQTT details
host = ""
port = 1000
clientID = ""
topic = ""

#API details
api_key = ''
api_secret = ''


def connect_to_broker(host, port):
    #connect to mqtt broker
    client = mqtt.Client(clientID)
    client.connect(host=host, port=port)
    return client


def connect_to_api(key, secret):
    #connect to the client with secretkey
    client = Client(key, secret)
    return client


def get_total_value(client):
    #get the account info
    info = binance_client.get_account()
    return sum([float(coin['free'])*float(client.get_symbol_ticker(symbol=coin['asset']+"BUSD")['price'])
                    if not coin['asset'] == "BUSD"
                    else float(coin['free'])
                    for coin in info['balances']
                    if not (float(coin['free']) == 0.0)])


if __name__ == "__main__":
    connected_client = connect_to_broker(host=host, port=port)
    binance_client = connect_to_api(api_key, api_secret)
    while True:
        try:
            total_usd = get_total_value(binance_client)
        except:
            connected_client = connect_to_broker(host=host, port=port)
            binance_client = connect_to_api(api_key, api_secret)
            continue
        msg = {'totalusdvalue': total_usd}
        connected_client.publish(topic, json.dumps(msg))
        time.sleep(1)