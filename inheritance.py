#library management system
#parent class
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def displayinfo(self):
        return f"Title: {self.title}, Author:{self.author}"
#child class
class libraryBook(Book):
    def __init__(self,title,author,isbn,copies_available):
        super().__init__(title,author)
        self.isbn = isbn
        self.copies_available = copies_available
    def borrowbook(self):
        if self.copies_available>0:
            self.copies_available -= 1
            return f"{self.title} borrowed. Copies is {self.copies_available}"
        else:
            return f"No of Title {self.title} available"

    def returnbook(self):
        self.copies_available += 1
        return f"{self.title} returned. {self.copies_available} available"




