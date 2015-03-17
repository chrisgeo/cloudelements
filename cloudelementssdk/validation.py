import logging
from validictory import SchemaValidator, validate
from validictory import ValidationError, SchemaValidator, FieldValidationError

log = logging.getLogger(__name__)


class NoDataException(Exception):
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message
        log.debug('[event=no_data_exception] Missing data')


def validate_schema(schema):
    def wrapper(func):
        def decorator(*args, **kwargs):
            # For data, we expect it to
            # be in the second or third position
            # in the tuple since the methods follow
            # the format of self, id, data
            data = None
            l = len(args)

            if l == 2:
                data = args[1]
            elif l == 3:
                data = args[2]

            if not data:
                raise NoDataException("Missing Data")

            try:
                validate(data, schema)
            except ValidationError as validation_error:
                log.info(
                    "[event=validate_schema][schema=%s] "
                    "Could not validate schema against data=%s",
                    schema, data
                )
                log.info(
                    '[event=validate_schema] Schema valiation message=%s',
                    validation_error.message
                )
                return False

            return func(*args, **kwargs)
        return decorator
    return wrapper
