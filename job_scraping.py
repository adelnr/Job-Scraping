import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_titles = []
locations = []
company_names = []
experiences = []
links = []
benefits = []

# Step 1: Enter the StepStone job search URL
stepstone_url = ""

# Step 2: Send a GET request to the StepStone URL
response = requests.get(stepstone_url)
html_content = response.content

# Step 3: Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Step 4: Find relevant HTML elements and extract job details
job_title_elements = soup.find_all("div", class_="resultlist-noiqwp")
location_elements = soup.find_all("div", class_="resultlist-1g9vssc")
company_name_elements = soup.find_all("div", class_="resultlist-1mjyynf")
experience_elements = soup.find_all("div", class_="resultlist-7v4f55")
link_elements = soup.find_all("a", class_="resultlist-1uvdp0v")

# Step 5: Loop through the job elements and extract the details
for i in range(len(job_title_elements)):
    job_titles.append(job_title_elements[i].text.strip())
    locations.append(location_elements[i].text.strip())
    company_names.append(company_name_elements[i].text.strip())
    experiences.append(experience_elements[i].text.strip())
    links.append(link_elements[i].get("href"))

# Step 6: Prepare the data for writing to CSV file
data = [job_titles, locations, company_names, experiences, links, benefits]
export_data = zip_longest(*data)

# Step 7: Enter the file path to save the CSV file
csv_file_path = ""

# Step 8: Write the job details to a CSV file
with open(csv_file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Job Title", "Location", "Company Name", "Experience", "Link", "Benefits"])
    writer.writerows(export_data)
