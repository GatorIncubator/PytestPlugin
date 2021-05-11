"""Adding a pytest plugin that send report to email"""

import smtplib
import pytest
from _pytest.terminal import TerminalReporter


def pytest_addoption(parser):
    """Turn email features on with --mail option."""
    group = parser.getgroup('mail')

    group.addoption("--mail", action="store_true",
    help="mail: send test report to user's email")

    group.addoption("--emailto", action="store_true",
    help="email-to: enter the receiver email")

    group.addoption("--emailfrom", action="store_true",
    help="email-to: enter your email")

    group.addoption("--pwd", action="store_true",
    help="--password: enter your email password")


def pytest_terminal_summary(terminalreporter, config):
    """Sending report to email"""
    passed = len(terminalreporter.stats.get('passed', ""))
    failed = len(terminalreporter.stats.get('failed', ""))
    total = passed + failed
    body = {"Passed test": passed,
            "Failed test": failed,
            "Total test": total}
    if config.getoption("--mail") is True:
        receiver = config.option.emailto
        password = config.option.pwd
        sender = config.option.emailfrom
        yagmail_prompt(body, senders, password, receiver)


def gmail_prompt(body, sender, pwd, receiver):
    """Set up the email content and address"""
    server = smtplib.SMTP(smtp)

    msg = MIMEMultipart()
    msg['Subject'] = "This is the test stats of your latest pytest"
    msg['From'] = sender
    msg['To'] = receiver
    msg.attach(MIMEText(body))

    try:
        server.starttls()
        if use_auth:
            server.login(user, pwd)
            server.sendmail(user, receivers, msg.as_string())
        print("Email succeffully")
    except:
        print("Error, can't send email")
