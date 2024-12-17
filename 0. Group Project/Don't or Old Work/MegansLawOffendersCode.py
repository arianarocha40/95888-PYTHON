# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:30:38 2024

@author: arian
"""
############ import / read ###############

import requests
from bs4 import BeautifulSoup

#URL being scraped
url = 'https://www.meganslaw.psp.pa.gov/Search/MileRadiusSearchResultsAsync?enteredAddr1=Hamburgh+Hall&enteredAddr2=Forbes+Avenue&selectedCity=PITTSBURGH&enteredState=PA&enteredZip=15213&selectedMileRadius=3&chkMileRadiusIncarcerated=false&GrecaptchaToken=03AFcWeA5EBIRLODReldUJGkz0bk1dhUvRlRxDgfUyJ8gEJWRIY4IBhFLsJG-e22HoCO2Jx7j2iep0AP2hkOFw1fHaQe9-_AkAj5FbXGNBNSjgcMzgj2JdBMGKOjEjMwtzZ7OYzT1u1m3a-8mdG-z_WGwy47EnTvaCnjVC4OpsKwGYZLnvJWB9wn_5z2yc1CU8BDcFOZtKFN7hsHfrw86TtNoFYpTAtxHlzT9yXYy7p4HMwbHqlfUUnTXyPH21x5xlq54hT0RkowNbPWoGs_sftmfANhVWKRWZgDX_cNMZi45pC7mbKhySTDy5Ydi1JHjLi1Vyf4SFONo-FWUfTc888pwm1NyN5zDfrIMtH79NGb9amENL97DP6e1iG3CyEDxbOLMNV497y9EoFzgcCLibOQp-j24_lktCCrfh4ONApUgaCPmHcVq9aphXAN6RE9phBuKaJxlA1u1muwwJhdxqlr5CiFWffuuvB32EKgyIkp6eI2uHLKVJynFyiG-A1ZRkA7-kKbFbriP8xVTkfv25N6gu44bEISTCSO10arIbOc17PXO9iBV4qrZtdcbZ195s4Qp0kmbUUz--L98ZgmYAsgHXyGQQA62m3N4qCQH5oHDmGYruEBkt4Iu0Zwze0zk5hP4dHl0LzG7a_VByHzDqfgzZbBtAjdGeiN9r2bYtSPyJiV3OrbEy5eXXEbdPb8NhAYtR0KFzkobJceNrwWtacqv_W4Omfy1VSebwy0FAdH4fLfLzkT9kuso6BMp_nB9S9osS_KAlCOH_S854t47604fuu_BjgJ4QDrp6WgvL-RlOF8VoROtgqo2fPDe6N2yGC5SDspb1oE98Kida9IdJbDAaQKa3sIA-hj3Bv4GbGr6UW6Su5_QWJCA'

#Requesting page content
response = requests.get(url)

#Request checking
if response.status_code == 200:
    print("Successfully retrieved the webpage for Megans Law Offenders")
    #Parsing HTML content with BS
    soup = BeautifulSoup(response.content, 'html.parser')
else: 
    print("Failed to retrieve webpage")
    
############### WORK #####################

# Assuming offender details are in 'div' tags with specific classes (you may need to adjust these based on the page structure)
offenders = soup.find_all('div', class_='row SearchResultsRow')  # Adjust the class name based on inspection

# Initialize an empty list to store extracted data
offender_data = []

# Loop through each offender and extract details
for offender in offenders:
    # Extract the offender's name
    name = offender.find('div', class_='searchResultName').get_text(strip=True)  # Adjust tag and class as needed
        #<p class="searchResultName">ABDI, MOHAMED HUSSEIN</p>


    # Extract the offender's address
    address = offender.find('p', class_='gridTxtLbl').get_text(strip=True)  # Adjust tag and class as needed
    
    # Print extracted information (for testing)
    print(f"Name: {name}")
    print(f"Address: {address}")
    
    # Append extracted data to the list
    offender_data.append({'Name': name, 'Address': address})

# Check if data was collected
if offender_data:
    print("\nData extraction complete!")
else:
    print("\nNo data found; please check the tags and classes.")