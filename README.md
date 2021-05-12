# Project2-Team7

.. contents:: **pytest-md-report-email-feature**
   :backlinks: top
   :depth: 2


A pytest plugin to make a test results report with Markdown table format and then sends the Markdown file to a user's email address.


Dependencies
============================================
- Python 3.6+
- `Python package dependencies (automatically installed)`

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
