# iploka
Get geolocation information from any IP addresses. Get free API Key from https://iploka.com for free-forever 10,000 monthly requests.

`iploka` was developed by [Howuku](https://howuku.com). Howuku is an all-in-one CRO & analytics tool to help you optimize conversion rates and user experience.

[![PYTHON Version](https://img.shields.io/pypi/v/iploka-python)](https://pypi.org/project/iploka-python/)

## Features

- Free up to 10,000 monthly request
- Support both IPv4 and IPv6
- Additional timezone, currency and connection information

## Installation

- Include package in your project

```sh
$ pip install iploka-python
```

#### How to use

```python
from iploka_geoip import GeoIP

geoip = GeoIP("YOUR_API_KEY")
# lookup ip address of the specified ip
data = geoip.lookup("134.201.250.155")
print(data)

```
- And the complete result will be returned:
```python
{
  "ip": "134.201.250.155",
  "type": "ipv4",
  "continent_code": "NA",
  "continent_name": "North America",
  "country_code": "US",
  "country_name": "United States",
  "region_code": "CA",
  "region_name": "California",
  "city": "Los Angeles",
  "latitude": 34.003,
  "longitude": -118.4298,
  "location": {
    "geoname_id": 4135386,
    "capital": "Washington",
    "languages": [
      {
        "code": "en-US",
        "name": "English"
      }
    ],
    "country_flag": "https://flagpedia.net/data/flags/h80/us.png",
    "country_flag_emoji": "🇺🇸",
    "country_flag_emoji_unicode": "U+1F1FA U+1F1F8",
    "calling_code": "1",
    "is_eu": false
  },
  "time_zone": {
    "id": "America/Los_Angeles",
    "current_time": "2021-06-29T20:01:53-07:00",
    "gmt_offset": -25200,
    "code": "-07",
    "is_daylight_saving": true
  },
  "currency": {
    "code": "USD",
    "name": "Us Dollar",
    "plural": "Us Dollars",
    "symbol": "$",
    "symbol_native": "$"
  },
  "connection": {
    "asn": 30722,
    "isp": "Vodafone Italia S.p.A."
  }
}
```


#### Example tests for iploka module

```python
class GetRespTest(BaseTest):
    """Tests for our helper function: ``_get_resp``."""

    def test_returns_response(self):
        self.assertIsInstance(_get_resp('test', 'test'), Response)


class GeoIPLookupTest(BaseTest):
    """Tests for our ``GeoIP.lookup()`` method."""

    def test_raises_connection_error_on_connection_error(self):
        import iploka_geoip

        iploka_geoip.geoip.API_URI = 'https://api.asdgasggasgdasgdsasgdasdfadfsda.com'
        geoip = iploka_geoip.GeoIP('test')

        self.assertRaises(ConnectionError, geoip.lookup, '8.8.8.8')

    def test_raises_geoip_exception_on_error(self):
        import iploka_geoip

        iploka_geoip.geoip.API_URI = 'https://api.asdgasggasgdasgdsasgdasdfadfsds.com'
        geoip = iploka_geoip.GeoIP('test')

        self.assertRaises(GeoIPException, geoip.lookup, '8.8.8.8')

    def test_raises_service_error_on_error(self):
        import iploka_geoip

        iploka_geoip.geoip.API_URI = 'https://api.ipify.org/woo'
        geoip = iploka_geoip.GeoIP('test')

        self.assertRaises(ServiceError, geoip.lookup, '8.8.8.8')

    def test_returns_geoip_data(self):
        import iploka_geoip

        iploka_geoip.geoip.API_URI = 'https://api.iploka.com/api/v1'
        geoip = iploka_geoip.GeoIP(environ.get('API_KEY'))

        self.assertEqual(geoip.lookup('8.8.8.8')['ip'], '8.8.8.8')
```
### Support

Email: hello@iploka.com