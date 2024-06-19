# FlickFinder

FlickFinder is a command-line tool to fetch IMDb ratings for movies or search for movies by keyword using the OMDb API. The tool can also provide links to IMDb pages for the search results.

## Features

- Fetch IMDb rating for a specific movie title.
- Search for movies by keyword.
- Optionally fetch IMDb ratings for search results.
- Provide clickable IMDb links for the search results.

## Installation

1. **Clone the repository or download the script:**

   ```sh
   git clone https://github.com/peiman/flickfinder.git
   cd flickfinder
   ```

2. **Install the required libraries:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Create a `.env` file in the project root directory and add your OMDb API key:**

   ```sh
   echo "OMDB_API_KEY=your_api_key_here" > .env
   ```

## Usage

### Fetch IMDb Rating by Movie Title

Fetch the IMDb rating for a specific movie title using the default API key:

```sh
flickfinder "Inception"
```

Fetch the IMDb rating for a specific movie title using a custom API key:

```sh
flickfinder "Inception" --api_key YOUR_CUSTOM_API_KEY
```

### Search for Movies by Keyword

Search for movies by a keyword using the default API key:

```sh
flickfinder "Star Wars" --search
```

Search for movies by a keyword using a custom API key:

```sh
flickfinder "Star Wars" --search --api_key YOUR_CUSTOM_API_KEY
```

### Fetch IMDb Ratings for Search Results

Search for movies by a keyword and fetch IMDb ratings for the results using the default API key:

```sh
flickfinder "Star Wars" --search --ratings
```

Search for movies by a keyword and fetch IMDb ratings for the results using a custom API key:

```sh
flickfinder "Star Wars" --search --ratings --api_key YOUR_CUSTOM_API_KEY
```

## Example Output

### Fetching IMDb Rating by Movie Title

```sh
$ flickfinder "Inception"
```

Output:
```
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ Attribute    ┃ Value           ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
│ Title        │ Inception       │
│ Year         │ 2010            │
│ IMDb Rating  │ 8.8             │
└──────────────┴─────────────────┘
```

### Searching for Movies by Keyword

```sh
$ flickfinder "Star Wars" --search
```

Output:
```
┏━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Title          ┃ Year ┃ IMDb ID      ┃ IMDb Link                           ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Star Wars      │ 1977 │ tt0076759    │ [link=https://www.imdb.com/title/tt0076759/]IMDb Link[/link] │
│ Star Wars: ... │ 1980 │ tt0080684    │ [link=https://www.imdb.com/title/tt0080684/]IMDb Link[/link] │
│ Star Wars: ... │ 1983 │ tt0086190    │ [link=https://www.imdb.com/title/tt0086190/]IMDb Link[/link] │
│ ...            │ ...  │ ...          │ ...                                 │
└────────────────┴──────┴──────────────┴─────────────────────────────────────┘
```

### Searching for Movies by Keyword with IMDb Ratings

```sh
$ flickfinder "Star Wars" --search --ratings
```

Output:
```
┏━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Title          ┃ Year ┃ IMDb ID      ┃ IMDb Link                           ┃ IMDb Rating┃
┡━━━━━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ Star Wars      │ 1977 │ tt0076759    │ [link=https://www.imdb.com/title/tt0076759/]IMDb Link[/link] │ 8.6        │
│ Star Wars: ... │ 1980 │ tt0080684    │ [link=https://www.imdb.com/title/tt0080684/]IMDb Link[/link] │ 8.7        │
│ Star Wars: ... │ 1983 │ tt0086190    │ [link=https://www.imdb.com/title/tt0086190/]IMDb Link[/link] │ 8.3        │
│ ...            │ ...  │ ...          │ ...                                 │ ...        │
└────────────────┴──────┴──────────────┴─────────────────────────────────────┴────────────┘
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Peiman Khorramshahi - [GitHub](https://github.com/peiman)
