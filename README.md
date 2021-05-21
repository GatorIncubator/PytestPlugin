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

### Purpose:

In order to help user to have a better systematic method to track their python test trials, the `pytest_email` plugin will send the email with the counts of different status of the test cases in a trial to the user.

* Prerequisite: To be able to send email using this plugin, the user (or the sender) should go the the setting of the email and allow the access from less secure app. Otherwise, the email will not let user send email through Python.


### Essential command

First, the user should clone the main repo of this dual plugin by:

```
git clone https://github.com/allegheny-computer-science-203-s2021/PytestPlugin-Team7.git
```
Then, go into this `PytestPlugin-Team7` directory and locate to the file `plugin.py` by th epath of `pytest_email\plugin.py`. Then, transfer the content of this file to the local `conftest.py` file in the project that user want to use this plugin.

- Finally, within the local directory, run the plugin by the command:

```
pipenv run pytest --mail --emailfrom="test@gmail.com" --pwd="XXXXXX" --emailto="test1@gmail.com"

```
- Argument included:

- `--mail`: Enable email plugin when called
- `--emailfrom`: Store the email address of the sender
- `--pwd`: Store the password of the sender's email
- `--emailto`: Store the email address of the receiver

* Note: The `setup.py` is down for some reason, making the user have to manually use the plugin as local `conftest.py`. We'll work on it.

### Sample result

The report email send from this plugin have the form of:

![Sample email](image/Sample_email.png)
