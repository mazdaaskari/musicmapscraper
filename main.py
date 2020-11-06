import os
import re
import requests
from bs4 import BeautifulSoup
import click

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def __get_music_map__(artistname) :
    website_address = 'https://www.music-map.com/{0}'.format(artistname)
    page = requests.get(website_address)
    soup = BeautifulSoup(page.content, 'html.parser')
    music_map = soup.find(id='gnodMap')
    artists = music_map.find_all(id=re.compile('^s[1-48]'))
    return artists


@click.command()
@click.help_option('--help', '-h')
@click.option('--artistname', '-a', type=str, help='Enter your favorite artist/band name', prompt='Please enter your '
                                                                                                  'favorite '
                                                                                                  'artist/band')
@click.option('--output', '-o', is_flag=True, help='will output a list of artsits/bands')
@click.argument('filepath', type=click.Path(exists=True), required=False, default='{0}'.format(ROOT_DIR))
def __get_other_artists_name__(artistname, output, filepath) :
    try :

        artists = __get_music_map__(artistname)

        if output:
            file_name = '{0}/artists.txt'.format(filepath)
            file = open(file_name, 'w+')
            for artist in artists:
                file.write('{0}\n'.format(artist.get_text()))
            file.close()

        for artist in artists :
            click.echo(artist.get_text())
    except AttributeError :
        click.echo('Artist not found ! \nPlease enter artist name correctly')
    except ConnectionError :
        click.echo('Not connected ! \nPlease check your internet connection')


if __name__ == '__main__' :
    print('Welcome to Music Map Scraper\nThe data is received from the www.music-map.com\n')
    __get_other_artists_name__()