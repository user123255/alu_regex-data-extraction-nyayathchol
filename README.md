Data Extraction using Python and Regular Expressions
Overview

This project shows how to extract common types of data from text using Python and regular expressions.
It can identify and extract emails, URLs, phone numbers, times, hashtags, and currency from any text.
The code is modular, easy to use, and accurate.

Features

Uses a class-based design with DataExtractor.

Each data type has its own extraction method:

extract_emails()

extract_urls()

extract_phones()

extract_times()

extract_hashtags()

extract_currency()

extract_all() extracts all supported types in one call.

Edge case testing ignores invalid formats, ensuring only correct data is captured.

Data Type	Example Match	Regex Pattern	Notes

Email	info@example.com \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b	Matches valid usernames and domains

URL	https://example.com https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?	Matches http/https links with domain and optional path

Phone	123-456-7890	\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}	Supports (123) 456-7890, 123.456.7890, etc.

Time	2:30 PM, 14:30	`\b(?:[01]?\d	2[0-3]):[0-5]\d\s?(?:[AP]M)?\b`

Hashtag	#Python	#\w+	Matches # followed by letters, numbers, or underscore

Currency	$19.99, $1,234.56	\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?	Matches dollars with commas and two decimal places

How to Use
from data_extractor import DataExtractor

extractor = DataExtractor()

sample_word = "Contact info@example.com for details. Visit https://example.com. Call 123-456-7890 at 2:30 PM. Follow #Python. Price $19.99."

results = extractor.extract_all(sample_word)

for category, items in results.items():
    print(f"{category.capitalize()}: {items}")

Emails: ['info@example.com']
Urls: ['https://example.com']
Phones: ['123-456-7890']
Times: ['2:30 PM']
Hashtags: ['#Python']
Currency: ['$19.99']


edge_case_word = "Invalid email: user@.com. Invalid URL: http://. Invalid phone: 123456. Invalid time: 25:00. Invalid hashtag: #. Invalid currency: $12.345."
edge_results = extractor.extract_all(edge_case_word)

Output:
Emails: []
Urls: []
Phones: []
Times: []
Hashtags: []
Currency: []

Only correctly formatted values are captured. All invalid formats are ignored.
