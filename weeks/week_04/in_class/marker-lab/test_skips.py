import pytest
import sys

@pytest.mark.skip(reason="Features not implemented yet")
def test_future_feature():
    assert False #would fail, but is skipped

@pytest.mark.skipif(sys.version_info < (3,8), reason="Requires Python 3.8+")
def test_needs_modern_python():
    assert True #this test will only run if Python version is 3.8 or higher
    