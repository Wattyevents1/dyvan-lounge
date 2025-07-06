from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from ..models import Cocktail, CocktailCreate, Wine, WineCreate
from ..database import get_database, COLLECTIONS

router = APIRouter(prefix="/api/bar", tags=["bar"])

# Cocktail endpoints
@router.get("/cocktails", response_model=List[Cocktail])
async def get_cocktails(category: Optional[str] = None, db=Depends(get_database)):
    """Get all cocktails, optionally filtered by category"""
    try:
        query = {}
        if category:
            query["category"] = category
        
        cocktails = await db[COLLECTIONS['cocktails']].find(query).to_list(1000)
        return [Cocktail(**cocktail) for cocktail in cocktails]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/cocktails/{cocktail_id}", response_model=Cocktail)
async def get_cocktail(cocktail_id: str, db=Depends(get_database)):
    """Get a specific cocktail by ID"""
    try:
        cocktail = await db[COLLECTIONS['cocktails']].find_one({"id": cocktail_id})
        if not cocktail:
            raise HTTPException(status_code=404, detail="Cocktail not found")
        return Cocktail(**cocktail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/cocktails", response_model=Cocktail)
async def create_cocktail(cocktail: CocktailCreate, db=Depends(get_database)):
    """Create a new cocktail"""
    try:
        new_cocktail = Cocktail(**cocktail.dict())
        await db[COLLECTIONS['cocktails']].insert_one(new_cocktail.dict())
        return new_cocktail
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Wine endpoints
@router.get("/wines", response_model=List[Wine])
async def get_wines(wine_type: Optional[str] = None, db=Depends(get_database)):
    """Get all wines, optionally filtered by type"""
    try:
        query = {}
        if wine_type:
            query["type"] = wine_type
        
        wines = await db[COLLECTIONS['wines']].find(query).to_list(1000)
        return [Wine(**wine) for wine in wines]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/wines/{wine_id}", response_model=Wine)
async def get_wine(wine_id: str, db=Depends(get_database)):
    """Get a specific wine by ID"""
    try:
        wine = await db[COLLECTIONS['wines']].find_one({"id": wine_id})
        if not wine:
            raise HTTPException(status_code=404, detail="Wine not found")
        return Wine(**wine)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/wines", response_model=Wine)
async def create_wine(wine: WineCreate, db=Depends(get_database)):
    """Create a new wine"""
    try:
        new_wine = Wine(**wine.dict())
        await db[COLLECTIONS['wines']].insert_one(new_wine.dict())
        return new_wine
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/categories/cocktails")
async def get_cocktail_categories(db=Depends(get_database)):
    """Get all cocktail categories"""
    try:
        categories = await db[COLLECTIONS['cocktails']].distinct("category")
        return {"categories": categories}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/types/wines")
async def get_wine_types(db=Depends(get_database)):
    """Get all wine types"""
    try:
        types = await db[COLLECTIONS['wines']].distinct("type")
        return {"types": types}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))