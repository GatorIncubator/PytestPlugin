"""Set up file for pytest plugin"""
#!/usr/bin/env python3

from setuptools import setup


setup(
    name='pytest-plugin-md-email',
    version='0.1.0',
    description='A pytest plugin to send email and produce mard down report',
    url='https://github.com/allegheny-computer-science-203-s2021/PytestPlugin-Team7',
    author='Mai Nguyen, Adriana Solis, Kyrie Doniz, Kevin Lee, Adam Shinomiya',
    author_email='nguyendacm@allegheny.edu, solisa@allegheny.edu, donizk@allegheny.edu, leek3@allegheny.edu, shinomiyaa@allegheny.edu',
    license='MIT',
    py_modules=['plugin'],
    install_requires=['pytest'],
    entry_points={'pytest11': ['pytest-email=pytest_email.plugin'], },
    classifiers=[
        "Framework :: Pytest",
    ],
)
