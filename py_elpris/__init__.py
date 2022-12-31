import requests
from bs4 import BeautifulSoup

def get_prices():
    """
    Retrieves today's electricity prices from elen.nu.

    Raises:
        ToDo: figure out which exceptions can be thrown

    Returns:
        A dictionary with areas as keys and prices as values.
    """

    url      = "https://elen.nu"
    content  = requests.get(url).text
    soup     = BeautifulSoup(content, "html.parser")
    areas    = soup.find_all("div",  attrs = { "class" : "uppercase text-sm" })
    today    = soup.find_all("span", attrs = { "class" : "text-lg" })
    tomorrow = soup.find_all("div",  attrs = { "class" : "text-xs" })

    prices   = { area.text : float(t.text.replace(",",".")) 
                   for (area, t) in zip(areas, today)
               }
    
    return prices