import streamlit as st
from news_scraper import fetch_automaistv, fetch_autopapo, fetch_motor1, fetch_quatrorodas, fetch_autoo, fetch_mobiauto, fetch_motoo, fetch_motociclismo, fetch_autoesporte

def main():
    st.title("Últimas Notícias Automotivas")
    st.write("Confira as 10 últimas notícias publicadas nos sites AutoMaisTV, AutoPapo, Motor1, Quatro Rodas, Autoo, Mobiauto, Motoo, Motociclismo e Autoesporte.")

    st.header("AutoMaisTV")
    automaistv_news = fetch_automaistv()
    if automaistv_news:
        for news in automaistv_news:
            st.write(f"[{news['title']}]({news['link']})")
    else:
        st.write("Nenhuma notícia encontrada no AutoMaisTV.")

    st.header("AutoPapo")
    autopapo_news = fetch_autopapo()
    if autopapo_news:
        for news in autopapo_news:
            st.write(f"[{news['title']}]({news['link']})")
    else:
        st.write("Nenhuma notícia encontrada no AutoPapo.")

    st.header("Motor1")
    motor1_news = fetch_motor1()
    if motor1_news:
        for news in motor1_news:
            st.write(f"[{news['title']}]({news['link']})")
    else:
        st.write("Nenhuma notícia encontrada no Motor1.")

    st.header("Quatro Rodas")
    quatrorodas_news = fetch_quatrorodas()
    if quatrorodas_news:
        for news in quatrorodas_news:
            st.write(f"[{news['title']}]({news['link']})")
    else:
        st.write("Nenhuma notícia encontrada no Quatro Rodas.")

    st.header("Autoo")
    autoo_news = fetch_autoo()
    if autoo_news:
        for news in autoo_news:
            st.write(f"[{news['title']}]({news['link']})")
    else:
        st.write("Nenhuma notícia encontrada no Autoo.")

    st.header("Mobiauto")
    mobiauto_news = fetch_mobiauto()
    if mobiauto_news:
        for news in mobiauto_news:
            st.write(f"[{news['title']}]({news['link']})")
    else:
        st.write("Nenhuma notícia encontrada no Mobiauto.")

    st.header("Motoo")
    motoo_news = fetch_motoo()
    if motoo_news:
        for news in motoo_news:
            st.write(f"[{news['title']}]({news['link']})")
    else:
        st.write("Nenhuma notícia encontrada no Motoo.")

    st.header("Motociclismo")
    motociclismo_news = fetch_motociclismo()
    if motociclismo_news:
        for news in motociclismo_news:
            st.write(f"[{news['title']}]({news['link']})")
    else:
        st.write("Nenhuma notícia encontrada no Motociclismo.")

    st.header("Autoesporte")
    autoesporte_news = fetch_autoesporte()
    if autoesporte_news:
        for news in autoesporte_news:
            st.write(f"[{news['title']}]({news['link']})")
    else:
        st.write("Nenhuma notícia encontrada no Autoesporte.")

if __name__ == "__main__":
    main()
