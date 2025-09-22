import re

class DataExtractor:
    """
    A class to extract common data types from text using regular expressions.
    Supports emails, URLs, phone numbers, times, hashtags, and currency.
    Each data type has its own extraction method for modular use.
    """
    
    def __init__(self):
        # ---------- REGEX PATTERNS ----------
        
        self.email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
        self.url_pattern = r"https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?"
        self.phone_pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
        self.time_pattern = r"\b(?:[01]?\d|2[0-3]):[0-5]\d\s?(?:[AP]M)?\b"
        self.hashtag_pattern = r"#\w+"
        self.currency_pattern = r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"

    # ---------- INDIVIDUAL EXTRACTION METHODS ----------
    def extract_emails(self, text):
        return re.findall(self.email_pattern, text, flags=re.IGNORECASE)

    def extract_urls(self, text):
        return re.findall(self.url_pattern, text, flags=re.IGNORECASE)

    def extract_phones(self, text):
        return re.findall(self.phone_pattern, text)

    def extract_times(self, text):
        return re.findall(self.time_pattern, text, flags=re.IGNORECASE)

    def extract_hashtags(self, text):
        return re.findall(self.hashtag_pattern, text)

    def extract_currency(self, text):
        return re.findall(self.currency_pattern, text, flags=re.IGNORECASE)

    # ---------- COMBINED EXTRACTION METHOD ----------
    def extract_all(self, text):
        """
        Extract all supported data types from the provided text.
        Returns a dictionary with categories as keys and lists of matches as values.
        """
        return {
            'emails': self.extract_emails(text),
            'urls': self.extract_urls(text),
            'phones': self.extract_phones(text),
            'times': self.extract_times(text),
            'hashtags': self.extract_hashtags(text),
            'currency': self.extract_currency(text)
        }


# ---------- EXAMPLE USAGE ----------
if __name__ == "__main__":
    extractor = DataExtractor()

    # Sample single-word string
    sample_word = "Contact info@example.com for details. Visit https://example.com. Call 123-456-7890 at 2:30 PM. Follow #Python. Price $19.99."

    # Extract and display results
    results = extractor.extract_all(sample_word)
    print("=== Extracted Data ===")
    for category, items in results.items():
        print(f"{category.capitalize()}: {items}")

    # ---------- EDGE CASE TESTING ----------
    edge_case_word = "Invalid email: user@.com. Invalid URL: http://. Invalid phone: 123456. Invalid time: 25:00. Invalid hashtag: #. Invalid currency: $12.345."

    print("\n=== Edge Case Testing ===")
    edge_results = extractor.extract_all(edge_case_word)
    for category, items in edge_results.items():
        print(f"{category.capitalize()}: {items}")

