# EDITED Scrapy Assignment

## Task
Scrape product data from https://www2.hm.com/bg_bg/productpage.1274171042.html using Python Scrapy. Extract:
- name
- price
- current color
- available colors
- reviews count
- reviews score

## Solution
- Scrapy spider attempts to load the product page and extract the required fields.
- Output is written to `output.json`.

## Limitations
- The website blocks Scrapy with HTTP 403 Forbidden errors, even with realistic headers and cookies.
- Anti-bot protection prevents scraping with Scrapy alone.

## Troubleshooting steps
- Updated headers and enabled cookies to mimic a real browser.
- Still received 403 errors.

## Recommendation
If allowed, use Selenium or Playwright for scraping. Otherwise, document the limitation.

## How to run
```
scrapy crawl product -o output.json
```

## Contact
Submitted by: Tvetelin Spasov
Email: cvetelinspasov930@gmail.com
