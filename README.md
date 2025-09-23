Regex Data Extraction Project

Project Overview
This project implements regular expressions to extract 5 specific data types from text strings as part of the Formative One - Regex Onboarding Hackathon assignment. The solution accurately identifies and extracts email addresses, URLs, phone numbers, time formats, and currency amounts from any given text input.

Features Implemented
Data Type	Examples	Pattern Description
Email Addresses	user@example.com, firstname.lastname@company.co.uk	Standard email format with domains
URLs	https://www.example.com, http://subdomain.org/page	HTTP/HTTPS URLs with subdomains and paths
Phone Numbers	(123) 456-7890, 123-456-7890, 123.456.7890	Multiple format support (parentheses, dashes, dots)
Time Formats	14:30 (24-hour), 2:30 PM (12-hour)	Both 12-hour and 24-hour time formats
Currency Amounts	$19.99, $1,234.56	Dollar amounts with commas and decimals

Quick Start
Prerequisites
Python 3.6 or higher
Git

Installation & Setup
Step 1: Clone the Repository
bash
git clone https://github.com/yourusername/alu_regex-data-extraction-YourUsername.git
cd alu_regex-data-extraction-YourUsername
Step 2: Verify Project Structure

text
alu_regex-data-extraction-YourUsername/
├── README.md
├── requirements.txt
├── run.py
└── src/
    ├── __init__.py
    ├── regex_extractor.py
    └── test_extractor.py
    
Step 3: Run the Demo (Quick Test)
bash
python3 run.py
Expected Output:

text
Extracted Data:
emails: ['john@example.com']
urls: ['https://www.company.com']
phone_numbers: ['(123) 456-7890']
times: ['9:00 AM', '5:00 PM']
currency: ['$19.99']

 Usage Guide
Method 1: Using the Demo Script (Easiest)
bash
python3 run.py
Method 2: Importing in Your Code
python
from src.regex_extractor import DataExtractor

# Initialize the extractor
extractor = DataExtractor()

# Sample text to analyze
text = """
Contact us at support@company.com or visit https://www.company.com.
Call (555) 123-4567 between 9:00 AM - 5:00 PM.
Pricing starts at $19.99 per month.
"""

# Extract all data types at once
results = extractor.extract_all(text)

# Access individual results
print("Emails found:", results['emails'])
print("URLs found:", results['urls'])
print("Phone numbers:", results['phone_numbers'])
print("Time formats:", results['times'])
print("Currency amounts:", results['currency'])
Method 3: Individual Extraction Methods
python
from src.regex_extractor import DataExtractor

extractor = DataExtractor()
text = "Email: user@example.com, Phone: (123) 456-7890"

# Extract specific data types
emails = extractor.extract_emails(text)
phones = extractor.extract_phone_numbers(text)
urls = extractor.extract_urls(text)
times = extractor.extract_times(text)
currency = extractor.extract_currency(text)

 Regex Patterns Explained
Email Pattern
regex
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
Matches: Standard email formats with multiple subdomains

Examples: user@example.com, first.last@company.co.uk

URL Pattern
regex
https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\.-]*\/?
Matches: HTTP/HTTPS URLs with paths and parameters

Examples: https://www.example.com, http://api.service.com/v1/endpoint

Phone Number Pattern
regex
\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}
Matches: Multiple phone number formats

Examples: (123) 456-7890, 123-456-7890, 123.456.7890

Time Pattern
regex
(\d{1,2}:\d{2}\s?[AP]M?)|(\d{1,2}:\d{2})
Matches: Both 12-hour and 24-hour formats

Examples: 2:30 PM, 14:30, 09:00 AM

Currency Pattern
regex
\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?
Matches: Dollar amounts with proper formatting

Examples: $19.99, $1,234.56, $1,000,000.00


File Purposes:
regex_extractor.py: Contains the DataExtractor class with all regex patterns

test_extractor.py: Unit tests validating each regex pattern

run.py: Demonstration script with sample usage

requirements.txt: Empty (no external dependencies needed)
