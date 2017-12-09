from newsapi.topheadlines import Everything
import pprint
from json2html import *

if __name__ == '__main__':
    everything = Everything(API_KEY='<Your API Key>')
    content = everything.get(sources='bbc-news', attributes_format=False)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(content)
    html_content = json2html.convert(json=content)
    f = open('html/test.html', 'w')
    f.write(html_content)
    f.close()
