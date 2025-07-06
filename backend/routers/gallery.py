from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from ..models import GalleryImage, GalleryImageCreate
from ..database import get_database, COLLECTIONS

router = APIRouter(prefix="/api/gallery", tags=["gallery"])

@router.get("/", response_model=List[GalleryImage])
async def get_gallery_images(category: Optional[str] = None, db=Depends(get_database)):
    """Get all gallery images, optionally filtered by category"""
    try:
        query = {}
        if category:
            query["category"] = category
        
        images = await db[COLLECTIONS['gallery_images']].find(query).to_list(1000)
        return [GalleryImage(**image) for image in images]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{image_id}", response_model=GalleryImage)
async def get_gallery_image(image_id: str, db=Depends(get_database)):
    """Get a specific gallery image by ID"""
    try:
        image = await db[COLLECTIONS['gallery_images']].find_one({"id": image_id})
        if not image:
            raise HTTPException(status_code=404, detail="Gallery image not found")
        return GalleryImage(**image)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/", response_model=GalleryImage)
async def create_gallery_image(image: GalleryImageCreate, db=Depends(get_database)):
    """Add a new gallery image"""
    try:
        new_image = GalleryImage(**image.dict())
        await db[COLLECTIONS['gallery_images']].insert_one(new_image.dict())
        return new_image
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{image_id}")
async def delete_gallery_image(image_id: str, db=Depends(get_database)):
    """Delete a gallery image"""
    try:
        result = await db[COLLECTIONS['gallery_images']].delete_one({"id": image_id})
        
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Gallery image not found")
        
        return {"message": "Gallery image deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/categories/list")
async def get_gallery_categories(db=Depends(get_database)):
    """Get all gallery categories"""
    try:
        categories = await db[COLLECTIONS['gallery_images']].distinct("category")
        return {"categories": categories}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))