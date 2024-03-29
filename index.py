# This is the main file to run the script to feed from the csv file to salesforce
import time
from fetcher_bot import FetcherBot
import os

print(f"Current folder: {os.getcwd()}\n")

brain = FetcherBot()
bell_salesForce_url = "https://bellconsent.my.salesforce.com/?ec=302&startURL=%2Fvisualforce%2Fsession%3Furl%3Dhttps%253A%252F%252Fbellconsent.lightning.force.com%252Flightning%252Fn%252FBell"

site_to_be_updated = "TNHLON40_3104A"


# Read environment variables to get credentials
# username = os.getenv("USERNAME")
# password = os.getenv("PASSWORD")

# If environment variables are not set, use hardcoded credentials
username = "alexandre_garcia.azevedo@bell.ca"
password = "Doortodoor20231!"

csv_file_path = "./toFeedSF/update_from_app_to_sf.csv"

site_data = brain.process_csv_to_dict(file_path=csv_file_path)
# print(site_data)


def main():
    """
    Main function to run the bot

    - return: None
    """
    brain.go_to_url(bell_salesForce_url)
    time.sleep(4)
    brain.login(username=username, password=password)
    time.sleep(4)
    login_confirmed = brain.get_login_confirmation()
    if not login_confirmed:
        print("Error: Login confirmation failed")
        pass
    else:
        brain.select_site(site_to_be_updated)
        # loop through site_data and update each site in salesforce
        for data in site_data:
            # address_match = brain.find_matching_address_from_table(data)
            if not brain.find_matching_address_from_table(data):
                pass
        #     else:
        #         brain.switch_to_forms_iframe()
        #         # TODO: check if site is already updated
        #         check = brain.update_site_form_1(data)
        #         if not check:
        #             print('Error: Site not updated, unable to submit form 1')
        #             pass
        #         else:
        #             brain.switch_to_forms_iframe()
        #             # check if form 2 is required
        #             if not brain.check_if_form_2_required():
        #                 print('Form 1 updated successfully')
        #                 pass
        #             else:
        #                 brain.switch_to_second_form_iframe()
        #                 brain.draw_signature()
        # print('All sites updated successfully')

main()
