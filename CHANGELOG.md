# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased 1.0.0]

### Frontend



### Backend

#### Added

- `AllNewsView` to render all news on `/api/news/` endpoint
- `BaseGetService` is a base service to get model entries
- `GetNewsService` is a service to get News model entries
- `News` model with `title`, `preview`, `text`, and `pub_date` fields
- `NewsSerializer` is a serializer for `News` model
- `ConcreteNewsView` to render a concrete view on `/api/news/` endpoint
- `LastNewsView` to render last 9 news on `/api/news/last/` endpoint
