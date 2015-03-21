CLOUD ELEMENTS PYTHON SDK
==========================

This SDK is a basic wrapper around the HTTP/S calls needed to use CloudElements

Current Version: 0.1
------
* Mostly SalesForce and CRM Hub integration


##INSTALLATION
```shell
    git clone git@github.com:MobileWorks/cloudelements.git cloudelements
    cd cloudelements
    pip install -e .
    pip install -r test-requirements.txt
```

## SETUP
Instead of having set variables in the file, the tests rely on environment variables for your instances.

You can use a tool like [direnv]() or [autoenv]()

Currently the tests use these:

```python
    os.getenv('CLOUD_ELEMENTS_USER_SECRET')
    os.getenv('CLOUD_ELEMENTS_ORG_SECRET')
    os.getenv('SALES_FORCE_SECRET')
    os.getenv('SALES_FORCE_ACCESS_KEY')
    os.getenv('SALES_FORCE_CALLBACK_URL')
```
## RUN TESTS
``` py.test -v ```

OR

```shell
    pip install tox
    tox .
```
