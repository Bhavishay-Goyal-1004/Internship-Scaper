import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time

OUTPUT_FILE = "internship_results.csv"


def fetch_internships(word):

    print("\n==============================")
    print(" Internship Finder Started ")
    print("==============================\n")

    if word:
        skill = word
    else:
        skill = input("Enter skill keyword: ").strip().lower()

    url = (f"https://internshala.com/internships/keywords-{skill}/")

    browser_header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    try:

        print("Connecting to website...\n")

        response = requests.get(
            url,
            headers=browser_header,
            timeout=15
        )

        response.raise_for_status()
        time.sleep(1)

        parsed_html = BeautifulSoup(response.text, "html.parser")

        internship_boxes = parsed_html.find_all("div", {"internshipid": True})

        print(f"Total internships detected: {len(internship_boxes)}\n")

        collected_data = []

        for item in internship_boxes:

            try:

                title_tag = item.find( "a", class_="job-title-href" ) 
                if title_tag: 
                    title = title_tag.text.strip() 
                    job_link = ( "https://internshala.com" + title_tag.get("href") ) 
                else: 
                    title = "N/A" 
                    job_link = "N/A" 
                
                # COMPANY 
                company_tag = item.find( "p", class_="company-name" ) 
                if company_tag: 
                    company = ( company_tag.text.strip() ) 
                else: company = "N/A" 
                
                # LOCATION 
                location_tag = item.find( "div", class_="row-1-item locations" ) 
                if location_tag: 
                    location = ( location_tag.text.strip() ) 
                else: location = "N/A" 
                
                # DATE POSTED 
                date_tag = item.find( "div", class_="status-success" ) 
                if date_tag: 
                    posted_date = ( date_tag.text.strip() ) 
                
                else: posted_date = "Not Available"

                collected_data.append({
                    "Title": title, 
                    "Company": company, 
                    "Location": location, 
                    "Link": job_link, 
                    "Date Posted": posted_date
                })

            except Exception as err:

                print(f"Skipped one entry: {err}")

        if not collected_data:

            print(
                "\nNo matching internships found."
            )

            return

        internship_df = pd.DataFrame(collected_data)

        # Remove duplicates from current scrape
        internship_df.drop_duplicates(inplace=True)

        # Check if CSV already exists
        if pd.io.common.file_exists(OUTPUT_FILE):

            old_df = pd.read_csv(OUTPUT_FILE)

            # Combine old + new data
            internship_df = pd.concat([old_df, internship_df])

            # Remove duplicates again
            internship_df.drop_duplicates(inplace=True)

        # Save updated data
        internship_df.to_csv(
            OUTPUT_FILE,
            index=False
        )

        print("\n==============================")
        print(" Data Saved Successfully ")
        print("==============================")

        print(f"File Name: {OUTPUT_FILE}")

        print(f"Total Saved Records: {len(internship_df)}")

    except requests.exceptions.Timeout:
        print("Connection timed out.")

    except requests.exceptions.ConnectionError:
        print("Unable to connect to internet.")

    except Exception as error:
        print(f"Unexpected Error: {error}")


def automatic_run(word):

    print("\nAuto scraping initiated...\n")


    fetch_internships(word)


print("\n1 --> Start Scraper")
print("2 --> Enable Daily Automation")

user_option = input("\nSelect option: ")

if user_option == "1":
    fetch_internships(None)

elif user_option == "2":

    print("\n================================")
    print(" Daily Automation Enabled ")
    print("================================")

    word = input("Enter skill keyword: ").strip().lower() 
    automatic_run(word)

    print("\nScraper will run every day at 10:00 AM")

    print("Press CTRL + C to stop.")

    schedule.every().day.at("10:00").do(automatic_run,word)
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)

    except KeyboardInterrupt:
        print("\nAutomation stopped by user!\n")

else:
    print("\nInvalid option selected.")
