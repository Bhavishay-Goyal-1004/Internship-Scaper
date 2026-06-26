# Daily Internship Scraper

## Project Overview

Daily Internship Scraper is a Python automation project that scrapes internship listings from Internshala based on a user-provided skill keyword.

The script extracts internship details such as:

* Internship Title
* Company Name
* Location
* Application Link
* Date Posted

and stores the data into a CSV file.

The project also supports daily automation using Python scheduling.

---

# Features

* Scrapes internship listings automatically
* Extracts:

  * Internship Title
  * Company Name
  * Location
  * Application Link
  * Date Posted
* Saves internship data into CSV
* Removes duplicate internship records
* Supports daily automated scraping
* Handles connection and timeout errors
* Uses ethical scraping practices
* Clean and user-friendly terminal output

---

# Project Structure

```text
internship_scraper/
│
├── main.py
├── internship_results.csv
├── requirements.txt
├── README.md
```

---

# Installation

## Clone Repository

```bash
git clone <your-github-repo-link>
```

## Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# Required Libraries

```text
requests
beautifulsoup4
pandas
schedule
```

---

# How to Run

Run the script using:

```bash
python main.py
```

---

# Menu Options

## Option 1 — Start Scraper

Runs the scraper once and stores internship data into CSV.

## Option 2 — Enable Daily Automation

Automatically runs the scraper every day at 10:00 AM.

---
# Output

The script generates a CSV file named:

```text
internship_results.csv
```

Each row contains:

| Column      | Description                       |
| ----------- | --------------------------------- |
| Title       | Internship title                  |
| Company     | Company offering the internship   |
| Location    | Internship location               |
| Link        | Direct internship URL             |
| Date Posted | Posting date shown on Internshala |

Duplicate internships are automatically removed before saving.
---

# Example Terminal Output

```text
1 --> Start Scraper
2 --> Enable Daily Automation

Select option: 1

==============================
 Internship Finder Started 
==============================

Enter skill keyword: Python
Connecting to website...

Total internships detected: 25

Data Saved Successfully
==================================
File Name: internship_results.csv
Total Saved Records: 25
==================================
```

---

# Output CSV Format

| Title | Company | Location | Link | Date Posted |
| ----- | ------- | -------- | ---- | ----------- |

---

# Duplicate Handling

The project automatically:

* Loads existing CSV data
* Merges old and new internship records
* Removes duplicate entries

This prevents repeated internship listings during daily automation runs.

---

# Ethical Scraping Practices

This project follows basic ethical scraping practices:

* Checked robots.txt before scraping
* Added request headers with User-Agent
* Added delay using `time.sleep(1)`
* Avoided excessive requests to the server

---

# Error Handling

The project handles:

* Connection timeout
* Internet connection errors
* Missing internship fields
* Empty internship results

---

# Author

Bhavishay Goyal
