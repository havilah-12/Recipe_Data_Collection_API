import json
from database import SessionLocal
from models import Recipe
import math

file_path = r'C:\Users\havil\OneDrive\Desktop\projects\recipes\US_recipes_null.json'


with open(file_path, 'r') as f:
    data = json.load(f)
    print(data)

    db = SessionLocal()
    for item in data.values():
        try:
            recipe = Recipe(
                cuisine=item['cuisine'],
                title=item['title'],
                rating=None if item['rating'] == "NaN" else item['rating'],
                prep_time=None if item['prep_time'] == "NaN" else item['prep_time'],
                cook_time=None if item['cook_time'] == "NaN" else item['cook_time'],
                total_time=None if item['total_time'] == "NaN" else item['total_time'],
                description=item['description'],
                nutrients=item['nutrients'],
                serves=item['serves']
            )
            db.add(recipe)
        except Exception as e:
            print(f"Error adding recipe: {e}")
    db.commit()
    db.close()
