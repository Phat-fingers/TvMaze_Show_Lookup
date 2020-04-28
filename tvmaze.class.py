import requests
from datetime import datetime

today = datetime.today()
today = today.strftime("%Y-%m-%d")

class TVMaze:


    def getShowInfo(self, show):
        # Grabbing show info
        self.single_search_url = f'http://api.tvmaze.com/singlesearch/shows?q=:{show}'
        self.response = requests.get(self.single_search_url)
        self.data = self.response.json()
        # Grabing info about next episode
        try:
            self.next_ep_url = self.data['_links']['nextepisode']['href']
            self.next_resp = requests.get(self.next_ep_url)
            self.next_data = self.next_resp.json()
        except:
            self.noData = 'No data found'

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
                print(f'Next Episode: {self.noData}')
                print(f'Airs        : {self.noData}')

    def todaysSchedule(self, date):
        self.todays_url = f'http://api.tvmaze.com/schedule?country=US&date={date}'
        self.today_resp = requests.get(self.todays_url)
        self.today_data = self.today_resp.json()

        for show in self.today_data:
            if show['airtime'] >= '20:00':
                print('-' * 30)
                print(f"Tonight at {show['airtime']}: {show['show']['name']}")
                print(f"Show Type: {show['show']['type']}")


    def menu(self):
        print('--------------MENU---------------')
        print('1. Lookup a show')
        print('2. Show today´s schedule (US) ')
        print('3. Enter date to see schedule (US)')
        print('-'*33)


if __name__ == "__main__":
    tv = TVMaze()
    while True:
        tv.menu()
        choice = input('Select a choice: ')
        if choice not in ('1, 2, 3'):
            print('you must enter a valid number')
        elif choice == '1':
            show = input('Enter a show: ')
            tv.ShowInfo(show)
        elif choice == '2':
            tv.todaysSchedule(today)
        elif choice == '3':
            date = input('Enter a date in format (2020-01-01) ')
            tv.todaysSchedule(date)