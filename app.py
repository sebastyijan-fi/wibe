from flask import Flask, render_template
from flask_login import LoginManager, current_user, logout_user
from dotenv import load_dotenv
from database.connection import db, init_db
from routes.registration import bp as registration_bp
from routes.login import bp as login_bp
from routes.logout import bp as logout_bp  # Assuming you named your logout blueprint as 'logout_bp'
from routes.submit_wibe import bp as submit_wibe_bp
from routes.get_wibe import bp as get_wibe_bp
from models.user import User
from flask_cors import CORS
from typing import cast
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    init_db(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route("/")
    def home():
        user = cast(User, current_user)
        if user.is_authenticated:
            return render_template("frontpage.html", user=user)
        else:
            return render_template("index.html")  # Redirect to index page if user is not authenticated

    app.register_blueprint(registration_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(logout_bp)
    app.register_blueprint(submit_wibe_bp)
    app.register_blueprint(get_wibe_bp)

    return app

app = create_app()

if __name__ == '__main__':
    print("Starting the application...")
    app.run(port=2121, debug=True)
    print("Application ended.")
