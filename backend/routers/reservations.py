from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from ..models import Reservation, ReservationCreate, ReservationUpdate
from ..database import get_database, COLLECTIONS
from datetime import datetime

router = APIRouter(prefix="/api/reservations", tags=["reservations"])

@router.post("/", response_model=Reservation)
async def create_reservation(reservation: ReservationCreate, db=Depends(get_database)):
    """Create a new reservation"""
    try:
        new_reservation = Reservation(**reservation.dict())
        await db[COLLECTIONS['reservations']].insert_one(new_reservation.dict())
        return new_reservation
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[Reservation])
async def get_reservations(
    status: Optional[str] = None,
    date: Optional[str] = None,
    limit: int = 100,
    db=Depends(get_database)
):
    """Get all reservations, optionally filtered by status or date"""
    try:
        query = {}
        if status:
            query["status"] = status
        if date:
            query["date"] = date
        
        reservations = await db[COLLECTIONS['reservations']].find(query).limit(limit).to_list(limit)
        return [Reservation(**reservation) for reservation in reservations]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{reservation_id}", response_model=Reservation)
async def get_reservation(reservation_id: str, db=Depends(get_database)):
    """Get a specific reservation by ID"""
    try:
        reservation = await db[COLLECTIONS['reservations']].find_one({"id": reservation_id})
        if not reservation:
            raise HTTPException(status_code=404, detail="Reservation not found")
        return Reservation(**reservation)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{reservation_id}", response_model=Reservation)
async def update_reservation(reservation_id: str, reservation_update: ReservationUpdate, db=Depends(get_database)):
    """Update a reservation status"""
    try:
        update_data = {k: v for k, v in reservation_update.dict().items() if v is not None}
        
        if not update_data:
            raise HTTPException(status_code=400, detail="No fields to update")
        
        result = await db[COLLECTIONS['reservations']].update_one(
            {"id": reservation_id}, 
            {"$set": update_data}
        )
        
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Reservation not found")
        
        updated_reservation = await db[COLLECTIONS['reservations']].find_one({"id": reservation_id})
        return Reservation(**updated_reservation)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{reservation_id}")
async def delete_reservation(reservation_id: str, db=Depends(get_database)):
    """Delete a reservation"""
    try:
        result = await db[COLLECTIONS['reservations']].delete_one({"id": reservation_id})
        
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Reservation not found")
        
        return {"message": "Reservation deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/availability/check")
async def check_availability(date: str, time: str, db=Depends(get_database)):
    """Check table availability for a specific date and time"""
    try:
        # Count existing reservations for the date and time
        existing_reservations = await db[COLLECTIONS['reservations']].count_documents({
            "date": date,
            "time": time,
            "status": {"$in": ["pending", "confirmed"]}
        })
        
        # Assume we have 20 tables max capacity
        max_capacity = 20
        available = existing_reservations < max_capacity
        
        return {
            "available": available,
            "existing_reservations": existing_reservations,
            "max_capacity": max_capacity
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))