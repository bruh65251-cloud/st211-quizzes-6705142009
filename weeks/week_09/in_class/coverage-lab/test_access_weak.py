from access import check_access

def test_admin_active():
    assert check_access("admin", True) == "granted"

def test_user_inactive():
    assert check_access("user", False) == "denied"

#even tho 100%, it is not granted that you test all the functions and lines, there are other way round like admin_inactive, user-active, in that case, use branch coverage.