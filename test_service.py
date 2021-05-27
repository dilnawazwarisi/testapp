from service import get_message


def test_get_message():
    resp = get_message('jabba')
    assert resp == 'Hi jabba'


def test_get_message2():
    resp = get_message('jabbaa')
    assert resp == 'Hi jabbaa'