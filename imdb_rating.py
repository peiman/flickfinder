import requests
import click
from rich.console import Console
from rich.table import Table

DEFAULT_API_KEY = '33faa6c9'
console = Console()

def get_movie_rating(movie_title, api_key=DEFAULT_API_KEY):
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

@click.command()
@click.argument('query')
@click.option('--api_key', default=DEFAULT_API_KEY, help='OMDb API key')
@click.option('--search', is_flag=True, help='Search for movies by keyword')
@click.option('--ratings', is_flag=True, help='Fetch IMDb ratings for search results')
def main(query, api_key, search, ratings):
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

if __name__ == "__main__":
    main()
