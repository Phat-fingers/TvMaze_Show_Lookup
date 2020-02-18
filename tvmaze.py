import requests
import json
tvinfo_dict = {
    "Show_name": "",
    "Show_url": "",
    "Show_type": "",
    "Show_status": "",
    "Runtime": "",
    "Next_episode": "",
    "Season": "",
    "Episode": ""

}
def get_show_info(show):

    api = f'http://api.tvmaze.com/singlesearch/shows?q=:{show}'
    resp = requests.get(api)
    data = resp.json()
    da = json.dumps(data, indent=2)
    tvinfo_dict['Show_name'] = data['name']
    tvinfo_dict['Show_url'] = data['url']
    tvinfo_dict['Show_type'] = data['type']
    tvinfo_dict['Show_status'] = data['status']
    #for n in data:
    #     print(n,'<>',data[n])
    if data['status'] == 'Ended':
         print(tvinfo_dict['Show_name'] + ' '+ tvinfo_dict['Show_url'] + ' ' + tvinfo_dict['Show_status'])
    else:
        next_episode = data['_links']['nextepisode']['href']
        nextep = requests.get(next_episode)
        epdata = nextep.json()
        #print(epdata)


        tvinfo_dict['Next_episode'] = epdata['airdate']
        tvinfo_dict['Season'] = epdata['season']
        tvinfo_dict['Episode'] = epdata['number']
        tvinfo_dict['Runtime'] = data['runtime']


        # print(tvinfo_dict['Show_name'])
        # print(tvinfo_dict['Show_type'])
        # print(tvinfo_dict['Show_status'])
        # print(tvinfo_dict['Next_episode'])
        return tvinfo_dict


v = input('Search for show')
get_show_info(v)
print(tvinfo_dict)