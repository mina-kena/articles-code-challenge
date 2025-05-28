from lib.db.connection import get_connection

class Author:
    def __init__(self, name, id=None):
        self._name = name
        self._id = id
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value.strip()
    
    def save(self):
        
        conn = get_connection()
        cursor = conn.cursor()
        
        try:
            if self._id is None:
                
                cursor.execute(
                    "INSERT INTO authors (name) VALUES (?)",
                    (self._name,)
                )
                self._id = cursor.lastrowid
            else:
                
                cursor.execute(
                    "UPDATE authors SET name = ? WHERE id = ?",
                    (self._name, self._id)
                )
            conn.commit()
        finally:
            conn.close()
        
        return self
    
    @classmethod
    def find_by_id(cls, author_id):
       
        conn = get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
            row = cursor.fetchone()
            if row:
                return cls(name=row['name'], id=row['id'])
            return None
        finally:
            conn.close()
    
    @classmethod
    def find_by_name(cls, name):

        conn = get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT * FROM authors WHERE name = ?", (name,))
            row = cursor.fetchone()
            if row:
                return cls(name=row['name'], id=row['id'])
            return None
        finally:
            conn.close()
    
    def articles(self):
       
        conn = get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute, (self._id,)
            return cursor.fetchall()
        finally:
            conn.close()
    
    def magazines(self):
        
        conn = get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute, (self._id,)
            return cursor.fetchall()
        finally:
            conn.close()
    
    def add_article(self, magazine, title):
        
        from lib.models.article import Article
        
        if not isinstance(title, str) or len(title.strip()) == 0:
            raise ValueError("Title must be a non-empty string")
        
        
        if magazine.id is None:
            magazine.save()
        
        
        if self._id is None:
            self.save()
        
        article = Article(title=title.strip(), author_id=self._id, magazine_id=magazine.id)
        return article.save()
    
    def topic_areas(self):
       
        conn = get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute, (self._id,)
            return [row['category'] for row in cursor.fetchall()]
        finally:
            conn.close()
    
    def __repr__(self):
        return f"<Author {self._name}>"