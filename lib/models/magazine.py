from lib.db.connection import get_connection

class Magazine:
    def __init__(self, name, category, id=None):
        self._name = name
        self._category = category
        self._id = id
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value.strip()) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value.strip()
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value.strip()
    
    def save(self):
        
        conn = get_connection()
        cursor = conn.cursor()
        
        try:
            if self._id is None:
                
                cursor.execute(
                    "INSERT INTO magazines (name, category) VALUES (?, ?)",
                    (self._name, self._category)
                )
                self._id = cursor.lastrowid
            else:
                
                cursor.execute(
                    "UPDATE magazines SET name = ?, category = ? WHERE id = ?",
                    (self._name, self._category, self._id)
                )
            conn.commit()
        finally:
            conn.close()
        
        return self
    
    @classmethod
    def find_by_id(cls, magazine_id):
        
        conn = get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT * FROM magazines WHERE id = ?", (magazine_id,))
            row = cursor.fetchone()
            if row:
                return cls(name=row['name'], category=row['category'], id=row['id'])
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
    
    def contributors(self):
        
        conn = get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute, (self._id,)
            return cursor.fetchall()
        finally:
            conn.close()
    
    def article_titles(self):
        
        conn = get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute, (self._id,)
            return [row['title'] for row in cursor.fetchall()]
        finally:
            conn.close()
    
    def contributing_authors(self):
        
        conn = get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute (self._id,)
            return cursor.fetchall()
        finally:
            conn.close()
    
    def __repr__(self):
        return f"<Magazine {self._name}>"