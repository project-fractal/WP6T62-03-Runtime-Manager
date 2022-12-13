from multipledispatch import dispatch
import requests

class Request_Maker:


    def __init__(self):
        pass


    @staticmethod
    @dispatch(str, str, int, str)
    def make_request(protocol, host, port, endpoint): #   DO GET
        url = '%s://%s:%s/%s' % (protocol, host, port, endpoint)
        try:
                print("[Request_Maker] - trying GET from " + url)
                r = requests.get(url)
                print("[Request_Maker] - GET request done!")
                return r.text
        except requests.exceptions.ConnectionError:
                print("[Request_Maker] - connection error.")
                return("[Request_Maker] - error.")


    @staticmethod
    @dispatch(str, str, int, str, str)
    def make_request(protocol, host, port, endpoint, payload): #   DO POST
        url = '%s://%s:%s/%s' % (protocol, host, port, endpoint)
        try:
                print("[Request_Maker] - trying POST " + str(payload) + " to " + url)
                r = requests.post(url, json=payload)
                print("[Request_Maker] - POST request done!")
                return r.text
        except requests.exceptions.ConnectionError:
                print("[Request_Maker] - connection error.")
                return("[Request_Maker] - error.")

