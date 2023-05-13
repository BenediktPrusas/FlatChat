import requests
from bs4 import BeautifulSoup
from typing import Optional
from urllib.parse import urlparse


def get_wg_gesucht_flat_description(url: str) -> str:
    """
    Scrape the description of a flat from the website 'https://www.wg-gesucht.de/'.

    Parameters:
    url (str): The URL of the flat to scrape.

    Returns:
    str: The description of the flat.
    """

    validate_domain(url, 'www.wg-gesucht.de')

    description = scrape_flat_description(url, 'ad_description_text')

    description = clean_flat_description(description)

    return description

def validate_domain(url: str, domain: str) -> None:
    """
    Validate that a URL belongs to a specific domain.

    Parameters:
    url (str): The URL to validate.
    domain (str): The domain to validate the URL against.

    Returns:
    None
    """

    if urlparse(url).netloc != domain:
        raise ValueError(f"The URL '{url}' does not belong to the domain '{domain}'.")


def clean_flat_description(description: str) -> str:
    """
    Clean the description of a flat.

    Parameters:
    description (str): The description of the flat.

    Returns:
    str: The cleaned description of the flat.
    """

    # Remove unnecessary whitespaces
    cleaned_text = ' '.join(description.split())

    return cleaned_text



def scrape_flat_description(url: str, element_id: str) -> Optional[str]:
    """
    Scrape text from a specific element on a website.

    Parameters:
    url (str): The URL of the website to scrape.
    element_id (str): The id of the HTML element to scrape text from.

    Returns:
    Optional[str]: The text from the specified HTML element, or None if the element was not found.
    """

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as err:
        print(f"An error occurred while trying to get the webpage: {err}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    element_text = soup.find(id=element_id)

    if element_text is None:
        raise ValueError(f"The element with id '{element_id}' was not found on the webpage.")

    return element_text.text

