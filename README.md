# Flask application for validating static chamber measurements.

## Running the app.

Clone the repo with:
```
git clone --recurse-submodules https://github.com/kootepe/ac_dash_app.git
```
Add file ```.env.dev``` in the root folder with this content:
```
FLASK_APP=project/__init__.py
FLASK_DEBUG=1
DATABASE_URL=postgresql://hello_flask:hello_flask@db:5432/hello_flask_dev
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
FLASK_CONFIG=project.ac_dash.ac_dash.db.Config
```

To run the app, go to root of the repo and run:
```
docker compose up
```
To completely reset the app and the db:
```
docker-compose down -v; docker compose up --build
```

Full deployment instructions to come.

## Usage:

[Instructions for initiating data and navigating the app here.](docs/instructions.md)
