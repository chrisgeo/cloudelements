import pytest
from mock import patch


def test_validate_decorator():
    from cloudelementssdk.validation import validate_schema

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
    def temp_func(self, data):
        return True

    resp = temp_func(object(), dict(first='foo', last=1))
    assert resp is True

    @validate_schema(schema=schema)
    def temp_func(self, id, data):
        return True

    resp = temp_func(object(), 1, dict(first='foo', last=1))
    assert resp is True


def test_validate_decorator_fails():
    from cloudelementssdk.validation import validate_schema
    from cloudelementssdk.validation import NoDataException, ValidationError

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
    def temp_func(self, data):
        return True

    resp = temp_func(object(), dict(first='foo', last='foo'))
    assert resp == [{'error': 'foo', 'field': 'last', 'msg': "Value 'foo' for field '<obj>.last' is not of type integer"}]

    with pytest.raises(NoDataException) as exc:
        temp_func(1)
    assert exc.value.message == 'Missing Data'
