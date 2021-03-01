# Yakutia Tripp

This project is a site for travel company

## Getting Started

These instructions will get you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on how to deploy the project on a live system.

### Installing

If you want to run this project on your PC you need to install:

* `python-3.9`
* `pipenv`
* `postgresql`

After you install it you need to install dependencies using pipenv

```
$ pipenv install --dev
```

Create a file with environment variables `.env` with the following content:

```
DJANGO_SECRET_KEY="<django_secret_key>"
DJANGO_ENVIRONMENT=development
```

After that you need to create a new PostgreSQL DB with name `yakutiatripp`

```
$ createdb yakutiatripp
```

And create a new superuser for DB with name `django`

## Running the tests

To run the tests you need to run the following command:

```
$ python manage.py test
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

This project is licensed under the [GNU General Public License](LICENSE.md)
- see the [LICENSE.md](LICENSE.md) file for details
