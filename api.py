import requests
import pandas as pd

# Google Books API 端點
API_URL = "https://www.googleapis.com/books/v1/volumes"

# 查詢參數
params = {
    "q": "Python",  # 搜尋關鍵字
    "maxResults": 10,  # 取得 10 本書
    "printType": "books",
    "langRestrict": "zh"  # 限制為中文書籍
}

# 發送 GET 請求
response = requests.get(API_URL, params=params)

# 確保請求成功
if response.status_code == 200:
    data = response.json()
    books = data.get("items", [])

    # 解析資料
    book_list = []
    for book in books:
        info = book["volumeInfo"]
        title = info.get("title", "無標題")
        authors = ", ".join(info.get("authors", ["未知作者"]))
        publisher = info.get("publisher", "未知出版社")
        published_date = info.get("publishedDate", "未知日期")
        page_count = info.get("pageCount", "未知頁數")

        book_list.append({
            "書名": title,
            "作者": authors,
            "出版社": publisher,
            "出版日期": published_date,
            "頁數": page_count
        })

    # 儲存成 CSV
    df = pd.DataFrame(book_list)
    df.to_csv("api.csv", index=False, encoding="utf-8-sig")

    print("✅ API 串接成功，結果已儲存至 api.csv")
else:
    print(f"❌ API 錯誤，狀態碼：{response.status_code}")
