import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import squarify

url = "https://companiesmarketcap.com/dow-jones/largest-companies-by-market-cap/"
#tech_url = "https://companiesmarketcap.com/tech/largest-tech-companies-by-market-cap/"
#food_url = "https://companiesmarketcap.com/food/largest-food-companies-by-market-cap/"
#video_games_url = "https://companiesmarketcap.com/video-games/largest-video-game-companies-by-market-cap/"
#telecommunications_url="https://companiesmarketcap.com/telecommunication/largest-telecommunication-companies-by-market-cap/"
#automaker_url = "https://companiesmarketcap.com/automakers/largest-automakers-by-market-cap/"
#healthcare_url = "https://companiesmarketcap.com/healthcare/largest-healthcare-companies-by-market-cap/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

rows = soup.findChildren("tr")

symbols = []
market_caps = []
sizes = []

for row in rows:
    try:
        symbol = row.find("div", {"class": "company-code"}).text
        market_cap = row.findAll('td')[2].text
        market_caps.append(market_cap)
        symbols.append(symbol)

        if market_cap.endswith("T"):
            sizes.append(float(market_cap[1:-2])* 10 ** 12)
        elif  market_cap.endswith("B"):
            sizes.append(float(market_cap[1:-2])* 10 ** 9)

    except AttributeError:
        pass

labels = [f"{symbols[i]}\n({market_caps[i]})" for i in range(len(symbols))]
colors = [plt.cm.tab20c(i / float(len(symbols)))for i in range(len(symbols))]

squarify.plot(sizes=sizes, label=labels, color=colors,
                bar_kwargs={"linewidth": 0.5, "edgecolor": "#111111"})
plt.show()