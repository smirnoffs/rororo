2.0.0 (In Development)
----------------------

2.0.0a4 (2019-10-22)
--------------------

- feature: Parse API Key & HTTP security data for OpenAPI operation
- chore: Cover ``rororo.openapi`` with non-machine docs
- chore: Provide another example on using OpenAPI schema inside aiohttp web
  application
- feature: Allow to remove root handlers on setting up logging config

2.0.0a3 (2019-10-09)
--------------------

- feature: Support `type: array` request bodies as well
- feature: Allow to validate responses against OpenAPI schema
- chore: Do not directly depend on ``jsonschema``

2.0.0a2 (2019-10-08)
--------------------

- fix: Depend on ``aiohttp>=3.5,<4.0``

2.0.0a1 (2019-10-08)
--------------------

- feature: Add ``rororo.get_openapi_context`` shortcut
- chore: Update API docs for ``rororo.openapi`` public functions & classes

2.0.0a0 (2019-10-08)
--------------------

- **feature: Complete library rewrite**

  - Instead of targeting any Python web framework, make ``rororo`` support only
    ``aiohttp.web`` applications
  - Build the library around the OpenAPI 3 schema support for ``aiohttp.web``
    applications
  - As result entirely remove ``rororo.schemas`` package from the project

1.2.1 (2019-07-08)
------------------

- Publish 1.2.1 release

1.2.1a1 (2019-07-03)
--------------------

- chore: Introduce ``pre-commit`` hooks
- chore: Use ``pytest`` for tests
- chore: Use ``black`` for code formatting

1.2.1a0 (2019-02-24)
--------------------

- fix: Do not yet depend on ``jsonschema>=3.0.0``
- chore: Move ``tox.ini`` content into ``pyproject.toml``
- chore: Only use poetry for install project deps for tests & lint

1.2.0 (2018-11-01)
------------------

- Publish 1.2.0 release

1.2.0a1 (2018-10-22)
--------------------

- Make all project packages `PEP-561 <https://www.python.org/dev/peps/pep-0561/>`_
  compatible

1.2.0a0 (2018-10-18)
--------------------

- Python 3.7 support
- Ensure that ``rororo`` works well with latest ``aiohttp``
- Allow setting ``level`` on updating logging dict to use Sentry handler
- Add new ``rororo.timedelta`` module with utilities to work with timedeltas
- Add new ``rororo.utils`` module
- Move type annotations to ``rororo.annotations`` module

1.1.1 (2017-10-09)
------------------

- Do not attempt to convert empty list to dict for request/response data

1.1.0 (2017-10-09)
------------------

- Allow to supply non-dicts in request/response data

1.0.0 (2017-05-14)
------------------

- Publish 1.0 release, even proper docs are not ready yet

1.0.0b1 (2017-05-13)
--------------------

- Annotate all code in ``rororo``
- Use `mypy <http://mypy.readthedocs.io/>`_ on linting source code
- Require Python 3.5 or higher due to changes above

1.0.0a5 (2016-10-23)
--------------------

- Support validating schema via `fastjsonschema
  <http://opensource.seznam.cz/python-fastjsonschema/>`_ or any other validator

1.0.0a4 (2016-09-01)
--------------------

- Pass ``kwargs`` to ``SentryHandler`` on configuring Sentry logging

1.0.0a3 (2016-08-08)
--------------------

- Add ``rororo.aio`` module with:

  - ``add_resource_context`` context manager
  - ``is_xhr_request``, ``parse_aioredis_url`` utility functions

- Update flake8 config & bump aiohttp version for tests
- Added ChangeLog & modified GitHub Releases Page

1.0.0a2 (2015-12-18)
--------------------

- Adds ability to supply custom error class while making manual errors by
  ``schema.make_error`` method
- Default validator class preset default values from schema to instance for
  validation
- Several improvements to test process

1.0.0a1 (2015-11-26)
--------------------

- New beginning for rororo project. Now it is a bunch of helper methods instead
  of yet another web-framework.
