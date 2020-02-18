import requests
tvinfo = {
    "Show_name": "",
    "Show_url": "",
    "Show_type": "",
    "Show_status": "",
    "Runtime": "",
    "Next_episode": "No info",
    "Season": "No info",
    "Episode": "No info"

}
def get_show_info(show):

    api = f'http://api.tvmaze.com/singlesearch/shows?q=:{show}'
    response = requests.get(api)
    data = response.json()
    #fetching info about the show
    tvinfo['Show_name'] = data['name']
    tvinfo['Show_url'] = data['url']
    tvinfo['Show_type'] = data['type']
    tvinfo['Show_status'] = data['status']
    try:
        next_episode = data['_links']['nextepisode']['href']
        nextep = requests.get(next_episode)
        epdata = nextep.json()
        # fetching info about the next episode
        tvinfo['Next_episode'] = epdata['airdate']
        tvinfo['Season'] = epdata['season']
        tvinfo['Episode'] = epdata['number']
        tvinfo['Runtime'] = data['runtime']
    except:
        pass
    #for n in data:
    #     print(n,'<>',data[n])


    #print(tvinfo_dict['Show_name'])
    #print(tvinfo_dict['Show_type'])
    #print(tvinfo_dict['Show_status'])
    #print(tvinfo_dict['Next_episode'])
    return tvinfo


v = input('Search for show: ')
get_show_info(v)
print(f"Show: {tvinfo['Show_name']}")
print(f"Url: {tvinfo['Show_url']}")
print(f"Show type: {tvinfo['Show_type']}")
print(f"Show status: {tvinfo['Show_status']}")
print(f"Season: {tvinfo['Season']}. Episode: {tvinfo['Episode']}. Airs: {tvinfo['Next_episode']}.")
