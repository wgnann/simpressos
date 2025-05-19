import requests
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()

def page_count(printer_ip):
    url = "https://"+printer_ip+"/hp/device/InternalPages/Index?id=UsagePage"
    page = requests.get(url, verify=False)
    parser = BeautifulSoup(page.content, features="lxml")
    element = parser.find("td", {"id": "UsagePage.EquivalentImpressionsTable.Total.Total"}, "html.parser")

    # ex: 314,159,265.35
    tmp = element.getText()
    counter = round(float(tmp.replace(",","")))
    return counter

if __name__ == "__main__":
    from sys import argv
    ip = argv[1]
    print(page_count(ip))
