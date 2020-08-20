# zkan

Experiments in making a very very lightweight data platform.

## Docs

[Development](docs/DEVELOPMENT.md)

## Overview

zkan is actually an excuse to use some shiny technologies to solve an already solved
problem :-)

The first step is constructing a RESTful service that manages metadata
for datasets, inspired by [CKAN](https://ckan.org) and
[DKAN](https://getdkan.org).  The data models of these platforms have
in turn been inspired by the
[W3C DCAT](https://www.w3.org/TR/vocab-dcat-2/) specification, and often
specifically by the
[DCAT-US](https://resources.data.gov/resources/dcat-us/) flavor used
by the US Federal government.

Essentially, a *dataset* is a collection of structured data objects
with some unified metadata.  These structured data objects are known
as *distributions*, have their own metadata, and represent a view on
the dataset.

A *catalog* is a collection of datasets.

For example, a dataset describing the annual temperature ranges for cities
might have a title ("Annual Temperature Ranges for Certain Cities") and 4
distributions:

* The data in CSV form
* The data as an Excel spreadsheet
* The data dictionary as a text document
* A URL to an API that provides access to the underlying data

The first phase of this project is to provide a simple RESTful API that allows
datasets and distributions to be created, updated, and deleted.

Subsequent phases would add:

* A search service, that allows datasets to be queried.  For example,
  find me all datasets having to do with "annual temperature".
* A datastore service, that allows the data in distributions to be stored and
  queried.  For example, return the minimum and maximum temperatures
  for a selected city over time.
* An export service, that would export catalog metadata.  For example,
  support a *data.json* endpoint.  (See the
  [DCAT-US](https://resources.data.gov/resources/dcat-us/) for
  details.)
* A simple React/Vue/??? based front end

## Shiny Technology

* Python 3 whenever possible
* Docker (and docker-compose) for development and CI
* [MongoDB](https://www.mongodb.com/) for persistence
* [JSON Schema](https://json-schema.org/) for validation
* [pytest](https://docs.pytest.org/en/stable/) for unit (and possibly functional) tests
* [cypress](https://www.cypress.io/) for integration tests, maybe?  Might be better
  to just use pytest and save cypress for the front end!
* [Pydantic](https://pydantic-docs.helpmanual.io/) and
  [Starlette](https://www.starlette.io/) and
  [FastAPI](https://fastapi.tiangolo.com/) to build the service
* [OAUTH2](https://oauth.net/2/) for authz
* [flake8](https://pypi.org/project/flake8/) for linting
* [black](https://pypi.org/project/black/) for code formatting
* [SNYK](https://snyk.io/) and/or dependabot for vulnerability analysis
* [Poetry](https://python-poetry.org/) for dependency management
* [Markdown](https://www.markdownguide.org/) for documentation
* [Hypothesis](https://hypothesis.readthedocs.io/en/latest/) for cool
  property-based tests
* GitHub Actions for CI
* Some Yet To Be Determined cloud platform for deployment

## Architecture (work in progress)

* Don't reinvent anything.  Well, except for an open data platform.
* Schemas should be first class objects.  This will make development
  easy, because we can get started with very simple schemas (e.g.,
  datasets have a title, distributions have a URL) and add the
  complicated stuff later (e.g., tags)
* JSON everywhere
* Simple but sufficient role based authorization.
* Let MongoDB do heavy lifting
* [[Contentious]] Since MongoDB will store any JSON, and we can
  decouple validation from persistence, we can make "is this dataset
  valid?" an attribute of a dataset and persist invalid datasets.
  This allows easy support of "draft" forms of datasets, which makes
  all sorts of workflows possible (either via a front end or API)
* Versioning.  Something really simple, like just save old versions of
  datasets as MongoDB documents. See
  https://www.mongodb.com/blog/post/building-with-patterns-the-document-versioning-pattern
  


