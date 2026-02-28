# مسؤول على استخراج البيانات

from bs4 import BeautifulSoup

def parse_page(html, base_url):
    soup = BeautifulSoup(html, "lxml")
    data = []

    # Titles
    titles = soup.find_all(["h2", "h3"])

    for title in titles[:20]:
        title_text = title.text.strip()
        if len(title_text) > 10:
            next_p = title.find_next("p")
            description = next_p.text.strip() if next_p else "No description"

            link_tag = title.find("a")
            link = link_tag["href"] if link_tag else base_url

            if link.startswith("/"):
                link = "https://www.postscapes.com" + link

            data.append([title_text, description, link, "IoT"])

    # Tables
    tables = soup.find_all("table")
    for table in tables:
        rows = table.find_all("tr")
        for row in rows[1:]:
            cols = row.find_all("td")
            if len(cols) >= 2:
                col1 = cols[0].text.strip()
                col2 = cols[1].text.strip()
                data.append([col1, col2, base_url, "IoT Table"])

    return data