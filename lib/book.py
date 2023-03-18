#!/usr/bin/env python3

class Book:
    
    def __init__(self, title, author="", page_count=0, genre=""):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.genre = genre

    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, page_count):
        if (type(page_count) == int):
            self._page_count = page_count
            print(f"Setting page count to {page_count} for {self.title}")
        else:
            print ("page_count must be an integer")
    
    page_count = property(get_page_count, set_page_count)


    def turn_page(self):
        print("Flipping the page...wow, you read fast!")



huck_finn = Book("Huck Finn", "Mark Twain", 150)
nineteen_eighty_four = Book("1984", "George Orwell", "")
huck_finn.turn_page()