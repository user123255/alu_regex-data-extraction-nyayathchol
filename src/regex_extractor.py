import re
from typing import List, Dict

class DataExtractor:
    def __init__(self):
        self.patterns = {
            'email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            'url': r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\.-]*\/?',
            'phone': r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
            'time': r'(\d{1,2}:\d{2}\s?[AP]M?)|(\d{1,2}:\d{2})',
            'currency': r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
        }
        self.compiled_patterns = {key: re.compile(pattern) for key, pattern in self.patterns.items()}
    
    def extract_emails(self, text: str) -> List[str]:
        return self.compiled_patterns['email'].findall(text)
    
    def extract_urls(self, text: str) -> List[str]:
        return self.compiled_patterns['url'].findall(text)
    
    def extract_phone_numbers(self, text: str) -> List[str]:
        return self.compiled_patterns['phone'].findall(text)
    
    def extract_times(self, text: str) -> List[str]:
        matches = self.compiled_patterns['time'].findall(text)
        return [match for group in matches for match in group if match]
    
    def extract_currency(self, text: str) -> List[str]:
        return self.compiled_patterns['currency'].findall(text)
    
    def extract_all(self, text: str) -> Dict[str, List[str]]:
        return {
            'emails': self.extract_emails(text),
            'urls': self.extract_urls(text),
            'phone_numbers': self.extract_phone_numbers(text),
            'times': self.extract_times(text),
            'currency': self.extract_currency(text)
        }







    


        







































        























