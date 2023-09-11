from Roma import decomposition
import pytest

def test_decomposition():
    assert decomposition(1234) == (1,2,3,4)

