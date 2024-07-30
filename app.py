import streamlit as st
from news_scraper import (
    fetch_automaistv, fetch_autopapo, fetch_motor1, fetch_quatrorodas,
    fetch_autoo, fetch_mobiauto, fetch_motoo, fetch_motociclismo, fetch_autoesporte
)
from collections import Counter
import re

def main():
    st.title("Últimas Notícias Automotivas")
    st.write("Confira as 10 últimas notícias publicadas nos sites AutoMaisTV, AutoPapo, Motor1, Quatro Rodas, Autoo, Mobiauto, Motoo, Motociclismo e Autoesporte.")

    # Sidebar for source selection
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
    }

    selected_sources = []
    for source_name in sources.keys():
        if st.sidebar.checkbox(source_name, value=True):
            selected_sources.append(source_name)

    # Search functionality
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

    # Generate term frequency list
    if all_news:
        all_titles = " ".join(news['title'] for news in all_news)
        all_titles = re.sub(r'[^a-zA-Z0-9\s]', '', all_titles)
        word_count = Counter(all_titles.split())

        # Remove common stop words
        stop_words = set(['a', 'e', 'o', 'de', 'da', 'do', 'em', 'para', 'com', 'por', 'que', 'na', 'no', 'as', 'os', 'uma', 'um', 'tem', 'também', 'se', 'são', 'é', 'este', 'esta','ao','mais','ser','ter', 'foi', 'como', 'veja', 'pode', 'deve, 'deverá', 'com' , ])
        filtered_word_count = {word: count for word, count in word_count.items() if word.lower() not in stop_words}
        sorted_word_count = Counter(filtered_word_count)

        st.sidebar.header("Termos Mais Frequentes")
        for word, count in sorted_word_count.most_common(10):
            st.sidebar.write(f"{word}: {count}")

if __name__ == "__main__":
    main()
