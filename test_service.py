from service import get_message


def test_get_message():
    resp = get_message('jabba')
    assert resp == 'Hi jabba'