from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize Selenium WebDriver (Chrome)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Runs Chrome in headless mode (no UI)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Go to the webpage with Selenium
url = "https://www.meganslaw.psp.pa.gov/Search/MileRadiusSearch"
driver.get(url)

wait = WebDriverWait(driver, 10)

# Automate filling in the search form
try:
    # Find and click the "Accept" button (targeting the form and the button class)
    accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Accept"]')))
    accept_button.click()

    print("Clicked the Accept button. Now proceeding to the search page...")

    # Use JavaScript to directly set the value of the address input field
    driver.execute_script("document.getElementById('enteredAddr1').value = 'Hamburgh Hall';")

    # Select the city
    city_field = wait.until(EC.visibility_of_element_located((By.ID, 'selectedCity')))
    city_field.send_keys("PITTSBURGH")

    # Input ZIP code
    zip_field = wait.until(EC.visibility_of_element_located((By.ID, 'enteredZip')))
    zip_field.send_keys("15213")

    # Select radius (in miles)
    mile_radius_dropdown = Select(driver.find_element(By.ID, 'MileRadiusDDL'))
    mile_radius_dropdown.select_by_visible_text("3 Miles")

    # Submit the search form (adjust the submit button identifier as needed)
    submit_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, 'MileRadiusSearchResults')))
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)

    # Wait for the results page to load
    time.sleep(5)

    # Now proceed to scrape the result page
    offenders = driver.find_elements(By.CLASS_NAME, 'row.searchResultRow')

    # Initialize a list to store the extracted data
    offender_data = []

    has_next_page = True

    while True:
        time.sleep(5)

        # Scrape the result page
        offenders = driver.find_elements(By.CLASS_NAME, 'row.searchResultRow')

        # Loop through each offender and extract details
        for offender in offenders:
            name = offender.find_element(By.CLASS_NAME, 'searchResultName').text
            tier = offender.find_elements(By.CLASS_NAME, 'gridDataItem.br-responsive-sm')[0].text
            birth_year = offender.find_elements(By.CLASS_NAME, 'gridDataItem.br-responsive-sm')[1].text
            address_block = offender.find_element(By.CLASS_NAME, 'searchResultAddress').text.split("\n")

            # Append the extracted data
            offender_data.append({
                'Name': name,
                'Tier': tier,
                'Birth Year': birth_year,
                'Address': address_block[0],  # Street Address
                'City/State/ZIP': address_block[1]  # City/State/ZIP
            })

        try:
            next_button_li = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'PagedList-skipToNext'))
            )

            # Check if the "Next" button is disabled by looking at its class or missing href
            if "disabled" in next_button_li.get_attribute("class"):
                print("No more pages, 'Next' button is disabled.")
                break  # No more pages, stop the loop

            # Find the anchor tag inside the next button and click it
            next_link = next_button_li.find_element(By.TAG_NAME, 'a')
            next_href = next_link.get_attribute('href')  # Get the URL for the next page

            print(f"Navigating to next page: {next_href}")
            driver.execute_script("arguments[0].click();", next_link)  # Trigger the click via JavaScript

        except Exception as e:
            print("No more pages or error encountered.")
            break  # No more next button, stop the loop

    # Close the browser when done
    driver.quit()

    # Print the extracted data
    if offender_data:
        for data in offender_data:
            print(data)
    else:
        print("No data found.")

except Exception as e:
    print(f"Error during scraping: {e}")
    driver.quit()
