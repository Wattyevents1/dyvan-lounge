from fastapi import APIRouter, HTTPException, Depends
from ..database import get_database, COLLECTIONS
from ..models import (
    MenuItem, Cocktail, Wine, GalleryImage, SpecialOffer, 
    TeamMember, Testimonial
)

router = APIRouter(prefix="/api/seed", tags=["data-seeder"])

@router.post("/all")
async def seed_all_data(db=Depends(get_database)):
    """Seed the database with initial data"""
    try:
        # Clear existing data
        for collection in COLLECTIONS.values():
            await db[collection].delete_many({})
        
        # Seed menu items
        menu_items = [
            # Appetizers
            {
                "id": "1",
                "name": "Truffle Arancini",
                "description": "Crispy risotto balls with truffle oil, parmesan, and herb aioli",
                "price": 16.0,
                "category": "appetizers",
                "image": "https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b",
                "available": True
            },
            {
                "id": "2",
                "name": "Burrata & Prosciutto",
                "description": "Creamy burrata, aged prosciutto, grilled peach, and balsamic reduction",
                "price": 18.0,
                "category": "appetizers",
                "image": "https://images.unsplash.com/photo-1571091655789-405eb7a3a3a8",
                "available": True
            },
            {
                "id": "3",
                "name": "Oysters Rockefeller",
                "description": "Fresh oysters with creamed spinach, herbs, and breadcrumb crust",
                "price": 22.0,
                "category": "appetizers",
                "image": "https://images.unsplash.com/photo-1606731426118-a733c2499b13",
                "available": True
            },
            {
                "id": "4",
                "name": "Charcuterie Board",
                "description": "Selection of artisanal meats, cheeses, nuts, and preserves",
                "price": 24.0,
                "category": "appetizers",
                "image": "https://images.unsplash.com/photo-1504674900247-0877df9cc836",
                "available": True
            },
            # Mains
            {
                "id": "5",
                "name": "Wagyu Beef Tenderloin",
                "description": "8oz prime cut with roasted vegetables and red wine reduction",
                "price": 48.0,
                "category": "mains",
                "image": "https://images.unsplash.com/photo-1546833999-b9f581a1996d",
                "available": True
            },
            {
                "id": "6",
                "name": "Pan-Seared Salmon",
                "description": "Atlantic salmon with quinoa pilaf and lemon butter sauce",
                "price": 32.0,
                "category": "mains",
                "image": "https://images.unsplash.com/photo-1467003909585-2f8a72700288",
                "available": True
            },
            {
                "id": "7",
                "name": "Duck Confit",
                "description": "Slow-cooked duck leg with cherry gastrique and wild rice",
                "price": 36.0,
                "category": "mains",
                "image": "https://images.unsplash.com/photo-1544025162-d76694265947",
                "available": True
            },
            {
                "id": "8",
                "name": "Lobster Risotto",
                "description": "Creamy arborio rice with fresh lobster and microgreens",
                "price": 42.0,
                "category": "mains",
                "image": "https://images.unsplash.com/photo-1611599548918-d1085825c2e8",
                "available": True
            },
            # Desserts
            {
                "id": "9",
                "name": "Chocolate Lava Cake",
                "description": "Warm chocolate cake with molten center and vanilla ice cream",
                "price": 12.0,
                "category": "desserts",
                "image": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c",
                "available": True
            },
            {
                "id": "10",
                "name": "Crème Brûlée",
                "description": "Classic vanilla custard with caramelized sugar crust",
                "price": 10.0,
                "category": "desserts",
                "image": "https://images.unsplash.com/photo-1470124182917-cc6e71b22ecc",
                "available": True
            },
            {
                "id": "11",
                "name": "Tiramisu",
                "description": "Traditional Italian dessert with espresso and mascarpone",
                "price": 11.0,
                "category": "desserts",
                "image": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9",
                "available": True
            }
        ]
        
        # Seed cocktails
        cocktails = [
            {
                "id": "1",
                "name": "Serenity Sunset",
                "description": "Bourbon, peach liqueur, honey, lemon, and fresh thyme",
                "price": 16.0,
                "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b",
                "category": "signature",
                "available": True
            },
            {
                "id": "2",
                "name": "Mountain Mist",
                "description": "Gin, elderflower, cucumber, lime, and rosemary smoke",
                "price": 15.0,
                "image": "https://images.unsplash.com/photo-1551538827-9c037cb4f32a",
                "category": "signature",
                "available": True
            },
            {
                "id": "3",
                "name": "Lodge Old Fashioned",
                "description": "Rye whiskey, maple syrup, orange bitters, and smoked cherry",
                "price": 18.0,
                "image": "https://images.unsplash.com/photo-1470337458703-46ad1756a187",
                "category": "signature",
                "available": True
            },
            {
                "id": "4",
                "name": "Classic Martini",
                "description": "Premium vodka or gin, dry vermouth, olive or lemon twist",
                "price": 14.0,
                "image": "https://images.unsplash.com/photo-1541746972996-4e0b0f93e586",
                "category": "classic",
                "available": True
            },
            {
                "id": "5",
                "name": "Negroni",
                "description": "Gin, Campari, sweet vermouth, orange peel",
                "price": 13.0,
                "image": "https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd",
                "category": "classic",
                "available": True
            },
            {
                "id": "6",
                "name": "Whiskey Sour",
                "description": "Bourbon, lemon juice, simple syrup, egg white",
                "price": 12.0,
                "image": "https://images.unsplash.com/photo-1560512823-829485b8bf24",
                "category": "classic",
                "available": True
            }
        ]
        
        # Seed wines
        wines = [
            {
                "id": "1",
                "name": "Château Margaux 2015",
                "description": "Bordeaux red wine with notes of blackberry and cedar",
                "price": 85.0,
                "type": "red",
                "region": "Bordeaux, France",
                "available": True
            },
            {
                "id": "2",
                "name": "Chablis Premier Cru",
                "description": "Crisp white wine with mineral notes and citrus finish",
                "price": 45.0,
                "type": "white",
                "region": "Burgundy, France",
                "available": True
            },
            {
                "id": "3",
                "name": "Caymus Napa Valley Cabernet",
                "description": "Full-bodied red with dark fruit flavors and smooth tannins",
                "price": 68.0,
                "type": "red",
                "region": "Napa Valley, CA",
                "available": True
            },
            {
                "id": "4",
                "name": "Dom Pérignon 2012",
                "description": "Prestigious champagne with fine bubbles and complex flavors",
                "price": 280.0,
                "type": "sparkling",
                "region": "Champagne, France",
                "available": True
            }
        ]
        
        # Seed gallery images
        gallery_images = [
            {
                "id": "1",
                "url": "https://images.unsplash.com/photo-1580719996124-1b5c300d251a",
                "category": "interior",
                "title": "Lounge Interior"
            },
            {
                "id": "2",
                "url": "https://images.unsplash.com/photo-1700874897288-27ae7ab28ee7",
                "category": "dining",
                "title": "Dining Experience"
            },
            {
                "id": "3",
                "url": "https://images.pexels.com/photos/29046927/pexels-photo-29046927.jpeg",
                "category": "interior",
                "title": "Elegant Seating"
            },
            {
                "id": "4",
                "url": "https://images.pexels.com/photos/18866153/pexels-photo-18866153.jpeg",
                "category": "dining",
                "title": "Fine Dining"
            },
            {
                "id": "5",
                "url": "https://images.pexels.com/photos/7476832/pexels-photo-7476832.jpeg",
                "category": "bar",
                "title": "Bar Area"
            },
            {
                "id": "6",
                "url": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b",
                "category": "bar",
                "title": "Craft Cocktails"
            },
            {
                "id": "7",
                "url": "https://images.unsplash.com/photo-1551538827-9c037cb4f32a",
                "category": "bar",
                "title": "Signature Drinks"
            },
            {
                "id": "8",
                "url": "https://images.unsplash.com/photo-1544025162-d76694265947",
                "category": "food",
                "title": "Gourmet Cuisine"
            }
        ]
        
        # Seed special offers
        special_offers = [
            {
                "id": "1",
                "title": "Happy Hour Special",
                "description": "50% off all cocktails and appetizers",
                "time": "Monday - Friday, 5:00 PM - 7:00 PM",
                "image": "https://images.unsplash.com/photo-1551538827-9c037cb4f32a",
                "active": True
            },
            {
                "id": "2",
                "title": "Wine Wednesday",
                "description": "30% off all wines by the bottle",
                "time": "Every Wednesday, All Day",
                "image": "https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb",
                "active": True
            },
            {
                "id": "3",
                "title": "Weekend Brunch",
                "description": "Special brunch menu with bottomless mimosas",
                "time": "Saturday & Sunday, 10:00 AM - 3:00 PM",
                "image": "https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b",
                "active": True
            }
        ]
        
        # Seed team members
        team_members = [
            {
                "id": "1",
                "name": "James Mitchell",
                "role": "Executive Chef",
                "image": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e",
                "bio": "With over 15 years of culinary experience, James brings innovative flavors to every dish.",
                "active": True
            },
            {
                "id": "2",
                "name": "Sarah Johnson",
                "role": "Head Bartender",
                "image": "https://images.unsplash.com/photo-1494790108755-2616b612b786",
                "bio": "Sarah crafts our signature cocktails with passion and precision, creating memorable experiences.",
                "active": True
            },
            {
                "id": "3",
                "name": "Michael Chen",
                "role": "General Manager",
                "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d",
                "bio": "Michael ensures every guest receives exceptional service and attention to detail.",
                "active": True
            }
        ]
        
        # Seed testimonials
        testimonials = [
            {
                "id": "1",
                "name": "Emily Rodriguez",
                "rating": 5,
                "comment": "Absolutely incredible experience! The ambiance is perfect and the food is outstanding.",
                "image": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80",
                "approved": True
            },
            {
                "id": "2",
                "name": "David Thompson",
                "rating": 5,
                "comment": "Best cocktails in town! The staff really knows their craft. Highly recommend.",
                "image": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e",
                "approved": True
            },
            {
                "id": "3",
                "name": "Lisa Wang",
                "rating": 5,
                "comment": "Perfect for date night. The atmosphere is romantic and the service is impeccable.",
                "image": "https://images.unsplash.com/photo-1494790108755-2616b612b786",
                "approved": True
            }
        ]
        
        # Insert all data
        await db[COLLECTIONS['menu_items']].insert_many(menu_items)
        await db[COLLECTIONS['cocktails']].insert_many(cocktails)
        await db[COLLECTIONS['wines']].insert_many(wines)
        await db[COLLECTIONS['gallery_images']].insert_many(gallery_images)
        await db[COLLECTIONS['special_offers']].insert_many(special_offers)
        await db[COLLECTIONS['team_members']].insert_many(team_members)
        await db[COLLECTIONS['testimonials']].insert_many(testimonials)
        
        return {
            "message": "Database seeded successfully",
            "data": {
                "menu_items": len(menu_items),
                "cocktails": len(cocktails),
                "wines": len(wines),
                "gallery_images": len(gallery_images),
                "special_offers": len(special_offers),
                "team_members": len(team_members),
                "testimonials": len(testimonials)
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/all")
async def clear_all_data(db=Depends(get_database)):
    """Clear all data from the database"""
    try:
        for collection in COLLECTIONS.values():
            await db[collection].delete_many({})
        
        return {"message": "All data cleared successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))