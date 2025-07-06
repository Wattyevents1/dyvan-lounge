from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from ..models import MenuItem, MenuItemCreate, MenuItemUpdate
from ..database import get_database, COLLECTIONS

router = APIRouter(prefix="/api/menu", tags=["menu"])

@router.get("/", response_model=List[MenuItem])
async def get_menu_items(category: Optional[str] = None, db=Depends(get_database)):
    """Get all menu items, optionally filtered by category"""
    try:
        query = {}
        if category:
            query["category"] = category
        
        menu_items = await db[COLLECTIONS['menu_items']].find(query).to_list(1000)
        return [MenuItem(**item) for item in menu_items]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{item_id}", response_model=MenuItem)
async def get_menu_item(item_id: str, db=Depends(get_database)):
    """Get a specific menu item by ID"""
    try:
        item = await db[COLLECTIONS['menu_items']].find_one({"id": item_id})
        if not item:
            raise HTTPException(status_code=404, detail="Menu item not found")
        return MenuItem(**item)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/", response_model=MenuItem)
async def create_menu_item(item: MenuItemCreate, db=Depends(get_database)):
    """Create a new menu item"""
    try:
        menu_item = MenuItem(**item.dict())
        await db[COLLECTIONS['menu_items']].insert_one(menu_item.dict())
        return menu_item
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{item_id}", response_model=MenuItem)
async def update_menu_item(item_id: str, item_update: MenuItemUpdate, db=Depends(get_database)):
    """Update a menu item"""
    try:
        update_data = {k: v for k, v in item_update.dict().items() if v is not None}
        
        if not update_data:
            raise HTTPException(status_code=400, detail="No fields to update")
        
        result = await db[COLLECTIONS['menu_items']].update_one(
            {"id": item_id}, 
            {"$set": update_data}
        )
        
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Menu item not found")
        
        updated_item = await db[COLLECTIONS['menu_items']].find_one({"id": item_id})
        return MenuItem(**updated_item)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{item_id}")
async def delete_menu_item(item_id: str, db=Depends(get_database)):
    """Delete a menu item"""
    try:
        result = await db[COLLECTIONS['menu_items']].delete_one({"id": item_id})
        
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Menu item not found")
        
        return {"message": "Menu item deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/categories/list")
async def get_menu_categories(db=Depends(get_database)):
    """Get all menu categories"""
    try:
        categories = await db[COLLECTIONS['menu_items']].distinct("category")
        return {"categories": categories}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))