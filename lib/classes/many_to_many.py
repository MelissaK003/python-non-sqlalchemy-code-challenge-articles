class Article:
    all_articles = [] #Store all instances of the article variable

    def __init__(self, author, magazine, title): #initializes instances
           #Ensures the title is a string
        if not isinstance(title, str):
            raise TypeError("Invalid Title input")
            #Ensures the length of title is 1-50
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
            #Validates that bothe the author and magazine object have the name attribute
        if not hasattr(author, 'name'):
            raise TypeError("Invalid Author ")
        if not hasattr(magazine, 'name'):
            raise TypeError("Invalid Magazine")
        
        # Assign values to instance variables
        self._author = author
        self._magazine = magazine
        self.__title = title

        #Add article to either author's or magazine list
        if hasattr(author, '_articles'):
            author._articles.append(self)
        if hasattr(magazine, '_articles'):
            magazine._articles.append(self)

         #Append the current instance to the class variable list
        Article.all_articles.append(self)

    # Gets the title,author and Magazine
    @property
    def title(self):
        return self.__title
    
    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine    
    
    @author.setter
    def author(self, value):
        #Validates the author object
        if not hasattr(value, 'name'):
            raise TypeError("Invalid Author ")
        #Assigns new author object    
        self._author = value

    
    @magazine.setter
    def magazine(self, value):
        #Validates the magazine object
        if not hasattr(value, 'name'):
            raise TypeError("Invalid Magazine")
        #Assigns new Magazine object    
        self._magazine = value
       
class Author:
    def __init__(self, name): #initializes instance

        self._articles = [] #Stores a list of articles written by a specific author

        #Ensures the title is a string
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        #Ensures the length of author name is > 0
        if len(name) == 0:
            raise ValueError("Insert a Character")
        
        self.__name = name # Assign a value to instance variable
        
    #Get authors name
    @property
    def name(self):
        return self.__name
    #Retrives articles from a specific author
    def articles(self):
        return [article for article in Article.all_articles if article.author == self]
    #Retrives magazines in which the aouthor has articles in it
    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        existing_articles = [article for article in self._articles if article.title == title and article.magazine == magazine]
        if existing_articles:
            return existing_articles[0]
        
        # Create and return new article
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(magazine.category for magazine in self.magazines()))

class Magazine:
    _all_magazines = []  # Moved outside __init__ as a class variable

    def __init__(self, name, category): #initializes instance
         #Ensures the title is a string
        if not isinstance(name, str):
            raise TypeError("Invalid name input")
        #Ensures the length of name is 2-16   
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be between 2 and 16 characters")
        #Ensures the category input is a string  
        if not isinstance(category, str):
            raise TypeError("Invalid input")
        #Ensures the length of category > 0     
        if len(category) == 0:
            raise ValueError("Insert character")
        
        # Assign a value to instance variable
        self._name = name
        self._category = category
        self._articles = []  # Track articles for this magazine
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        
        if not isinstance(value, str):
            raise TypeError("Invalid Input")
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        
        if not isinstance(value, str):
            raise TypeError("Invalid Input")
        if len(value) == 0:
            raise ValueError("Insert a characters")
        self._category = value

    def articles(self):
        return [article for article in Article.all_articles if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        if not self._articles:
            return None
        authors = {}
        for article in self._articles:
            if article.author not in authors:
                authors[article.author] = 0
            authors[article.author] += 1
        return [author for author, count in authors.items() if count > 2] or None

    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        most_articles_magazine = max(cls._all_magazines, key=lambda magazine: len(magazine._articles), default=None)
        if most_articles_magazine is None or len(most_articles_magazine._articles) == 0:
            return None
        return most_articles_magazine