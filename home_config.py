import os
import dotenv
from flask import Flask

app = Flask(__name__)

dotenv.load_dotenv(override=True)

if os.environ.get("LOCATION") == "home":
    app.config.from_pyfile("config/development.py")
else:
    app.config.from_pyfile("config/production.py")

print(app.config.get("LOCATION"))
