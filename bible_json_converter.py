import json

# Mapping of book abbreviations to full names and book numbers
book_mapping = {
    "Gen": {"name": "Genesis", "number": 1},
    "Exo": {"name": "Exodus", "number": 2},
    "Lev": {"name": "Leviticus", "number": 3},
    "Num": {"name": "Numbers", "number": 4},
    "Deut": {"name": "Deuteronomy", "number": 5},
    "Josh": {"name": "Joshua", "number": 6},
    "Judg": {"name": "Judges", "number": 7},
    "Ruth": {"name": "Ruth", "number": 8},
    "1Sam": {"name": "1 Samuel", "number": 9},
    "2Sam": {"name": "2 Samuel", "number": 10},
    "1Kgs": {"name": "1 Kings", "number": 11},
    "2Kgs": {"name": "2 Kings", "number": 12},
    "1Chr": {"name": "1 Chronicles", "number": 13},
    "2Chr": {"name": "2 Chronicles", "number": 14},
    "Ezra": {"name": "Ezra", "number": 15},
    "Neh": {"name": "Nehemiah", "number": 16},
    "Esth": {"name": "Esther", "number": 17},
    "Job": {"name": "Job", "number": 18},
    "Ps": {"name": "Psalms", "number": 19},
    "Prov": {"name": "Proverbs", "number": 20},
    "Eccl": {"name": "Ecclesiastes", "number": 21},
    "Song": {"name": "Song of Solomon", "number": 22},
    "Isa": {"name": "Isaiah", "number": 23},
    "Jer": {"name": "Jeremiah", "number": 24},
    "Lam": {"name": "Lamentations", "number": 25},
    "Ezek": {"name": "Ezekiel", "number": 26},
    "Dan": {"name": "Daniel", "number": 27},
    "Hos": {"name": "Hosea", "number": 28},
    "Joel": {"name": "Joel", "number": 29},
    "Amos": {"name": "Amos", "number": 30},
    "Obad": {"name": "Obadiah", "number": 31},
    "Jonah": {"name": "Jonah", "number": 32},
    "Mic": {"name": "Micah", "number": 33},
    "Nah": {"name": "Nahum", "number": 34},
    "Hab": {"name": "Habakkuk", "number": 35},
    "Zeph": {"name": "Zephaniah", "number": 36},
    "Hag": {"name": "Haggai", "number": 37},
    "Zech": {"name": "Zechariah", "number": 38},
    "Mal": {"name": "Malachi", "number": 39},
    "Matt": {"name": "Matthew", "number": 40},
    "Mark": {"name": "Mark", "number": 41},
    "Luke": {"name": "Luke", "number": 42},
    "John": {"name": "John", "number": 43},
    "Acts": {"name": "Acts", "number": 44},
    "Rom": {"name": "Romans", "number": 45},
    "1Cor": {"name": "1 Corinthians", "number": 46},
    "2Cor": {"name": "2 Corinthians", "number": 47},
    "Gal": {"name": "Galatians", "number": 48},
    "Eph": {"name": "Ephesians", "number": 49},
    "Phil": {"name": "Philippians", "number": 50},
    "Col": {"name": "Colossians", "number": 51},
    "1Thess": {"name": "1 Thessalonians", "number": 52},
    "2Thess": {"name": "2 Thessalonians", "number": 53},
    "1Tim": {"name": "1 Timothy", "number": 54},
    "2Tim": {"name": "2 Timothy", "number": 55},
    "Titus": {"name": "Titus", "number": 56},
    "Philem": {"name": "Philemon", "number": 57},
    "Heb": {"name": "Hebrews", "number": 58},
    "James": {"name": "James", "number": 59},
    "1Pet": {"name": "1 Peter", "number": 60},
    "2Pet": {"name": "2 Peter", "number": 61},
    "1John": {"name": "1 John", "number": 62},
    "2John": {"name": "2 John", "number": 63},
    "3John": {"name": "3 John", "number": 64},
    "Jude": {"name": "Jude", "number": 65},
    "Rev": {"name": "Revelation", "number": 66}
}

# Load the NKJV JSON file
with open('NKJV.bible.json', 'r') as file:
    nkjv_bible = json.load(file)

# Initialize an empty list to hold the formatted verses
formatted_verses = []

# Process each book
for book in nkjv_bible['books']:
    book_name = book['name']
    book_abbr = next((abbr for abbr, details in book_mapping.items() if details['name'] == book_name), None)
    if not book_abbr:
        continue
    
    book_number = book_mapping[book_abbr]['number']
    
    # Process each chapter
    for chapter in book['chapters']:
        chapter_number = chapter['num']
        
        # Process each verse
        for verse in chapter['verses']:
            verse_number = verse['num']
            verse_text = verse['text']
            
            formatted_verse = {
                "book_name": book_name,
                "book": book_number,
                "chapter": chapter_number,
                "verse": verse_number,
                "text": verse_text
            }
            
            formatted_verses.append(formatted_verse)

# Save the formatted verses to a new JSON file
with open('NKJV_formatted.json', 'w') as outfile:
    json.dump(formatted_verses, outfile, indent=4)

print("Conversion complete. Formatted JSON saved as 'NKJV_formatted.json'.")
