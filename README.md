# Flask application for validating static chamber measurements.

## Running the app.

Clone the repo with:
```
git clone https://github.com/kootepe/ac_dash.git
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

You can change the database user and password in ```docker-compose.yml```, note
that you will need to change DATABASE_URL in ```.env.dev``` also.
```
docker compose up --build
```
This will run the flask development server. It's fully functional, but flask is
full of holes and flask is intended to be ran inside a WSGI server.
