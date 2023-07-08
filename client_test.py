import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {
                "top_ask": {"price": 121.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(
                getDataPoint(quote),
                (
                    quote["stock"],
                    quote["top_bid"]["price"],
                    quote["top_ask"]["price"],
                    ((quote["top_bid"]["price"] + quote["top_ask"]["price"]) / 2),
                ),
            )

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {
                "top_ask": {"price": 119.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(
                getDataPoint(quote),
                (
                    quote["stock"],
                    quote["top_bid"]["price"],
                    quote["top_ask"]["price"],
                    ((quote["top_bid"]["price"] + quote["top_ask"]["price"]) / 2),
                ),
            )

    """ ------------ Add more unit tests ------------ """

    def test_getRatio_calculateRatio(self):
        quotes = [
            {
                "top_ask": {"price": 119.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]

        price_A = (quotes[0]["top_bid"]["price"] + quotes[0]["top_ask"]["price"]) / 2
        price_B = (quotes[1]["top_bid"]["price"] + quotes[1]["top_ask"]["price"]) / 2

        self.assertEqual(
            getRatio(price_A, price_B),
            (price_A / price_B),
        )

    def test_getRatio_calculatePriceA_Zero(self):
        quotes = [
            {
                "top_ask": {"price": 0, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 0, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]

        price_A = (quotes[0]["top_bid"]["price"] + quotes[0]["top_ask"]["price"]) / 2
        price_B = (quotes[1]["top_bid"]["price"] + quotes[1]["top_ask"]["price"]) / 2

        self.assertEqual(
            getRatio(price_A, price_B),
            (price_A / price_B),
        )

    def test_getRatio_calculatePriceB_Zero(self):
        quotes = [
            {
                "top_ask": {"price": 119.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 0, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 0, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]

        price_A = (quotes[0]["top_bid"]["price"] + quotes[0]["top_ask"]["price"]) / 2
        price_B = (quotes[1]["top_bid"]["price"] + quotes[1]["top_ask"]["price"]) / 2

        self.assertEqual(getRatio(price_A, price_B), None)


if __name__ == "__main__":
    unittest.main()
