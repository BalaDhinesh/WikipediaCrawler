# WikipediaCrawler

Clicking on the first link in the main text of a Wikipedia article, and then repeating the process for subsequent articles, usually leads to the Philosophy article. In February 2016, this was true for 97% of all articles in Wikipedia, an increase from 94.52% in 2011. The remaining articles lead to an article without any outgoing wikilinks, to pages that do not exist, or get stuck in loops.

## Problem Statement:
Given a list of random wikipedia pages link, the task is to crawl to 'Philosophy' page with web scrapping using python. And also to generate graph out of it.

## Rules:
1. Clicking on the first non-parenthesized, non-italicized link
2. Ignoring external links, links to the current page, or red links (links to non-existent pages)
3. Stopping when reaching "Philosophy", a page with no links or a page that does not exist, or when a loop occurs

## Modules Used:

- requests - to get https request from the server
- BeautifulSoup with lxml as the HTML parser - used to navigate and modify the DOM tree of each random Wikipedia mobile page
- time - Slow things down so as to not hammer Wikipedia's servers
- matplotlib - to plot graph
- networkx - to plot connected networks in matplotlib

## Code:
[Click Here]("./Wikipedia-Crawl.py")

## Sample output graph:
![Crawl]("./Samplegraph.png")
