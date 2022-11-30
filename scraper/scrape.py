import logging

import lxml
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}
shop_href = "https://www.etsy.com/shop/artsyantonelli"

logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def get_item(result):
    title = result.select_one(".v2-listing-card__title").text.strip()
    img = result.select_one('img[data-listing-card-listing-image]')
    img = img["src"] if img.has_key("src") else None
    cost = result.select_one('.currency-value').text
    badge = result.select_one('.wt-badge .wt-display-inline-block')
    badge = badge.text.strip() if badge else None

    return (title, img, cost, badge)


def scrape():
    listings_selector = "div[data-appears-component-name='shop_home_listing_grid'] .v2-listing-card"
    html = requests.get(shop_href, headers=headers, timeout=30)
    soup = BeautifulSoup(html.text, "lxml")

    # best sellers
    logger.info("\nBEST SELLERS")
    for result in soup.select(".featured-listings div.v2-listing-card"):
        (title, img, cost, badge) = get_item(result)
        logger.info(title)

    # all items
    logger.info("\nALL ITEMS - PAGE 1")
    for result in soup.select(listings_selector):
        (title, img, cost, badge) = get_item(result)
        logger.info(title)

    # paginate the rest
    page = 2
    while True:
        logger.info(f"\nALL ITEMS - PAGE {page}")

        html = requests.get(f"{shop_href}?page={page}#items",
                            headers=headers, timeout=30)
        soup = BeautifulSoup(html.text, "lxml")

        for result in soup.select(listings_selector):
            (title, img, cost, badge) = get_item(result)
            logger.info(title)

        paginate_next_page = soup.select(
            "[data-item-pagination] a[role='link']")[-1]
        disabled = paginate_next_page.get("aria-disabled")
        if not disabled:
            page += 1
        else:
            break


scrape()
