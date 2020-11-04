import re
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    print('Welcome to Music Map Scraper\nThe data is received from the www.music-map.com\n')
    artist_name = input('Please enter your favorite artist or band : ')
    try:
        website_address = 'https://www.music-map.com/{0}'.format(artist_name)
        page = requests.get(website_address)
        soup = BeautifulSoup(page.content, 'html.parser')
        musicMap = soup.find(id='gnodMap')
        artists = musicMap.find_all(id=re.compile('^s[1-48]'))
        for artist in artists:
            print(artist.get_text())
    except AttributeError:
        print('Artist not found ! \nPlease enter artist name correctly')
    except ConnectionError:
        print('Not connected ! \nPlease check your internet connection')
