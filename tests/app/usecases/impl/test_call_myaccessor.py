import pytest
from src.app.usecases.impl.call_myaccessor import CallMyAccessor

@pytest.mark.parametrize("i", [4, 5, 6])
def test_call_myaccessor(i):
    accessor = CallMyAccessor()
    actual = [*accessor.get(), i]
    accessor.add(i)
    assert actual == accessor.get() 
