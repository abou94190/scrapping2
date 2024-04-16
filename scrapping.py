import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    """Récupérer le contenu HTML à partir de l'URL."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"contenu inaccessible: {url}")

def get_book_prices(soup):
    """Récupérer les prix des livres à partir du soup (BeautifulSoup object)."""
    prix_elements = soup.find_all('span', class_='a-color-price a-text-bold')
    prix_selection = []
    for prix_element in prix_elements:
        text_prix = prix_element.text.strip()
        prix_selection.append(text_prix)
    return prix_selection

def get_book_names(soup):
    """Récupérer les noms des livres à partir du soup (BeautifulSoup object)."""
    nom_elements = soup.find_all('span', class_='a-size-base a-color-base browse-text-line browse-larger-text-one-line')
    nom_selection = []
    for nom_element in nom_elements:
        text_nom = nom_element.text.strip()
        nom_selection.append(text_nom)
    return nom_selection

def scrape_amazon_books(url):
    """Fonction principale pour faire le scraping des noms et des prix des livres sur Amazon."""
    html_content = get_html_content(url)
    soup = BeautifulSoup(html_content, 'html.parser')
    
    prix_selection = get_book_prices(soup)
    nom_selection = get_book_names(soup)
    
    livres = list(zip(nom_selection, prix_selection))
    
    return livres

def main():
    url = 'https://www.amazon.fr/kindle-dbs/browse?metadata=cardAppType%3ADESKTOP%24deviceTypeID%3AA2Y8LFC259B97P%24clientRequestId%3AY050AM5KD770854NFYY6%24deviceAppType%3ADESKTOP%24ipAddress%3A10.90.176.80%24browseNodes%3A695398031%24userAgent%3AMozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%3B+rv%3A124.0%29+Gecko%2F20100101+Firefox%2F124.0%24cardSurfaceType%3Adesktop%24cardMobileOS%3AUnknown%24locale%3Afr_FR%24deviceSurfaceType%3Adesktop&storeType=ebooks&widgetId=unified-ebooks-storefront-default_TopSellersStrategy&sourceAsin=&content-id=amzn1.sym.360aebec-b11d-4773-8755-47be2f158110&refTagFromService=ts&title=Meilleures%20Ventes&pf_rd_p=360aebec-b11d-4773-8755-47be2f158110&sourceType=recs&pf_rd_r=Y050AM5KD770854NFYY6&pd_rd_wg=8A2IT&ref_=dbs_r_recs_ts_r&SkipDeviceExclusion=true&page=1&pd_rd_w=wCpwS&nodeId=695398031&pd_rd_r=155e4e23-da00-4753-89c8-5ce26c805f69'
    
    livres = scrape_amazon_books(url)
    
    for nom, prix in livres:
        print(f"{nom}: {prix}")

if __name__ == "__main__":
    main()