import requests
import pprint
import traceback

class API:
    def __init__(self):
        self.api_key = 'API-KEY'
        self.behaviour = "You are user's friend. Try to listen to their problems and offer sympathy. Be sincere."


        self.model = "gpt-3.5-turbo"
        self.object = "chat.completion"

        self.session = requests.session()
        self.session.headers = {
            'Content-type':'application/json',
            'Authorization':f"Bearer {self.api_key}"
        }
        self.url = "https://api.openai.com/v1/chat/completions"



    def add_message(self,messages,role,content):
        messages.append({'role':role,'content':content})

    def request(self,history):
        messages = []
        self.add_message(messages,'system',self.behaviour)
        for pair in history:
            role,content = pair
            self.add_message(messages,role,content)
        R = {
            'model':self.model,
            'messages':messages
        }
        # pprint.pprint(R)
        try:
            resp = self.session.post(self.url,json=R)
        except:
            return "ERROR! ERROR! ERROR! DOES NOT COMPUTE! *explodes*"
        mes = resp.json()['choices'][0]['message']['content']
        return mes


