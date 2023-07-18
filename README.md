This script was prepared within the scope of the sample scenario and scenario in QA Hunt Academy.

# Nobel Prize Scraper

This is a simple web scraper that extracts contact information from the [Nobel Prize](https://www.nobelyayin.com/kurumsal/) website.

## Usage

The script uses [Playwright](https://playwright.dev/) to launch a Chromium browser, navigate to the Nobel Prize website, and extract the following information into an Excel spreadsheet:

- Name
- Role 
- Email
- Duplicate emails (if any)

It outputs the data to a file called `nobelakademi.xlsx`.

The script prints the extracted information to the console as it scrapes. It also warns if any duplicate emails are found for a person.

## Requirements

- Python 3
- Playwright (`pip install playwright`)
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
