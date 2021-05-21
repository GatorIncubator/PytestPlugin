"""Adding a pytest plugin that send report to email"""

import yagmail
import pandas as pd


def pytest_addoption(parser):
    """Turn email features on with --mail option."""
    group = parser.getgroup('mail')

    group.addoption("--mail", action="store_true",
                    help="mail: send test report to user's email")

    group.addoption("--emailto", action="store", dest="emailto",
                    default=None, help="email-to: enter the receiver email")

    group.addoption("--emailfrom", action="store", dest="emailfrom",
                    default=None, help="email-to: enter your email")

    group.addoption("--pwd", action="store", dest="pwd",
                    default=None, help="--password: enter your email password")


def pytest_terminal_summary(terminalreporter, config):
    """Sending report to email"""
    passed = len(terminalreporter.stats.get('passed', ""))
    failed = len(terminalreporter.stats.get('failed', ""))
    error = len(terminalreporter.stats.get('error', ""))
    skipped = len(terminalreporter.stats.get('skipped', ""))
    xfailed = len(terminalreporter.stats.get('xfailed', ""))
    xpassed = len(terminalreporter.stats.get('xpassed', ""))

    total = passed + failed + error + skipped + xfailed + xpassed

    body = {"Passed test": passed,
            "Failed test": failed,
            "Error test" : error,
            "Skipped test": skipped,
            "Xfailed test": xfailed,
            "Xpassed test": xpassed,
            "Total test": total}

    body_df = pd.DataFrame(list(body.items()), columns=['Status', 'Amount of test'])

    if config.getoption("--mail") is True:
        receiver = str(config.option.emailto)
        pwd = str(config.option.pwd)
        sender = str(config.option.emailfrom)
        yagmail_prompt(body_df, sender, pwd, receiver)


def yagmail_prompt(body, sender, pwd, receiver):
    """Set up the email content and address"""
    try:
        yag = yagmail.SMTP(user=sender, password=pwd)
        yag.send(
            to=receiver,
            subject="Test stats of your latest pytest",
            contents=body
        )
        print("Email succeffully")
    # pylint: disable=broad-except
    except Exception:
        print('The user does not exist with that ID')
