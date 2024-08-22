import streamlit as st
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

# Função de scraping para iCarros
def fetch_icarros():
    url = "https://www.icarros.com.br/noticias/arquivo.jsp"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    news = []
    
    articles = soup.find_all('ul', class_='listahorizontalarquivo')

    for item in articles[:10]:  # Limita a 10 notícias
        link_element = item.find('a')
        title_element = item.find('h1')
        if link_element and title_element:
            title = title_element.get_text(strip=True)
            link = link_element['href']
            if not link.startswith('http'):
                link = "https://www.icarros.com.br" + link
            news.append({"title": title, "link": link})

    return news

# Função de scraping para o UOL Carros
def fetch_uol_carros():
    url = "https://www.uol.com.br/carros/ultimas/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    news = []
    
    articles = soup.find_all('div', class_='thumbnails-item')

    for item in articles[:10]:  # Limita a 10 notícias
        link_element = item.find('a')
        title_element = item.find('h3', class_='thumb-title')
        if link_element and title_element:
            title = title_element.get_text(strip=True)
            link = link_element['href']
            if not link.startswith('http'):
                link = "https://www.uol.com.br" + link
            news.append({"title": title, "link": link})

    return news

# Funções de scraping para outras fontes de notícias
from news_scraper import (
    fetch_automaistv, fetch_autopapo, fetch_motor1, fetch_quatrorodas,
    fetch_autoo, fetch_mobiauto, fetch_motoo, fetch_motociclismo, fetch_autoesporte
)

def main():
    st.title("Últimas Notícias Automotivas")
    st.write("Confira as 10 últimas notícias publicadas nos sites AutoMaisTV, AutoPapo, Motor1, Quatro Rodas, Autoo, Mobiauto, Motoo, Motociclismo, Autoesporte, iCarros e UOL Carros.")

    # Sidebar para seleção de fontes
    st.sidebar.header("Selecione as Fontes de Notícias")
    sources = {
        "AutoMaisTV": fetch_automaistv,
        "AutoPapo": fetch_autopapo,
        "Motor1": fetch_motor1,
        "Quatro Rodas": fetch_quatrorodas,
        "Autoo": fetch_autoo,
        "Mobiauto": fetch_mobiauto,
        "Motoo": fetch_motoo,
        "Motociclismo": fetch_motociclismo,
        "Autoesporte": fetch_autoesporte,
        "iCarros": fetch_icarros,
        "UOL Carros": fetch_uol_carros,  # Adiciona o UOL Carros à lista de fontes
    }

    selected_sources = []
    for source_name in sources.keys():
        if st.sidebar.checkbox(source_name, value=True):
            selected_sources.append(source_name)

    # Função de busca por palavras-chave
    search_query = st.sidebar.text_input("Buscar notícias por palavras-chave")

    def filter_news(news_list, query):
        if not query:
            return news_list
        return [news for news in news_list if query.lower() in news['title'].lower()]

    all_news = []
    for source in selected_sources:
        with st.expander(source):
            fetch_function = sources[source]
            with st.spinner(f"Carregando notícias do {source}..."):
                try:
                    news = fetch_function()
                    if not news:
                        st.write(f"Nenhuma notícia encontrada no {source}.")
                    filtered_news = filter_news(news, search_query)
                    all_news.extend(filtered_news)
                    if filtered_news:
                        for news_item in filtered_news:
                            st.markdown(f"#### [{news_item['title']}]({news_item['link']})")
                    else:
                        st.write(f"Nenhuma notícia encontrada no {source}.")
                except Exception as e:
                    st.write(f"Erro ao carregar notícias do {source}: {e}")

    # Geração de lista de termos mais frequentes
    if all_news:
        all_titles = " ".join(news['title'] for news in all_news)
        all_titles = re.sub(r'[^a-zA-Z0-9\s]', '', all_titles)
        word_count = Counter(all_titles.split())

        # Remover palavras comuns
        stop_words = set(['a', 'e', 'o', 'de', 'da', 'do', 'em', 'para', 'com', 'por', 'que', 'na', 'no', 'as', 'os', 'uma', 'um', 'tem', 'também', 'se', 'são', 'é', 'este', 'esta', 'ao', 'mais', 'ser', 'ter', 'foi', 'como', 'veja', 'pode', 'deve', 'deverá'])
        filtered_word_count = {word: count for word, count in word_count.items() if word.lower() not in stop_words}
        sorted_word_count = Counter(filtered_word_count)

        st.sidebar.header("Termos Mais Frequentes")
        for word, count in sorted_word_count.most_common(10):
            st.sidebar.write(f"{word}: {count}")

if __name__ == "__main__":
    main()
