import requests
import json


class TVMaze:

    def getShowInfo(self, show):
        # Grabbing show info
        self.url = f'http://api.tvmaze.com/singlesearch/shows?q=:{show}'
        self.response = requests.get(self.url)
        self.data = self.response.json()
        # Grabing info about next episode
        try:
            self.next_ep_url = self.data['_links']['nextepisode']['href']
            self.next_resp = requests.get(self.next_ep_url)
            self.next_data = self.next_resp.json()
        except:
            pass

    def ShowInfo(self, show):
        self.getShowInfo(show)
        print(f"Show Name   : {self.data['name']}")
        print(f"Url         : {self.data['url']}")
        print(f"Show Type   : {self.data['type']}")
        print(f"Status      : {self.data['status']}")
        if self.data['status'] == 'Running':
            try:
                print(f"Next Episode: S{self.next_data['season']}E{self.next_data['number']}")
                print(f"Airs        : {self.next_data['airdate']}")
            except:
                print('Next Episode: N/A')
                print('Airs        : N/A')

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
            show = input('Enter a show: ')
            tv.ShowInfo(show)
