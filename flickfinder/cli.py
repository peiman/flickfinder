import os
import requests
import click
import configparser
from pathlib import Path
from rich.console import Console
from rich.table import Table

# Define the path for the config file in the user's home directory
CONFIG_FILE_PATH = Path.home() / '.flickfinder_config.ini'

def load_config():
    config = configparser.ConfigParser()
    if CONFIG_FILE_PATH.is_file():
        config.read(CONFIG_FILE_PATH)
    else:
        config['DEFAULT'] = {'OMDB_API_KEY': ''}
        with open(CONFIG_FILE_PATH, 'w') as configfile:
            config.write(configfile)
    return config

def save_config(config):
    with open(CONFIG_FILE_PATH, 'w') as configfile:
        config.write(configfile)

config = load_config()
DEFAULT_API_KEY = config['DEFAULT'].get('OMDB_API_KEY')

console = Console()

console.print(f"Config file loaded from: {CONFIG_FILE_PATH}", style="bold blue")
console.print(f"Default API Key: {DEFAULT_API_KEY}", style="bold blue")

def get_movie_rating(movie_title, api_key=DEFAULT_API_KEY):
    console.print(f"API Key in get_movie_rating: {api_key}", style="bold yellow")
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or 'Error' in data:
        return f"Error: {data.get('Error', 'Failed to fetch data')}"

    title = data.get('Title', 'N/A')
    year = data.get('Year', 'N/A')
    rating = data.get('imdbRating', 'N/A')
    return {
        'Title': title,
        'Year': year,
        'IMDb Rating': rating
    }

def search_movies(keyword, api_key=DEFAULT_API_KEY, fetch_ratings=False):
    url = f"http://www.omdbapi.com/?s={keyword}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or 'Error' in data:
        return f"Error: {data.get('Error', 'Failed to fetch data')}"

    if 'Search' not in data:
        return "No movies found."

    results = []
    for movie in data['Search']:
        imdb_id = movie.get('imdbID', 'N/A')
        imdb_link = f"https://www.imdb.com/title/{imdb_id}/"
        if fetch_ratings:
            movie_details = get_movie_details(imdb_id, api_key)
            movie_details['IMDb Link'] = imdb_link
            results.append(movie_details)
        else:
            results.append({
                'Title': movie.get('Title', 'N/A'),
                'Year': movie.get('Year', 'N/A'),
                'IMDb ID': imdb_id,
                'IMDb Link': imdb_link
            })

    return results

def get_movie_details(imdb_id, api_key=DEFAULT_API_KEY):
    url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or 'Error' in data:
        return {
            'Title': 'N/A',
            'Year': 'N/A',
            'IMDb Rating': 'N/A',
            'IMDb ID': imdb_id
        }

    return {
        'Title': data.get('Title', 'N/A'),
        'Year': data.get('Year', 'N/A'),
        'IMDb Rating': data.get('imdbRating', 'N/A'),
        'IMDb ID': imdb_id
    }

@click.group()
def cli():
    pass

@click.command()
@click.argument('query')
@click.option('--api_key', default=DEFAULT_API_KEY, help='OMDb API key')
@click.option('--search', is_flag=True, help='Search for movies by keyword')
@click.option('--ratings', is_flag=True, help='Fetch IMDb ratings for search results')
def find(query, api_key, search, ratings):
    console.print(f"Using API Key: {api_key}", style="bold green")
    if search:
        result = search_movies(query, api_key, fetch_ratings=ratings)
        if isinstance(result, str):
            console.print(result, style="bold red")
        else:
            table = Table(title="Search Results")
            table.add_column("Title", justify="left", style="cyan", no_wrap=True)
            table.add_column("Year", justify="left", style="magenta")
            table.add_column("IMDb ID", justify="left", style="green")
            table.add_column("IMDb Link", justify="left", style="blue")
            if ratings:
                table.add_column("IMDb Rating", justify="left", style="yellow")

            for movie in result:
                if ratings:
                    table.add_row(movie['Title'], movie['Year'], movie['IMDb ID'], f"[link={movie['IMDb Link']}]IMDb Link[/link]", movie['IMDb Rating'])
                else:
                    table.add_row(movie['Title'], movie['Year'], movie['IMDb ID'], f"[link={movie['IMDb Link']}]IMDb Link[/link]")

            console.print(table)
    else:
        result = get_movie_rating(query, api_key)
        if isinstance(result, str):
            console.print(result, style="bold red")
        else:
            table = Table(title="Movie Rating")
            table.add_column("Attribute", justify="left", style="cyan", no_wrap=True)
            table.add_column("Value", justify="left", style="magenta")

            for key, value in result.items():
                table.add_row(key, value)

            console.print(table)

@click.command()
@click.option('--key', required=True, help='Configuration key to set')
@click.option('--value', required=True, help='Configuration value to set')
def set_config(key, value):
    """Set a configuration value."""
    config = load_config()
    config['DEFAULT'][key] = value
    save_config(config)
    console.print(f"Configu
