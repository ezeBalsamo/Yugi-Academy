# Virtualenv on Windows

You can create a virtualenv for your Python project on Windows by executing the following commands

```shell
python3 -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

This will create a virtualenv in a directory named venv and assigned execution permissions on it.

Then, you can activate it by executing the following command

```shell
.\venv\Scripts\activate
```