web: gunicorn main:app
services:
  - type: web
    name: flask-api
    env: python
    buildCommand: ""
    startCommand: gunicorn main:app
    envVars:
      - key: FLASK_ENV
        value: production
    autoDeploy: true
