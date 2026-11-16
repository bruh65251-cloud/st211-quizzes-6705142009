from unittest.mock import Mock

def test_was_called():
    mock = Mock()
    mock.save() #this is one save,; duplicate this line to add more saves
    mock.save.assert_called() #at least once!!!!!!! 

def test_was_called_once():
    mock = Mock()
    mock.save()
    mock.save.assert_called_once() #only once!!!!!!!

#can be used if the sales, emails are duplicated.  