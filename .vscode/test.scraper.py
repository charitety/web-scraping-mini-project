import unittest
from unittest.mock import patch
from debt_management_plan import scrape_data  # Use underscores instead of hyphens

class TestWebCrawler(unittest.TestCase):

    @patch("requests.get")
    def test_scrape_data(self, mock_requests_get):
        # Mock the response for the requests.get call
        mock_response = mock_requests_get.return_value
        mock_response.status_code = 200
        mock_response.content = """
            <div class="brnd-crd-v2__ttl">Sample Plan</div>
            <div class="tp-pcks-brd-crd__itm-val">6 months</div>
            <div class="dynmc-tb__cell-ftr">$1000</div>
            <button class="ca-btn ca-btn--body-fs dynmc-tb__btn">Read Reviews</button>
        """

        url = "https://www.consumeraffairs.com/sample-plan-url"
        data = scrape_data(url)

        self.assertEqual(data["Plan Title"], "Sample Plan")
        self.assertEqual(data["Program Length"], "6 months")
        self.assertEqual(data["Debt Minimum"], "$1000")
        self.assertEqual(data["Reviews"], "Read Reviews")

if __name__ == '__main__':
    unittest.main()
