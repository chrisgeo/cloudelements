import pytest
from mock import patch


def test_validate_decorator():
    from cloudelementssdk.validation import validate_schema
    from cloudelementssdk.validation import NoDataException

    schema = {
        'type': 'object',
        'properties': {
            'first': {
                'type': 'string',
                'minLength': 1,
                'blank': False
            },
            'last': {
                'type': 'integer'
            }
        }
    }

    @validate_schema(schema=schema)
    def temp_func(self, id, data):
        return True

    resp = temp_func(object(), 1, dict(first='foo', last=1))
    assert resp is True

    with pytest.raises(NoDataException) as exc:
        temp_func(1)
    assert exc.value.message == 'Missing Data'
