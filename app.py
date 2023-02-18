from flask import Flask
from dotenv import load_dotenv
import os
from routes.auth import login
from routes.index import index
from routes.servers import servers
from routes.shops import shops
from routes.storage import storage
from routes.strategy import strategy
from routes.instruction import instruction
from routes.metrics import metrics

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")
app.config["PERMANENT_SESSION_LIFETIME"] = 86400

app.register_blueprint(login)
app.register_blueprint(index)
app.register_blueprint(servers)
app.register_blueprint(shops)
app.register_blueprint(storage)
app.register_blueprint(strategy)
app.register_blueprint(instruction)
app.register_blueprint(metrics)

if __name__ == "__main__":
    app.run(debug=True)
