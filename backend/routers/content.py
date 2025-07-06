from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ..models import SpecialOffer, SpecialOfferCreate, TeamMember, TeamMemberCreate, Testimonial, TestimonialCreate
from ..database import get_database, COLLECTIONS

router = APIRouter(prefix="/api/content", tags=["content"])

# Special Offers endpoints
@router.get("/special-offers", response_model=List[SpecialOffer])
async def get_special_offers(db=Depends(get_database)):
    """Get all active special offers"""
    try:
        offers = await db[COLLECTIONS['special_offers']].find({"active": True}).to_list(1000)
        return [SpecialOffer(**offer) for offer in offers]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/special-offers", response_model=SpecialOffer)
async def create_special_offer(offer: SpecialOfferCreate, db=Depends(get_database)):
    """Create a new special offer"""
    try:
        new_offer = SpecialOffer(**offer.dict())
        await db[COLLECTIONS['special_offers']].insert_one(new_offer.dict())
        return new_offer
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Team Members endpoints
@router.get("/team", response_model=List[TeamMember])
async def get_team_members(db=Depends(get_database)):
    """Get all active team members"""
    try:
        team = await db[COLLECTIONS['team_members']].find({"active": True}).to_list(1000)
        return [TeamMember(**member) for member in team]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/team", response_model=TeamMember)
async def create_team_member(member: TeamMemberCreate, db=Depends(get_database)):
    """Add a new team member"""
    try:
        new_member = TeamMember(**member.dict())
        await db[COLLECTIONS['team_members']].insert_one(new_member.dict())
        return new_member
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Testimonials endpoints
@router.get("/testimonials", response_model=List[Testimonial])
async def get_testimonials(db=Depends(get_database)):
    """Get all approved testimonials"""
    try:
        testimonials = await db[COLLECTIONS['testimonials']].find({"approved": True}).to_list(1000)
        return [Testimonial(**testimonial) for testimonial in testimonials]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/testimonials", response_model=Testimonial)
async def create_testimonial(testimonial: TestimonialCreate, db=Depends(get_database)):
    """Submit a new testimonial"""
    try:
        new_testimonial = Testimonial(**testimonial.dict())
        await db[COLLECTIONS['testimonials']].insert_one(new_testimonial.dict())
        return new_testimonial
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/testimonials/{testimonial_id}/approve")
async def approve_testimonial(testimonial_id: str, db=Depends(get_database)):
    """Approve a testimonial"""
    try:
        result = await db[COLLECTIONS['testimonials']].update_one(
            {"id": testimonial_id}, 
            {"$set": {"approved": True}}
        )
        
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Testimonial not found")
        
        return {"message": "Testimonial approved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))