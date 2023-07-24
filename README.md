This script was prepared within the scope of the sample scenario and scenario in QA Hunt Academy.

<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Playwright](https://img.shields.io/badge/playwright-%23242526.svg?style=for-the-badge&logo=playwright&logoColor=%45ba4b)
[![QA HUNT - Academy](https://img.shields.io/badge/QA_HUNT-Academy-blue?style=for-the-badge)](https://)

</div>


# Nobelyayin.com Scraper

This is a simple web scraper that extracts contact information from the [Nobelyayin.com](https://www.nobelyayin.com/kurumsal/) website.

## Usage

The script uses [Playwright](https://playwright.dev/) to launch a Chromium browser, navigate to the Nobelyayin.com website, and extract the following information into an Excel spreadsheet:

- Name
- Role 
- Email
- Duplicate emails (if any)

It outputs the data to a file called `nobelakademi.xlsx`.

The script prints the extracted information to the console as it scrapes. It also warns if any duplicate emails are found for a person.

## Requirements

- Python 3
- Playwright (`pip install pytest-playwright`)
- XlsxWriter (`pip install XlsxWriter`)

## Example Output

The output Excel file will contain a sheet with columns for name, role, email, and duplicate emails.

The console output will show the scraped information, like:

```
Name: John Doe 
Role: Marketing Manager
Email 1: john.doe@nobelprize.org
=========

Name: Jane Doe
Role: Events Coordinator
Email 1: jane.doe@nobelprize.org
Email 2: jane.doe@nobel.se
Warning: Duplicate email found!
=========
```

## Notes

- This is just a simple demo script to showcase web scraping with Playwright and outputting data to Excel.
- The script could be extended to scrape additional data from the site or other similar sites.
- Proper error handling could be added for robustness.
