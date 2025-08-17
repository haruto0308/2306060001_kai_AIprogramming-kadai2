import requests

WIKI_API_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"

def fetch_wikipedia_summary(query: str) -> dict:
    """
    Wikipediaから要約を取得する
    :param query: 検索キーワード
    :return: dict {"title": str, "description": str, "extract": str, "url": str}
    """
    try:
        response = requests.get(WIKI_API_URL + query)
        response.raise_for_status()
        data = response.json()

        return {
            "title": data.get("title", "N/A"),
            "description": data.get("description", "N/A"),
            "extract": data.get("extract", "N/A"),
            "url": data.get("content_urls", {}).get("desktop", {}).get("page", "")
        }
    except Exception as e:
        return {"title": "Error", "description": str(e), "extract": "", "url": ""}

