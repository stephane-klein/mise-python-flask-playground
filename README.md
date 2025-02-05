# Python, PostgreSQL, and Flask with Migrations playground

Here is a minimalist playground of a project based on Python, Flask-SQLAlchemy, Flask-Migrate and PostgreSQL launched via Docker.

The environment installation method has been documented for MacOS, Linux (Ubuntu and Fedora) and Windows 10 and 11 with WSL.

## Prepare your computer

The purpose of this part is to install Mise and Docker on your Workstation.

### On OSX: install Docker and Mise with Brew

Brew is a popular package manager on *macOS*.
However, it does not come pre-installed: follow the instructions from the Brew [Website](https://brew.sh/index_fr):

```sh
$ brew install git mise colima docker docker-compose
$ cat << EOF > ~/.docker/config.json
{
    "auths": {},
    "currentContext": "colima",
    "cliPluginsExtraDirs": [
        "/opt/homebrew/lib/docker/cli-plugins"
    ]
}
EOF
$ brew services start colima
```

### On MS Windows 10, 11 with WSL2

Instructions for installing and accessing an Ubuntu environment on Windows:

Open "Powershell" and execute:

```sh
$ wsl --install
```

Reboot.

Still in Powershell:

```sh
$ wsl --update
$ wsl --install -d Ubuntu-24.04
$ wsl --set-version Ubuntu-24.04 2
```

Then run this command and create your user account by entering your username and password:

```
$ wsl -d Ubuntu-24.04
Installing, this may take a few minutes...
Please create a default UNIX user account. The username does not need to match your Windows username.
For more information, visit: https://aka.ms/wslusers
Enter new UNIX username:
...

$
```

And normally, you should have a shell opened under Ubuntu and you can follow the Ubuntu-specific installation instructions.

### On Ubuntu: install Docker and Mise with apt

Install with *dnf* ([see official Mise instructions](https://mise.jdx.dev/installing-mise.html#apt))

```sh
$ apt update -y && apt install -y gpg sudo wget curl
$ sudo install -dm 755 /etc/apt/keyrings
$ wget -qO - https://mise.jdx.dev/gpg-key.pub | gpg --dearmor | sudo tee /etc/apt/keyrings/mise-archive-keyring.gpg 1> /dev/null
$ echo "deb [signed-by=/etc/apt/keyrings/mise-archive-keyring.gpg arch=amd64] https://mise.jdx.dev/deb stable main" | sudo tee /etc/apt/sources.list.d/mise.list
$ sudo apt update
$ sudo apt install -y mise
```

And follow there instruction to install Docker Engine on Ubuntu: https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository

### On Fedora: install Mise with dnf

Install with *dnf* ([see official Mise instructions](https://mise.jdx.dev/installing-mise.html#dnf))

```sh
$ sudo dnf install -y dnf-plugins-core
$ sudo dnf config-manager --add-repo https://mise.jdx.dev/rpm/mise.repo
$ sudo dnf install -y mise
```

And follow there instruction to install Docker Engine on Fedora: https://docs.docker.com/engine/install/fedora/#install-using-the-repository



### Configure Mise

If you use **Bash** shell execute:

```sh
$ echo 'eval "$(mise activate bash)"' >> ~/.bashrc
$ source ~/.bash_profile
```

If you use **Zsh** shell execute:

```sh
$ echo 'eval "$(mise activate zsh)"' >> "${ZDOTDIR-$HOME}/.zshrc"
$ source ~/.zsrhrc
```


## Getting started

```sh
$ mise trust
$ mise install
$ docker compose up --wait
$ pip install -r requirements.txt
```

If you just ran `docker compose up --wait`, you need to reload `.envrc` to update the `POSTGRES_URL` environment variable:

```sh
$ source .envrc
```

Here are the available Flask commands:

```sh
$ flask
Commands:
  db       Perform database migrations.
  init-db  Clear existing data and create new tables.
  routes   Show the routes for the app.
  run      Run a development server.
  shell    Run a shell in the app context.
```

Starting the database initialization:

```sh
$ flask init-db
```

Starting the HTTP server in development mode with auto-reload:

```sh
$ flask run
 * Serving Flask app 'src.app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

## Jouons un peu avec les migrations de modèle de données

When `migrations/versions/` is empty, first initialize with:

```sh
$ flask db init
```

After modifying your data model, you can generate a migration file with:

```sh
$ flask db migrate -m "add user.lastname"
```

Launch migrations with:

```sh
$ flask db upgrade
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
```
