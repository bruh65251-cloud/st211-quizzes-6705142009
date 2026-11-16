from unittest.mock import patch
from notification import notify_user

def test_notify_user_without_sending_email():
    with patch('notification.send_email') as mock_send:
        mock_send.return_value = True

        result = notify_user("student@siam.ac.th")
    assert result == "Notified student@siam.ac.th"
