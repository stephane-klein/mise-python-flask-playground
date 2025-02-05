import os
import click
from flask import Flask, render_template
from flask.cli import with_appcontext
from flask_migrate import Migrate

from models import User, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("POSTGRES_URL") or exit("POSTGRES_URL environment variable is required")

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def hello_world():
    return render_template(
        'hello.html',
        users=User.query.all()
    )

def init_db():
    db.drop_all()
    db.create_all()

@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")

app.cli.add_command(init_db_command)
