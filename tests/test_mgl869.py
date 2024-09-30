from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.mgl869 import mgl869


class TestMGL869(TestCase):

  @patch("src.mgl869.print")
  @patch("src.mgl869.datetime")
  def test_mgl869(self, datetime_mock: MagicMock, print_mock: MagicMock):
    datetime_mock.now.return_value.__str__.return_value = "datetime"
    mgl869()
    print_mock.assert_called_once_with("Démo MGL869: datetime")
    datetime_mock.now.assert_called_once_with()
    datetime_mock.now.return_value.__str__.assert_called_once_with()
