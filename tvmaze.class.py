import requests
import json

class TVMaze:

    def getShowInfo(self, show):
        # Grabbing show info
        self.url = f'http://api.tvmaze.com/singlesearch/shows?q=:{show}'
        self.response = requests.get(self.url)
        self.data = self.response.json()
        # Grabing info about next episode
        if self.data['status'] == 'Running':
            self.next_ep_url = self.data['_links']['nextepisode']['href']
            self.next_resp = requests.get(self.next_ep_url)
            self.next_data = self.next_resp.json()


    def ShowInfo(self, show):
        self.getShowInfo(show)
        print(f"Show Name   : {self.data['name']}")
        print(f"Url         : {self.data['url']}")
        print(f"Show Type   : {self.data['type']}")
        print(f"Status      : {self.data['status']}")
        if self.data['status'] == 'Running':
            print(f"Next Episode: S{self.next_data['season']}E{self.next_data['number']}")
            print(f"Airs        : {self.next_data['airdate']}")






    def menu(self):
        print('--------------MENU---------------')
        print('1. Lookup a show')
        print('2. Show today´s schedule (US) ')
        print('3. Enter date to see schedule (US)')



if __name__ == "__main__":
    tv = TVMaze()
    while True:
        tv.menu()
        choice = input('Select a choice: ')
        if choice == '1':
            #show = input('Enter a show: ')
            tv.ShowInfo('supernatural')

