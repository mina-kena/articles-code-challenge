from lib.db.connection import get_connection

class Article:
    def __init__(self, title, author_id, magazine_id, id=None):
        self._title = title
        self._author_id = author_id
        self._magazine_id = magazine_id
        self._id = id
    
    @property
    def id(self):
        return self._id
    
    @property
    def title(self):
        return self._title
    
    @property
    def author_id(self):
        return self._author_id
    
    @property
    def magazine_id(self):
        return self._magazine_id
    
    def save(self):
        
        conn = get_connection()
        cursor = conn.cursor()
        
        try:
            if self._id is None:
                
                cursor.execute(
                    "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                    (self._title, self._author_id, self._magazine_id)
                )
                self._id = cursor.lastrowid
            conn.commit()
        finally:
            conn.close()
        
        return self
    
    @classmethod
    def find_by_id(cls, article_id):
       
        conn = get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT * FROM articles WHERE id = ?", (article_id,))
            row = cursor.fetchone()
            if row:
                return cls(title=row['title'], author_id=row['author_id'], 
                          magazine_id=row['magazine_id'], id=row['id'])
            return None
        finally:
            conn.close()
    
    def author(self):
        
        from lib.models.author import Author
        return Author.find_by_id(self._author_id)
    
    def magazine(self):
        
        from lib.models.magazine import Magazine
        return Magazine.find_by_id(self._magazine_id)
    
    def __repr__(self):
        return f"<Article {self._title}>"