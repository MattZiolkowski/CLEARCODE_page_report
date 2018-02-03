#! python3

'''
Script page_report.py generates a report from a log file. Script counts requests
for each URL, ignoring the protocol, ending slash and query string parameters.
The log file path is read from the command line argument and the string generates report written to
the standard output. Every line of the result follows the CSV format:
'<stripped url>',<requests count>
e.g.:
'www.google.com',1
'''

import re, csv

# Opening command prompt for user to assign log file path  to logFile variable
logFile = open(input("Enter an absolute log file path:\n"))

logData = logFile.read()

# Pattern matching URL.
pattern = re.compile("https?:\/\/[a-zA-Z0-9./]+/?[a-zA-Z0-9]+")

# Searching "today.log" using url regex pattern
search = pattern.findall(logData)

# Creating list for protocol stripped URLs
matchURLs = []

# Stripping URL off the http/https protocol
for match in range(len(search)):
    strippedURL = re.sub(r"https?://", '', search[match], re.IGNORECASE)
    matchURLs.append(strippedURL)
print(matchURLs)

# Counting instances of URL and storing them in dictionary variable "results"
# I.e. creating tally counter in "results" dictionary
results = dict((instance, matchURLs.count(instance)) for instance in set(matchURLs))

# Sorting results in descending order
results = dict(sorted(results.items(), key=lambda kv: kv[1], reverse=True))

# Creating a "report.csv" file in current working directory
reportFile = open("report.csv", "w", newline="")

# Customizing csv writing format
outputReport = csv.writer(reportFile, delimiter=',', quotechar="'",  quoting=csv.QUOTE_NONNUMERIC)

# Writing results into report.csv file, one row at the time (memory efficient)
for k, v in results.items():
    outputReport.writerow([k, v])

# Closing report file
reportFile.close()
