from src.regex_extractor import DataExtractor

def main():
    extractor = DataExtractor()
    sample_text = """
    Contact: john@example.com
    Website: https://www.company.com
    Phone: (123) 456-7890
    Hours: 9:00 AM to 5:00 PM
    Price: $19.99
    """
    
    results = extractor.extract_all(sample_text)
    
    print("Extracted Data:")
    for data_type, values in results.items():
        print(f"{data_type}: {values}")

if __name__ == "__main__":
    main()
