from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from ..models import ContactMessage, ContactMessageCreate
from ..database import get_database, COLLECTIONS

router = APIRouter(prefix="/api/contact", tags=["contact"])

@router.post("/", response_model=ContactMessage)
async def submit_contact_message(message: ContactMessageCreate, db=Depends(get_database)):
    """Submit a new contact message"""
    try:
        new_message = ContactMessage(**message.dict())
        await db[COLLECTIONS['contact_messages']].insert_one(new_message.dict())
        return new_message
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[ContactMessage])
async def get_contact_messages(
    status: Optional[str] = None,
    limit: int = 100,
    db=Depends(get_database)
):
    """Get all contact messages, optionally filtered by status"""
    try:
        query = {}
        if status:
            query["status"] = status
        
        messages = await db[COLLECTIONS['contact_messages']].find(query).limit(limit).to_list(limit)
        return [ContactMessage(**message) for message in messages]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{message_id}", response_model=ContactMessage)
async def get_contact_message(message_id: str, db=Depends(get_database)):
    """Get a specific contact message by ID"""
    try:
        message = await db[COLLECTIONS['contact_messages']].find_one({"id": message_id})
        if not message:
            raise HTTPException(status_code=404, detail="Contact message not found")
        return ContactMessage(**message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{message_id}/status")
async def update_message_status(message_id: str, status: str, db=Depends(get_database)):
    """Update contact message status"""
    try:
        valid_statuses = ["new", "read", "replied"]
        if status not in valid_statuses:
            raise HTTPException(status_code=400, detail=f"Status must be one of: {valid_statuses}")
        
        result = await db[COLLECTIONS['contact_messages']].update_one(
            {"id": message_id}, 
            {"$set": {"status": status}}
        )
        
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Contact message not found")
        
        return {"message": "Status updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{message_id}")
async def delete_contact_message(message_id: str, db=Depends(get_database)):
    """Delete a contact message"""
    try:
        result = await db[COLLECTIONS['contact_messages']].delete_one({"id": message_id})
        
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Contact message not found")
        
        return {"message": "Contact message deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))