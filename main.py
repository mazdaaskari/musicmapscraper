import re
import requests
from bs4 import BeautifulSoup


def __get_music_map__(artistname):
    website_address = 'https://www.music-map.com/{0}'.format(artistname)
    page = requests.get(website_address)
    soup = BeautifulSoup(page.content, 'html.parser')
    music_map = soup.find(id='gnodMap')
    artists = music_map.find_all(id=re.compile('^s[1-48]'))
    return artists


if __name__ == '__main__':
    print('Welcome to Music Map Scraper\nThe data is received from the www.music-map.com\n')
    artist_input = input('Please enter your favorite artist or band : ')
    try:
        result = __get_music_map__(artist_input)
        for artist in result:
            print(artist.get_text())
    except AttributeError:
        print('Artist not found ! \nPlease enter artist name correctly')
    except ConnectionError:
        print('Not connected ! \nPlease check your internet connection')
