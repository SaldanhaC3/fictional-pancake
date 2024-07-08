import requests
from bs4 import BeautifulSoup

def fetch_automaistv():
    url = "https://www.automaistv.com.br/ultimas-noticias/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    news = []
    for item in soup.find_all('div', class_='feed-body')[:10]:
        title_element = item.find('h2', class_='post-title-feed-lg feed-title feed-title-lg')
        link_element = item.find_parent('a')
        if title_element and link_element:
            title = title_element.get_text(strip=True)
            link = link_element['href']
            news.append({"title": title, "link": link})
    return news

def fetch_autopapo():
    url = "https://autopapo.uol.com.br/noticia/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    news = []
    for item in soup.find_all('a', class_='card-block')[:10]:
        title_element = item.find('h2', class_='card-title')
        link_element = item
        if title_element and link_element:
            title = title_element.get_text(strip=True)
            link = link_element['href']
            news.append({"title": title, "link": link})
    return news

def fetch_motor1():
    url = "https://motor1.uol.com.br/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    news = []
    for item in soup.find_all('div', class_='info')[:10]:
        title_element = item.find('h3').find('a')
        if title_element:
            title = title_element.get_text(strip=True)
            link = "https://motor1.uol.com.br" + title_element['href']
            news.append({"title": title, "link": link})
    return news

def fetch_quatrorodas():
    url = "https://quatrorodas.abril.com.br/ultimas-noticias/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    news = []
    for item in soup.find_all('div', class_='col-s-12 col-l-9')[:10]:
        link_element = item.find('a', href=True)
        title_element = item.find('h2', class_='title')
        if link_element and title_element:
            title = title_element.get_text(strip=True)
            link = link_element['href']
            news.append({"title": title, "link": link})
    return news

def fetch_autoo():
    url = "https://www.autoo.com.br/noticias/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    news = []
    for item in soup.find_all('div', class_='col-sm-9')[:10]:
        link_element = item.find('a', href=True)
        title_element = item.find('h4')
        if link_element and title_element:
            title = title_element.get_text(strip=True)
            link = "https://www.autoo.com.br" + link_element['href']
            news.append({"title": title, "link": link})
    return news

def fetch_mobiauto():
    url = "https://www.mobiauto.com.br/revista/editorial/noticias"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    news = []
    for item in soup.find_all('div', class_='mui-style-d8mvmb')[:10]:
        title_element = item.find('h3', class_='mui-style-v8880f')
        link_element = item.find_parent('a')
        if title_element and link_element:
            title = title_element.get_text(strip=True)
            link = link_element['href']
            news.append({"title": title, "link": link})
    return news

def fetch_motoo():
    url = "https://www.motoo.com.br/noticias/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    news = []
    for item in soup.find_all('div', class_='header_title mt-3 mb-3')[:10]:
        title_element = item.find('h4')
        link_element = item.find('a', href=True)
        if title_element and link_element:
            title = title_element.get_text(strip=True)
            link = "https://www.motoo.com.br" + link_element['href']
            news.append({"title": title, "link": link})
    return news

def fetch_motociclismo():
    url = "https://motociclismoonline.com.br/noticias/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    news = []
    for item in soup.find_all('div', class_='col-12 media-body')[:10]:
        title_element = item.find('h2', class_='card-title').find('a')
        link_element = title_element
        if title_element and link_element:
            title = title_element.get_text(strip=True)
            link = link_element['href']
            news.append({"title": title, "link": link})
    return news

def fetch_autoesporte():
    url = "https://autoesporte.globo.com/ultimas-noticias/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    news = []
    for item in soup.find_all('div', class_='feed-post-body')[:10]:
        title_element = item.find('h2', class_='feed-post-link gui-color-primary gui-color-hover')
        link_element = title_element.find('a', href=True)
        if title_element and link_element:
            title = title_element.get_text(strip=True)
            link = link_element['href']
            news.append({"title": title, "link": link})
    return news

if __name__ == "__main__":
    # Testando as funções
    print("AutoMaisTV News:")
    automaistv_news = fetch_automaistv()
    for article in automaistv_news:
        print(f"{article['title']}: {article['link']}")

    print("\nAutoPapo News:")
    autopapo_news = fetch_autopapo()
    for article in autopapo_news:
        print(f"{article['title']}: {article['link']}")

    print("\nMotor1 News:")
    motor1_news = fetch_motor1()
    for article in motor1_news:
        print(f"{article['title']}: {article['link']}")

    print("\nQuatro Rodas News:")
    quatrorodas_news = fetch_quatrorodas()
    for article in quatrorodas_news:
        print(f"{article['title']}: {article['link']}")

    print("\nAutoo News:")
    autoo_news = fetch_autoo()
    for article in autoo_news:
        print(f"{article['title']}: {article['link']}")

    print("\nMobiauto News:")
    mobiauto_news = fetch_mobiauto()
    for article in mobiauto_news:
        print(f"{article['title']}: {article['link']}")

    print("\nMotoo News:")
    motoo_news = fetch_motoo()
    for article in motoo_news:
        print(f"{article['title']}: {article['link']}")

    print("\nMotociclismo News:")
    motociclismo_news = fetch_motociclismo()
    for article in motociclismo_news:
        print(f"{article['title']}: {article['link']}")

    print("\nAutoesporte News:")
    autoesporte_news = fetch_autoesporte()
    for article in autoesporte_news:
        print(f"{article['title']}: {article['link']}")
