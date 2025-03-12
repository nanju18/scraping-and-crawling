import asyncio
from crawl4ai import AsyncWebCrawler

async def scrape_all_pages():
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    all_text = "# Scraped Books Data\n\n"

    async with AsyncWebCrawler() as crawler:
        for page in range(1, 51):  # Loop from page 1 to 50
            url = base_url.format(page)
            print(f"Scraping: {url}")  # Print progress

            result = await crawler.arun(url=url)
            all_text += f"## Page {page}\n\n" + result.markdown + "\n\n"

    # Save to a Markdown file
    with open("scraped_books.md", "w", encoding="utf-8") as file:
        file.write(all_text)

    print(" Scraping completed! Data saved in 'scraped_books.md'.")

if __name__ == "__main__":
    asyncio.run(scrape_all_pages())
