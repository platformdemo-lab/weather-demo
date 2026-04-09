# Weather Service

Simple Flask-based weather API with minimal UI.

---

## Endpoints:

`GET /`
- Returns UI

`GET /weather?city=<city>`
- Returns weather data

Example:
 `/weather?city=Mumbai`

---
## Secrets

Environment variable required: `API_KEY=<openweather-api-key>`

---

## Run locally

```sh
docker build -t weather-service .
docker run -d -p 5000:5000 -e API_KEY=<key> weather-service
```
---

## Project structure:

- src/
    - app.py
    - templates/
    - static/

- tests/
    - test_app.py

- requirements.txt
- Dockerfile
- Jenkinsfile

---

## Notes:
- UI calls /weather API
- No secrets stored in code
- CI/CD handled via shared pipeline