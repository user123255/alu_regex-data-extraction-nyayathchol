import unittest
from regex_extractor import DataExtractor

class TestDataExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = DataExtractor()
    
    def test_email_extraction(self):
        text = "Contact: support@company.com and sales@example.org"
        result = self.extractor.extract_emails(text)
        self.assertEqual(result, ['support@company.com', 'sales@example.org'])
    
    def test_url_extraction(self):
        text = "Visit https://www.example.com and http://subdomain.org/page"
        result = self.extractor.extract_urls(text)
        self.assertEqual(result, ['https://www.example.com', 'http://subdomain.org/page'])
    
    def test_phone_extraction(self):
        text = "Call (123) 456-7890 or 123-456-7890"
        result = self.extractor.extract_phone_numbers(text)
        self.assertEqual(result, ['(123) 456-7890', '123-456-7890'])
    
    def test_time_extraction(self):
        text = "Meeting at 14:30 or 2:30 PM"
        result = self.extractor.extract_times(text)
        self.assertEqual(result, ['14:30', '2:30 PM'])
    
    def test_currency_extraction(self):
        text = "Price: $19.99 and $1,234.56"
        result = self.extractor.extract_currency(text)
        self.assertEqual(result, ['$19.99', '$1,234.56'])

if __name__ == '__main__':
    unittest.main()
