import unittest
from web_crawler import WebCrawler

class TestWebCrawler(unittest.TestCase):
    def setUp(self):
        self.crawler = WebCrawler()

    def test_crawler_fetch(self):
        url = "https://www.consumeraffairs.com/finance/debt-settlement/"
        response = self.crawler.fetch_url(url)
        self.assertEqual(response.status_code, 200)

    def test_crawler_parse(self):
        content = "<html><body><div class='tp-pcks-brd-crd__itm'>Loan details</div></body></html>"
        parsed_content = self.crawler.parse_content(content)
        self.assertEqual(len(parsed_content), 1)
        self.assertEqual(parsed_content[0].text, "Loan details")

if __name__ == '__main__':
    unittest.main()