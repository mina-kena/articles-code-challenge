from lib.db.connection import initialize_database
from lib.db.seed import seed_database
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def main():
    
    print("Initializing database...")
    initialize_database()
    
    print("Seeding database...")
    seed_database()
    
    print("\n=== Testing Authors ===")
    author1 = Author.find_by_name("John Doe")
    print(f"Author: {author1}")
    print(f"Articles by {author1.name}: {len(author1.articles())}")
    print(f"Magazines contributed to: {[m['name'] for m in author1.magazines()]}")
    print(f"Topic areas: {author1.topic_areas()}")
    
    print("\n=== Testing Magazines ===")
    magazine1 = Magazine.find_by_name("Tech Today")
    print(f"Magazine: {magazine1}")
    print(f"Articles in {magazine1.name}: {len(magazine1.articles())}")
    print(f"Contributors: {[c['name'] for c in magazine1.contributors()]}")
    print(f"Article titles: {magazine1.article_titles()}")
    
    print("\n=== Adding New Article ===")
    author1.add_article(magazine1, "New AI Breakthrough Discovery")
    print(f"Updated articles by {author1.name}: {len(author1.articles())}")
    
    print("\nEverything is working! ✅")

if __name__ == "__main__":
    main()