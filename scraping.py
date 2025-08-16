import requests
from bs4 import BeautifulSoup
from fastmcp import FastMCP
import csv
import datetime

mcp = FastMCP(name="Scraping")


@mcp.tool
def scraping_data(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    targets = []
    for element in soup.find_all("a", text=True):
        targets.append({"text": element.getText(),
                       "link": element.get("href")})
    date_now = datetime.datetime.now()
    with open(f"scraping_{date_now}.csv", mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["テキスト", "リンク"])
        writer.writerows([[target["text"], target["link"]]
                         for target in targets])

    return ",".join([target["text"] for target in targets])


if __name__ == "__main__":
    mcp.run()
