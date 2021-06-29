"""
tests.iploka_geoip.settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~

All tests for our iploka_geoip.settings module.
"""


from unittest import TestCase

from iploka_geoip import __version__
from iploka_geoip.settings import USER_AGENT


class SettingsTest(TestCase):
    """Tests for our settings module."""

    def test_user_agent_contains_library_version(self):
        self.assertTrue(__version__ in USER_AGENT)

    def test_user_agent_contains_python_version(self):
        self.assertTrue('python' in USER_AGENT)
