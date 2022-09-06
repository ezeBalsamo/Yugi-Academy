# Virtualenv on Windows

You can create one for your Python project by executing the following commands

```shell
python3 -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

This will create a virtualenv in a directory named venv.
It will be assigned execution permissions.

Then, you can activate it by executing the following command

```shell
.\venv\Scripts\activate
```
