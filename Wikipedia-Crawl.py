# import all necessary modules
import requests
from bs4 import BeautifulSoup
import lxml
import time
import networkx as nx
import matplotlib.pyplot as plt

# URL to crawl
URL = ["https://en.wikipedia.org/wiki/Idea",
       "https://en.wikipedia.org/wiki/Science",
       "https://en.wikipedia.org/wiki/Superman",
       "https://en.wikipedia.org/wiki/Alcohol"]


# Remove unnecesssary links under a class
def waste_remove(soup):
    for div in soup.find_all("p", {'class': 'mw-empty-elt'}):
        div.decompose()

# Remove unnecessary links inside parenthesis according to Rule 2
def waste_a_tag(content):
    lists = []
    initial = 0
    final = 0

    for i in range(0, len(content)):
        lists.append(str(content[i]))

    first_line = "".join(lists)

    datas = list(first_line)

    for i in range(len(datas)):
        if datas[i] == "(":
            initial = i
            for j in range(i, len(datas)):
                if datas[j] == ")":
                    final = j

                    capturedString = ''.join(datas[initial:final+1])

                    if '<a' in capturedString:
                        for i in range(initial, final+1):
                            datas[i] = ""
                    else:
                        pass
                    break
                else:
                    pass
        else:
            pass

    str_datas = "".join(datas)

    essentialData = BeautifulSoup(str_datas, 'lxml')
    return essentialData


def crawl(link, count, network_data):

    data = requests.get(link)
    soup = BeautifulSoup(data.text, 'lxml')
    waste_remove(soup)

    content = soup.find("div", {"class": "mw-parser-output"})
    content = content.find_all("p", recursive=False)

    essentialData = waste_a_tag(content)

    title = ""

    for i in range(len(essentialData.select("p"))):
        if (essentialData.select("p")[i].find_all("a", recursive=False) == []):

            pass
        else:
            link = "https://en.wikipedia.org" + \
                essentialData.select("p")[i].find_all(
                    "a", recursive=False)[0]['href']
            title = essentialData.select("p")[i].find_all(
                "a", recursive=False)[0]['title']
            print(title)
            network_data.append(title)

            if(title == "Philosophy"):

                return ("Success!! You finally reached Philosophy page")
            else:
                count = count + 1
                if (count < 25):
                    time.sleep(1)
                    return crawl(link, count, network_data)
                else:
                    return("Maximum number of links referred. Aborting!!")


def plot_graph(datas):
    g = nx.Graph()

    for i in range(len(URL)):
        for j in range(len(datas[i]) - 1):
            g.add_edge(datas[i][j], datas[i][j+1])

    nx.draw(g, node_color='#A0CBE2', with_labels=True)

    plt.draw()
    plt.savefig('crawl.png')                # Graph is stored as crawl.png
    plt.show()


if __name__ == "__main__":

    count = 0                               # To abort the crawl function when maximum crawl reaches 25
    datas = []

    for i in range(len(URL)):
        data = requests.get(URL[i])
        datas.append([])
        soup = BeautifulSoup(data.text, 'lxml')
        title = soup.find("h1").getText()
        datas[i].append(title)
        print("Crawling URL : ", URL[i], "...")
        crawl(URL[i], count, datas[i])
        print("Finished crawling URL :", URL[i], "\n")

    print("Successfully crawled all URL's!!!")
    plot_graph(datas)                      # Function to plot network
