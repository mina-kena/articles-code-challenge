from lib.db.connection import initialize_database
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed_database():
    
    
    initialize_database()
    
    
    author1 = Author("John Doe").save()
    author2 = Author("Jane Smith").save()
    author3 = Author("Bob Johnson").save()
    
    
    magazine1 = Magazine("Tech Today", "Technology").save()
    magazine2 = Magazine("Science Weekly", "Science").save()
    magazine3 = Magazine("Health & Life", "Health").save()
    
    
    Article("The Future of AI Technology", author1.id, magazine1.id).save()
    Article("Machine Learning Basics", author1.id, magazine1.id).save()
    Article("Climate Change Research", author2.id, magazine2.id).save()
    Article("Quantum Physics Explained", author2.id, magazine2.id).save()
    Article("Healthy Living Tips", author3.id, magazine3.id).save()
    Article("Advanced AI Applications", author2.id, magazine1.id).save()
    
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()