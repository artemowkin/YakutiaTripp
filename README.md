# Yakutia Tripp

[![Coverage Status](https://coveralls.io/repos/github/artemowkin/YakutiaTripp/badge.svg?branch=dev)](https://coveralls.io/github/artemowkin/YakutiaTripp?branch=dev)
[![Build Status](https://travis-ci.com/artemowkin/YakutiaTripp.svg?branch=main)](https://travis-ci.com/artemowkin/YakutiaTripp)

This project is a site for travel company

## Getting Started

These instructions will get you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on how to deploy the project on a live system.

### Installing

If you want to run this project on your PC you need to install:

* `python-3.9`
* `pipenv`
* `docker`
* `docker-compose`

Create a file with environment variables `.env` with the following content:

```
DJANGO_SECRET_KEY="<django_secret_key>"
```

Run building of docker container:

```
$ sudo docker-compose build
```

And up this container

```
$ sudo docker-compose up -d
```

## API Docs

You can read documentation for API on http://localhost:8000/redoc/

## Running the tests

To run the tests you need to run the following command:

```
$ docker-compose run web python manage.py test
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code
of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions
available, see the [tags on this
repository](https://github.com/PurpleBooth/a-good-readme-template/tags).

## Authors

  - **Artyom Loskan** (https://github.com/artemowkin/) - backend developer
  - **Kirill Shurov** (https://github.com/steelWinds/) - frontend developer

## License

This project is licensed under the [GNU General Public License](LICENSE.md) -
see the [LICENSE.md](LICENSE.md) file for details
