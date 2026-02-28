import time
from config import URLS, HEADERS, MIN_ROWS, OUTPUT_FILE
from scraper.fetcher import fetch_page
from scraper.parser import parse_page
from scraper.processor import process_data
from utils.file_handler import save_to_csv


def main():
    all_data = []

    for url in URLS:
        try:
            print(f"🔍 Scraping: {url}")
            html = fetch_page(url, HEADERS)
            page_data = parse_page(html, url)
            all_data.extend(page_data)
            print(f"✅ Done: {url}")
            time.sleep(1)

        except Exception as e:
            print(f"❌ Error with {url}: {e}")

    df = process_data(all_data, MIN_ROWS)
    print(f"✅ Final rows: {len(df)}")

    save_to_csv(df, OUTPUT_FILE)
    print("✅ Data saved successfully!")


if __name__ == "__main__":
    main()