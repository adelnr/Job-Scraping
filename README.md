# Job Scraping

This Python script scrapes job information from the StepStone website (https://www.stepstone.de/) and saves it to a CSV file.
The code can be modified to scrape job information from any website, not just StepStone. By changing the website_url variable to the desired website URL, you can scrape job details from that specific website.

## Requirements

To run this script, you need to have the following dependencies installed:

- Python 3.x
- requests (`pip install requests`)
- BeautifulSoup (`pip install beautifulsoup4`)

## Usage

1. Run the `job_scraping.py` script.

2. The script will scrape job information from the StepStone website based on the provided URL.

3. It will extract job titles, locations, company names, experience requirements, and links from the webpage.

4. The scraped data will be saved in a CSV file named `newfile.csv`.

5. You can modify the `stepstone` URL variable in the script to scrape different job listings or customize the scraping logic as per your requirements.

## Contributing

Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
