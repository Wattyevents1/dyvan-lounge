from motor.motor_asyncio import AsyncIOMotorClient
import os
from typing import Optional

class Database:
    client: Optional[AsyncIOMotorClient] = None
    database = None

# Database instance
db_instance = Database()

async def get_database() -> AsyncIOMotorClient:
    return db_instance.database

async def connect_to_mongo():
    """Create database connection"""
    mongo_url = os.environ.get('MONGO_URL')
    db_name = os.environ.get('DB_NAME', 'serenity_lodge')
    
    db_instance.client = AsyncIOMotorClient(mongo_url)
    db_instance.database = db_instance.client[db_name]
    print(f"Connected to MongoDB: {db_name}")

async def close_mongo_connection():
    """Close database connection"""
    if db_instance.client:
        db_instance.client.close()
        print("Disconnected from MongoDB")

# Collection names
COLLECTIONS = {
    'menu_items': 'menu_items',
    'cocktails': 'cocktails', 
    'wines': 'wines',
    'reservations': 'reservations',
    'contact_messages': 'contact_messages',
    'gallery_images': 'gallery_images',
    'special_offers': 'special_offers',
    'team_members': 'team_members',
    'testimonials': 'testimonials',
    'status_checks': 'status_checks'
}