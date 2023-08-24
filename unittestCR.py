import unittest
from unittest.mock import patch
import scraper


class TestScraper(unittest.TestCase):
    @patch("scraper.requests.get")
    def testScrapeConsumerAffairs(self, mockGet):
        mockResponse = unittest.mock.Mock()
        mockResponse.text = """
        <html>
            <body>
                <a href="https://www.consumeraffairs.com/finance/bofa_gift_card.html" data-ga-data-layer="{&quot;campaign_id&quot;: 1230, &quot;gtm_event&quot;: &quot;brand-click&quot;}" class="ca-a ca-a--bld-no-undln brd-card__tit-nm js-gadatalayer" data-track-goal="buyersguide:profile_entrances:click" data-uapi-link="company_name_cta">
                Bank1
                <a href="https://www.consumeraffairs.com/finance/bofa_gift_card.html" data-ga-data-layer="{&quot;campaign_id&quot;: 1230, &quot;gtm_event&quot;: &quot;brand-click&quot;}" class="ca-a ca-a--bld-no-undln brd-card__tit-nm js-gadatalayer" data-track-goal="buyersguide:profile_entrances:click" data-uapi-link="company_name_cta">
                Bank2
                </a>
                <a href="https://www.consumeraffairs.com/finance/bofa_gift_card.html" data-ga-data-layer="{&quot;campaign_id&quot;: 1230, &quot;gtm_event&quot;: &quot;brand-click&quot;}" class="ca-a ca-a--bld-no-undln brd-card__tit-nm js-gadatalayer" data-track-goal="buyersguide:profile_entrances:click" data-uapi-link="company_name_cta">
                Bank3
                </a>

            </body>
        </html>
        """

        mockGet.return_value = mockResponse

        bankNames = scraper.scrapeConsumerAffairs()
        self.assertEqual(len(bankNames), 3)
        self.assertIn("Bank1", bankNames)
        self.assertIn("Bank2", bankNames)
        self.assertIn("Bank3", bankNames)

    if __name__ == "__main__":
        unittest.main()
