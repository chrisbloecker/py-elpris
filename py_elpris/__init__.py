import requests
import re
from bs4 import BeautifulSoup


url = "https://www.elbruk.se"


def get_prices_today():
    """
    Retrieves today's electricity prices from elbruk.se.

    Raises:
        ToDo: figure out which exceptions can be thrown

    Returns:
        A dictionary with areas as keys and prices as values.
    """
    soup   = BeautifulSoup(requests.get(url).text, "html.parser")
    areas  = [ area.text for area in soup.find_all("span", attrs = { "class" : "info-box-text" }) ][:4]
    today  = [ t.text    for t    in soup.find_all("span", attrs = { "class" : "info-box-number" }) ][:4]

    prices = { area : float(t.replace(",",".")) 
                 for (area, t) in zip(areas, today)
             }
    
    return prices


def get_prices_tomorrow():
    """
    Retrieves tomorrow's electricity prices from elbruk.nu.

    Raises:
        ToDo: figure out which exceptions can be thrown

    Returns:
        A dictionary with areas as keys and prices as values.
    """
    soup     = BeautifulSoup(requests.get(url).text, "html.parser")
    areas    = [ area.text for area in soup.find_all("span", attrs = { "class" : "info-box-text" }) ][:4]
    tomorrow = [ t.text    for t    in soup.find_all("span", attrs = { "class" : "progress-description" }) ][:4]

    prices = { area : None for area in areas}
    for (area, t) in zip(areas, tomorrow):
        matches = re.findall(r"\d+,\d+", t)
        if len(matches) == 1:
            prices[area] = float(matches[0].replace(",","."))
    
    return prices