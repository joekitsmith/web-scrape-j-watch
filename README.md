# web-scrape-j-watch
Scraping medical research papers from jwatch.com

# Dependencies
This repo is configured to run on Windows with an installation of Google Chrome browser.

The following dependencies are required:
- python version 3.8
- pipenv

# Setting up
To install python, go to https://www.python.org/downloads/ and follow installation instructions, making sure to add python to PATH.
Once python is installed, open a terminal and type:
`pip install pipenv`

The python environment is installed by opening a terminal from the repository root directory and entering the following command:
`pipenv install`
To open the terminal from the repository root directory, navigate to the directory in Windows File Explorer, type `cmd` in the address bar and hit enter.

# Running the script
Once installation is complete, type the following command to launch the environment:
`pipenv shell`

To run the scraper, use:
`pipenv run scrape`

# Troubleshooting
If the scraper quits unexpectedly, try running it again.
If the problem persists, the delay times for WebDriverWait elements may need to be increased.