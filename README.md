# page_report.py

Script page_report.py generates a report from a log file. Script counts requests
for each URL, ignoring the protocol, ending slash and query string parameters.
The log file path is read from the command line argument and the string generates report written to
the standard output. Every line of the result follows the CSV format:
'<stripped url>',<requests count>
e.g.:
'www.google.com',1

# Getting Started

Download a file from my GitHub account. Make sure you have Python3+ installed. If you use Windows you are able to
run the program in a command prompt.

# Prerequisites

You will need a Python 3 and above installed on your computer and Windows to run program through command prompt.

# Installing

Save the files on your PC. Make sure you have Python 3 and above installed. For guidence on installation of Python
visit www.python.org.

# Deployment

You can run hack_power.py file through IDLE (PythonShell),
Windows command prompt or with other Pythonic environment (e.g. PyCharm).

# Built With

Python 3.6.1
-using 're' and 'csv' frameworks (regex)
-PyCharm

# Authors

Mateusz Ziolkowski

# License

This project is licensed under the MIT License - see the LICENSE.md file for details

# Acknowledgments

Thanks to Clearcode for setting up this assignment- was quite fun.
