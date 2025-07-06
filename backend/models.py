from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid

# Base Models
class StatusCheck(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    client_name: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class StatusCheckCreate(BaseModel):
    client_name: str

# Menu Models
class MenuItem(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    price: float
    category: str  # appetizers, mains, desserts
    image: str
    available: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

class MenuItemCreate(BaseModel):
    name: str
    description: str
    price: float
    category: str
    image: str
    available: bool = True

class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None
    image: Optional[str] = None
    available: Optional[bool] = None

# Cocktail Models
class Cocktail(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    price: float
    image: str
    category: str  # signature, classic
    available: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

class CocktailCreate(BaseModel):
    name: str
    description: str
    price: float
    image: str
    category: str
    available: bool = True

# Wine Models
class Wine(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    price: float
    type: str  # red, white, sparkling
    region: str
    available: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

class WineCreate(BaseModel):
    name: str
    description: str
    price: float
    type: str
    region: str
    available: bool = True

# Reservation Models
class Reservation(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    first_name: str
    last_name: str
    email: str
    phone: str
    date: str
    time: str
    guests: int
    occasion: Optional[str] = None
    special_requests: Optional[str] = None
    status: str = "pending"  # pending, confirmed, cancelled
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ReservationCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    date: str
    time: str
    guests: int
    occasion: Optional[str] = None
    special_requests: Optional[str] = None

class ReservationUpdate(BaseModel):
    status: Optional[str] = None

# Contact Models
class ContactMessage(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: str
    phone: Optional[str] = None
    subject: str
    message: str
    status: str = "new"  # new, read, replied
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ContactMessageCreate(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    subject: str
    message: str

# Gallery Models
class GalleryImage(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    url: str
    title: str
    category: str  # interior, dining, bar, food
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class GalleryImageCreate(BaseModel):
    url: str
    title: str
    category: str
    description: Optional[str] = None

# Special Offer Models
class SpecialOffer(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    time: str
    image: str
    active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

class SpecialOfferCreate(BaseModel):
    title: str
    description: str
    time: str
    image: str
    active: bool = True

# Team Member Models
class TeamMember(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    role: str
    bio: str
    image: str
    active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

class TeamMemberCreate(BaseModel):
    name: str
    role: str
    bio: str
    image: str
    active: bool = True

# Testimonial Models
class Testimonial(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    comment: str
    rating: int
    image: str
    approved: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)

class TestimonialCreate(BaseModel):
    name: str
    comment: str
    rating: int
    image: str