# Project2-Team7

.. contents:: **pytest-md-report-email-feature**
   :backlinks: top
   :depth: 2


A pytest plugin to make a test results report with Markdown table format and then sends the Markdown file to a user's email address.


## Dependencies

- Python 3.6+
- `Python package dependencies (automatically installed)`

## Installation

You can clone this repository with the following command

```
git clone git@github.com:allegheny-computer-science-203-s2021/PytestPlugin-Team7.git
```

`cd` into the project root folder:

```bash
cd PytestPlugin-Team7.git
```

This program uses [Pipenv](https://github.com/pypa/pipenv) for dependency management.

- - If needed, install and upgrade the `pipenv` with `pip`:

  ```bash
  pip install pipenv -U
  ```

- To create a default virtual environment and use the program:

  ```bash
  pipenv install
  ```

## Email plugin: plugin-email

- Run command:

```
pipenv run pytest --mail --emailfrom="test@gmail.com" --pwd="XXXXXX" --emailto="test1@gmail.com"

```
- Argument included:

- `--mail`: Enable email plugin when called
- `--emailfrom`: Store the email address of the sender
- `--pwd`: Store the password of the sender's email
- `--emailto`: Store the email address of the receiver
