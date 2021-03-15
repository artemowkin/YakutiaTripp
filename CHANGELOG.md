# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased 1.0.0]

### Frontend

#### Added

- `feedback.html` template with form to create a review
- `index.html` template with main site page

### Backend

#### Added

- `AllNewsView` to render all news on `/api/news/` endpoint
- `BaseService` is a base service class for all services
- `BaseGetService` is a base service to get model entries
- `GetNewsService` is a service to get `News` model entries
- `News` model with `title`, `preview`, `text`, and `pub_date` fields
- `NewsSerializer` is a serializer for `News` model
- `ConcreteNewsView` to render a concrete news on `/api/news/{news_pk}/`
endpoint
- `LastNewsView` to render last 9 news on `/api/news/last/` endpoint
- `AllToursView` to render all tours on `/api/tours/` endpoint
- `GetToursService` is a service to get `Tour` model entries
- `Tour` model with `uuid`, `title`, `preview`, `short_description`,
`about`, `price`, `city_from`, `city_to` and `views` fields
- `TourDay` model with `weekday`, `description` and `tour` fields
- `TourSerializer` is a serializer for `Tour` model
- `ConcreteTourView` to render a concrete tour on `/api/tours/{tour_pk}/`
endpoint
- `GetToursService.get_concrete` returns a concrete tour with incremented
`views` field
- `SearchToursView` to render searched tours on
`/api/tours/search/{city_from}/{city_to}/{date}/`
- `SearchToursService` to search tours by `city_from`, `city_to`, and `date`
- `AllReviewsView` to render all moderated reviews on `/api/reviews/`
- `GetReviewsService` is a service to get `Review` model entries
- `Review` model with `name`, `avatar`, `rating`, `text`, `moderated`,
`pub_date` fields
- `ReviewSerializer` is a serializer for `Review` model
- `CreateReviewService` is a service to create a new review using `name`,
`rating`, and `text`
- `AllReviewsView` POST method to create a new review
- `set_review_avatar` is a service function to set avatar for review
- `SetReviewAvatarView` supports PATCH requests on `/api/reviews/{review_pk}/`
and sets avatars for reviews
