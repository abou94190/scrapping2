# Amazon Books Scraper

Ce script Python permet de récupérer les noms et les prix des livres à partir de la page Amazon Kindle Top Sellers.

## Utilisation

1. Assurez-vous d'avoir Python installé sur votre système.
2. Installez les dépendances en exécutant `pip install requests` et `pip install beautifulsoup4`.
3. Exécutez le script en exécutant `python amazon_books_scraper.py`.

Le script récupérera automatiquement les noms et les prix des livres à partir de la page Amazon Kindle Top Sellers et les affichera dans la console.

## Fonctions du script

### `get_html_content(url)`

Cette fonction récupère le contenu HTML à partir de l'URL spécifiée.

### `get_book_prices(soup)`

Cette fonction récupère les prix des livres à partir de l'objet BeautifulSoup.

### `get_book_names(soup)`

Cette fonction récupère les noms des livres à partir de l'objet BeautifulSoup.

### `scrape_amazon_books(url)`

Cette fonction est la fonction principale du script qui effectue le scraping des noms et des prix des livres sur Amazon.

### `affichage()`

Cette fonction exécute le scraping et affiche les noms et les prix des livres dans la console.

## Exemple d'utilisation

```python
from amazon_books_scraper import affichage

affichage()
