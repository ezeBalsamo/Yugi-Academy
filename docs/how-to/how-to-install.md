# How to install

First of all, you need to clone the repository:

```shell
git clone https://github.com/ezeBalsamo/Yugi-Academy.git
```

This will clone the project in Yugi-Academy/

The project follows this directory structure

- `assets/` : Static resources
- `docs/` : Documentation
  - `README.md` : Documentation readme
  - `how-to/` : [How-to guides](https://documentation.divio.com/how-to-guides/)
- `README.md` : Readme
- `CONTRIBUTING.md` : Contribution Guidelines
- `LICENSE` : MIT License

As you can see, the source code is in the root directory.
All the following commands must be executed from there.

From there, we suggest you to use virtual environments.
Feel free to read how to create a virtualenv:

- [on Windows](how-to-create-virtualenv-on-windows.md)

- [on Linux](how-to-create-virtualenv-on-linux.md)

Once you have configured the virtual environment, you'll need to install the requirements.

To do this, you can execute:

For development:

```shell
pip install -r dev-requirements.txt
```

For production:

```shell
pip install -r requirements.txt
```

This project requires `Django` and `python-dotenv`.
The latter one is for managing the secret key in the `.env` file.

For the development process, you can generate an `.env` file with a secret key with:

```shell
cp .env.example .env
python -c 'from django.core.management.utils import get_random_secret_key;print(get_random_secret_key())'
```

A new random secret key will be generated.
You have to copy it and replaced it the `.env` file.
For instance, if the secret is:

`6(j^4d9wvx)%=6a1glire*mmid-ynnslt2=)vdbf_rqhf(6=gv`

Then, your `.env` _SECRET_KEY_ variable should look like this

`SECRET_KEY=6(j^4d9wvx)%=6a1glire*mmid-ynnslt2=)vdbf_rqhf(6=gv`

From here, we need to prepare the database and migrate the model definitions.

```shell
python manage.py migrate
```

One last step remains. You must create a superuser.

```shell
python manage.py createsuperuser
```

The prompt will require you, in order:

- The username

- An email address

- The password

- The password confirmation

If all went well, you should see a message like the following:

`Superuser created successfully.`

You are almost ready.
In order to play around with your application, you need to start the server.

```shell
python manage.py runserver
```

Congratulations, your application is up and running.

Go to `http://localhost:8000/` and have fun, because it's time to duel!
