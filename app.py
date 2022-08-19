import os
import dotenv
from flask import Flask

app = Flask(__name__)

dotenv.load_dotenv(override=True)

if os.environ.get("APP_CONFIG") == 'development':
    app.config.from_pyfile("config/development.py")
else:
    app.config.from_pyfile("config/production.py")


@app.route("/", methods=["GET"])
def main_page():
    title = app.config.get("TITLE")
    description = app.config.get("DESCRIPTION")
    return f"<p>{title} - {description}</p>"


app.run(host='0.0.0.0', port=8000)
