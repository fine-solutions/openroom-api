"""
Базовые сущности системы
"""
from datetime import datetime
from re import S
from typing import Optional, List
from enum import Enum

from pydantic import BaseModel, Field, EmailStr



class AuthData(BaseModel):
    userID: int
    email: EmailStr
    password: str



class UserExtraPermission(BaseModel):
    permissionID: int
    permissionName: str
    permissionDescription: str



class User(BaseModel):
    userID: int
    userName: str 
    userDescription: Optional[str] = None
    registerAt: datetime
    extraPermissionIDs: List[int]
    adminedRoomIDs: List[int]
    availableRoomIDs: List[int]



class Building(BaseModel):
    '''
    Датакласс для строения
    '''
    buildingID: int
    buildingName: str 
    buildingDescription: Optional[str] = None
    geopointLT: str 
    geopointRB: str
    unitIDs: list[int]
    svg_schema: str 



class Unit(BaseModel):
    '''
    Датакласс корпуса организации
    '''
    unitID: int 
    unitName: str  
    unitDescription: Optional[str] = None 
    floorIDs: list[int]



class Floor(BaseModel):
    '''
    Датакласс помещения
    '''
    floorID: int
    floorName: Optional[str] = None
    floorSequence: int
    roomIDs: list[int]



class Room(BaseModel):
    '''
    Датакласс помещения
    '''
    roomID: int
    romName: Optional[str] = 'Unnamed room'
    roomDescription: Optional[str] = None
    floorID: int



class RoomGroup(BaseModel):
    '''
    Датакласс группы помещений
    '''
    groupID: int 
    groupName: str
    groupDescription: Optional[str] = None 
    creatorID: int 
    public: bool 
    roomIDs: list[int]



class EventStatus(Enum):
    UNCONFIRMED = 0
    CONFIRMED = 1
    REJECTED = 2
    CANCELLED = 3
    FINISHED = 4



class Event(BaseModel):
    eventID: int
    organizerID: int
    roomID: int 
    eventName: str 
    eventDescription: Optional[str] = None 
    startAt: datetime
    endAt: datetime
    freeEntry: bool 
    isClosed: bool 
    status: EventStatus



class EventRegistrationStatus(Enum):
    WAITING = 0
    ACCEPTED = 1
    REJECTED = 2



class EventRegistration(BaseModel):
    eventID: int 
    userID: int 
    status: EventRegistrationStatus



class EventInviteStatus(Enum):
    WAITING = 0
    ACCEPTED = 1
    REJECTED = 2



class EventInvite(BaseModel):
    eventID: int 
    userID: int 
    status: EventInviteStatus
