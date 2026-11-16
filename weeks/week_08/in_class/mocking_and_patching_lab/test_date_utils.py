from unittest.mock import patch
from date_utils import report_name

@patch("date_utils.get_year")
def test_report_name(mock_get_year):
    mock_get_year.return_value = 2030

    assert report_name() == "Report-2030"