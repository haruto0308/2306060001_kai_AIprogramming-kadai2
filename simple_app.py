import streamlit as st
from simple_logic import fetch_wikipedia_summary

st.set_page_config(page_title="Wikipedia Summarizer", page_icon="📚")

st.title("📚 Wikipedia Summarizer")
st.write("検索キーワードを入力すると、Wikipediaから要約を取得します。")

query = st.text_input("検索ワードを入力してください（例: Python, Tokyo, Elon Musk）")

if st.button("検索"):
    if query.strip():
        result = fetch_wikipedia_summary(query.strip())
        if result["title"] == "Error":
            st.error("情報を取得できませんでした: " + result["description"])
        else:
            st.subheader(result["title"])
            st.write(f"**説明:** {result['description']}")
            st.write(result["extract"])
            if result["url"]:
                st.markdown(f"[Wikipediaで続きを読む]({result['url']})")
    else:
        st.warning("検索ワードを入力してください。")
