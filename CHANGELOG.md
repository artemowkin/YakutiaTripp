# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased 1.0.0]

### Frontend



### Backend

#### Added

- `AllNewsView` to render all news on `/api/news/` endpoint
- `BaseService` is a base service class for all services
- `BaseGetService` is a base service to get model entries
- `GetNewsService` is a service to get News model entries
- `News` model with `title`, `preview`, `text`, and `pub_date` fields
- `NewsSerializer` is a serializer for `News` model
- `ConcreteNewsView` to render a concrete news on `/api/news/{news_pk}/` endpoint
- `LastNewsView` to render last 9 news on `/api/news/last/` endpoint
- `AllToursView` to render all tours on `/api/tours/` endpoint
- `GetToursService` is a service to get Tour model entries
- `Tour` model with `uuid`, `title`, `preview`, `short_description`,
`about`, `price`, `city_from`, `city_to` and `views` fields
- `TourDay` model with `weekday`, `description` and `tour` fields
- `TourSerializer` is a serializer for `Tour` model
- `ConcreteTourView` to render a concrete tour on `/api/tours/{tour_pk}/` endpoint
- `GetToursService.get_concrete` returns a concrete tour with incremented `views` field
- `SearchToursView` to render searched tours on `/api/tours/search/{city_from}/{city_to}/{date}/`
- `SearchToursService` to search tours by `city_from`, `city_to`, and `date`
