from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

# Set base download directory
base_download_dir = os.getcwd()  # Current working directory

years = ["2022","2019", "2017", "2014", "2012", "2009", "2007"]

for year in years:
    # Start driver for year selection
    chrome_options = webdriver.ChromeOptions()
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://ceouttarpradesh.nic.in/rollpdf/form20.aspx")
    time.sleep(3)

    # Select year from dropdown
    year_dropdown = Select(driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_DropDownList2"))
    year_dropdown.select_by_value(year)
    time.sleep(2)

    # Get all district options
    district = Select(driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_DropDownList1"))
    ac_options = district.options[1:]  # Ignore the first default option

    # Store district names & values
    district_data = [[city.text.strip(), city.get_attribute('value')] for city in ac_options]
    
    driver.quit()  # Close driver for year selection

    for district_option in district_data:
        district_name = district_option[0]
        district_value = district_option[1]

        # **Create Year/District Folder**
        download_dir = os.path.join(base_download_dir, year, district_name)
        os.makedirs(download_dir, exist_ok=True)  # Ensure directory exists

        # **Set up Chrome options for custom download location**
        chrome_options = webdriver.ChromeOptions()
        prefs = {
            "download.default_directory": download_dir,  # Set custom download path
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True
        }
        chrome_options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://ceouttarpradesh.nic.in/rollpdf/form20.aspx")
        time.sleep(3)

        # Select district
        district_dropdown = Select(driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_DropDownList2"))
        district_dropdown.select_by_value(year)
        time.sleep(2)

        district = Select(driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_DropDownList1"))
        district.select_by_value(district_value)
        time.sleep(2)

        # Find all "Select" buttons for download
        select_buttons = driver.find_elements(By.XPATH, "//table[@id='ctl00_ContentPlaceHolder1_GridView3']//a[contains(text(),'select')]")

        print(f"Found {len(select_buttons)} download buttons in {district_name} ({year}).")

        # Click each button to download files
        for button in select_buttons:
            try:
                button.click()  # Click to start download
                time.sleep(5)  # Wait for the download to start
                print(f"Downloading: {button.get_attribute('href')} into {download_dir}")
            except Exception as e:
                print(f"Error clicking button: {e}")

        driver.quit()  # Close the driver after downloads
