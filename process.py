import os
from datetime import datetime, timezone
import ssl
from bs4 import BeautifulSoup
from urllib.request import urlopen
from jinja2 import Environment, FileSystemLoader

from settings import SOURCES
ssl._create_default_https_context = ssl._create_unverified_context

def get_data(source):
    try:
        url = source.get('url')
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")

        data = soup.find("table", {"id": source.get('table_id')})
        modified = soup.find("span", {'class': 'last-modified'}).contents[0]
    except Exception as e:
        print(e)
        return (None, None)

    return (data, modified)


if __name__ == '__main__':
    data = []
    # Get urls from settings and retrieve the html
    for source in SOURCES:
        table_html = get_data(source)

        data.append({
            'name': source.get('name'),
            'html': table_html[0],
            'modified': table_html[1]
        })

    utc_dt = datetime.now(timezone.utc)
    generated_when = utc_dt.astimezone().strftime("%d/%m/%Y %H:%M:%S")

    abspath = os.path.abspath(__file__)
    BASE_DIR = os.path.dirname(abspath)

    # Set template directory and load template 
    env = Environment(loader=FileSystemLoader(BASE_DIR + '/templates'))
    template = env.get_template('index.html')

    # render the output html with the downloaded timetables
    result = template.render(source_data=data, generated_when=generated_when)

    with open(os.path.join(BASE_DIR, 'static/index.html'), 'w') as f:
        f.write(result)
