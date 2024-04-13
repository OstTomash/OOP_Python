import json

books = [
    {
        'title': 'Function-based static product',
        'author': 'David Brown',
        'isbn': '1-341-39115-9',
        'copies': 94,
    },
    {
        'title': 'Synergized background infrastructure',
        'author': 'Paul Gomez',
        'isbn': '0-511-65220-8',
        'copies': 62,
    },
    {
        'title': 'Business-focused discrete concept',
        'author': 'Edward Deleon',
        'isbn': '0-558-76567-4',
        'copies': 82,
    },
]

with open('mocked_books.json', 'w') as f:
    json.dump(books, f)