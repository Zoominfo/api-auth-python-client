# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [2.0.0] - 2022-12-20

### Major change

- Fix: Follow up to the fix of [#4](https://github.com/Zoominfo/api-auth-python-client/issues/4) in `1.0.2` #4
  - Ensure we support status code in the error response

When you upgrade, make sure to handle `HttpError` instead of `RuntimeError`.

### Changed features

- Update `PyJwt` to latest version 2.6.0
- Update `requests` to latest version 2.28.1
- Update `cryptography` to latest version 38.0.4