class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if not hasattr(self, '_title'):
            if isinstance(new_title, str) and 5 <= len(new_title) <= 50:
                self._title = new_title
        else:
            print("title must be immutable and between 5 and 50 characters")
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            print("author must be an instance of Author")

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            print("author must be an instance of Magazine")

    def __repr__(self):
        return f"Article {self.author} {self.magazine} {self.title}"

class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not hasattr(self, '_name'):
            if isinstance(new_name, str) and new_name != "":
                self._name = new_name
        else:
            print("must be an immutable string longer than 0 characters")

    def articles(self):
        """Returns list of articles the author has written"""
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        """Returns unique list of magazines the author has contributed to"""
        author_articles = Author.articles(self)
        magazines = [article.magazine for article in author_articles]
        return list(set(magazines))

    def add_article(self, magazine, title):
        """Creates and returns a new Article instance"""
        # self is author instance
        return Article(self, magazine, title)

    def topic_areas(self):
        """Returns unique list of strings with the categories of magazines
        the author has contributed to"""
        author_magazines = Author.magazines(self)
        topics = [magazine.category for magazine in author_magazines]
        if topics:
            return list(set(topics))
        else: 
            return None

    def __repr__(self) -> str:
        return f"<Author {self.name}>"

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
        else:
            print("name is a string that must be between 2 and 16 characters")

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and new_category != '':
            self._category = new_category
        else:
            print("category must be a string longer than 0 characters")

    def articles(self):
        """Returns list of all the articles the magazine has published"""
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        """Returns unique list of authors who have written for this magazine"""
        articles_in_mag = Magazine.articles(self)
        authors = [article.author for article in articles_in_mag]
        return list(set(authors))

    def article_titles(self):
        """Returns list of the title strings of all articles written
        for the magazine, or None if the magazine has no articles"""
        articles = Magazine.articles(self)
        if articles:
            return [article.title for article in articles]
        else:
            return None

    def contributing_authors(self):
        """Returns list of authors who have written 
        more than 2 articles for the magazine, 
        or None if there are no authors with more than 2 articles"""
        articles = Magazine.articles(self)
        authors = Magazine.contributors(self)
        big_contributors = []
        for author in authors:
            count = 0
            for article in articles:
                if author == article.author:
                    count = count + 1
            # print(author, count)
            if count > 2:
                big_contributors.append(author)
        if len(big_contributors) > 0:
            return big_contributors
        else:
            return None

    def __repr__(self):
        return f"<Magazine {self.name} {self.category}>"

a1 = Author("Ernest")
a2 = Author("JK Rowling")

m1 = Magazine("Vogue", "fashion")
m2 = Magazine("ESPN", "sports")
m3 = Magazine("AD", "architecture")

art1 = Article(a1, m1, "Fashion in Milan")
art2 = Article(a1, m2, "Sports Theor")
art3 = Article(a2, m1, "How to Dres")
art4 = Article(a2, m2, "football")
art5 = Article(a1, m1, "How to wear a tutu with style")
# art5 = Article(a1, m1, "How to be single and happy")


# print(Article.all)
# a1.add_article(m1, "FightNight")
# print("~~~~~~~~~~~~~~~")
# print(Article.all)
print(m1.contributing_authors())