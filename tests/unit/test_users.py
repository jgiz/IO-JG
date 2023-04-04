import FuzzyFloat as FuzzyFloat
from flask import Response

from flask.app import add_user


class DictFactory:
    pass
class FuzzyText:
    pass
class FuzzyInteger:
    pass


class UserPayloadFactory(DictFactory):
    name = FuzzyText()
    last_name = FuzzyText()
    email = FuzzyText()
    age = FuzzyInteger(low=0)
    essays_count = FuzzyInteger(low=0)
    rating = FuzzyFloat(low=0)


def userPayloadFactory():
    pass


def test_returns_501() -> None:
    print(userPayloadFactory())
    actual = add_user()
    expected = Response(status=501)
    assert actual.status_code == expected.status_code


#testing