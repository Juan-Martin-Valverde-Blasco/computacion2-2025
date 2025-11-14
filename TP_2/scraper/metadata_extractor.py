from bs4 import BeautifulSoup

class MetadataExtractor:
    @staticmethod
    def extract(html: str) -> dict:
        soup = BeautifulSoup(html, "html.parser")
        title = soup.title.string if soup.title else ''
        description = ''
        desc_tag = soup.find("meta", attrs={"name": "description"})
        if desc_tag:
            description = desc_tag.get("content",'')
        links = [a.get("href") for a in soup.find_all("a", href=True)]
        return {'title': title, 'description': description, 'links': links}