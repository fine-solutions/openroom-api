from datetime import datetime

from sqlalchemy import ReleaseSavepointClause, String, ForeignKey, Integer, Enum
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs



class Base(AsyncAttrs, DeclarativeBase):
    pass 



class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str|None] = mapped_column(String(1000))
    create_at: Mapped[datetime]

    auth_data: Mapped["AuthData"] = relationship(
        "AuthData",
        back_populates="user"
    )
    
    permission_ids: Mapped[list["UserPermission"]] = relationship(
        "UserPermission",
        back_populates="user"
    )

    created_user_groups: Mapped[list["UserGroup"]] = relationship(
        "UserGroup",
        back_populates="creator"
    )

    group_ids: Mapped[list["UserInGroup"]] = relationship(
        "UserInGroup",
        back_populates="user"
    )

    created_room_groups: Mapped[list["RoomGroup"]] = relationship(
        "RoomGroup",
        back_populates="creator"
    )

    available_room_ids: Mapped[list["AvailableRoom"]] = relationship(
        "AvailableRoom",
        back_populates="user"
    )

    admined_room_ids: Mapped[list["AdminedRoom"]] = relationship(
        "AdminedRoom",
        back_populates="user"
    )

    organized_events: Mapped[list["Event"]] = relationship(
        "Event",
        back_populates="organizer"
    )

    invites: Mapped[list["Invite"]] = relationship(
        "Invite",
        back_populates="user"
    )

    registrations: Mapped[list["Registration"]] = relationship(
        "Registration",
        back_populates="user"
    )



class Permission(Base):
    __tablename__ = "permission"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]

    user_ids: Mapped[list["UserPermission"]] = relationship(
        "UserPermission",
        back_populates="permission"
    )



class UserPermission(Base):
    __tablename__ = "user_permission"

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    permission_id: Mapped[int] = mapped_column(ForeignKey("permission.id"), primary_key=True)

    user: Mapped["User"] = relationship(
        "User",
        back_populates="permission_ids"
    )

    permission: Mapped["Permission"] = relationship(
        "Permission",
        back_populates="user_ids"
    )



class AuthData(Base):
    __tablename__ = "auth_data"

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    email: Mapped[str]
    password: Mapped[str]

    user: Mapped["User"] = relationship(
        "User",
        back_populates="auth_data"
    )



class UserGroup(Base):
    __tablename__ = "user_group"

    id: Mapped[int] = mapped_column(primary_key=True)
    creator_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(1000))
    public: Mapped[bool]

    creator: Mapped["User"] = relationship(
        "User",
        back_populates="created_user_groups"
    )

    user_ids: Mapped[list["UserInGroup"]] = relationship(
        "UserInGroup",
        back_populates="group"
    )



class UserInGroup(Base):
    __tablename__ = "user_in_group"

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("user_group.id"), primary_key=True)

    group: Mapped["UserGroup"] = relationship(
        "UserGroup",
        back_populates="user_ids"
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="group_ids"
    )



class Unit(Base):
    __tablename__ = "unit"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(1000))

    floors: Mapped[list["Floor"]] = relationship(
        "Floor",
        back_populates="unit"
    )



class Floor(Base):
    __tablename__ = "floor"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    sequence: Mapped[int]
    unit_id: Mapped[int] = mapped_column(ForeignKey("unit.id"))

    unit: Mapped["Unit"] = relationship(
        "Unit",
        back_populates="floors"
    )

    rooms: Mapped[list["Room"]] = relationship(
        "Room",
        back_populates="floor"
    )



class Room(Base):
    __tablename__ = "room"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(1000))
    floor_id: Mapped[int] = mapped_column(ForeignKey("floor.id"))

    floor: Mapped["Floor"] = relationship(
        "Floor",
        back_populates="rooms"
    )

    group_ids: Mapped[list["RoomInGroup"]] = relationship(
        "RoomInGroup",
        back_populates="room"
    )

    organizers: Mapped[list["AvailableRoom"]] = relationship(
        "AvailableRoom",
        back_populates="room"
    )

    admins: Mapped[list["AdminedRoom"]] = relationship(
        "AdminedRoom",
        back_populates="room"
    )

    events: Mapped[list["Event"]] = relationship(
        "Event",
        back_populates="room"
    )



class RoomGroup(Base):
    __tablename__ = "room_group"

    id: Mapped[int] = mapped_column(primary_key=True)
    creator_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(1000))
    public: Mapped[bool]

    creator: Mapped["User"] = relationship(
        "User",
        back_populates="created_room_groups"
    )

    room_ids: Mapped[list["RoomInGroup"]] = relationship(
        "RoomInGroup",
        back_populates="group"
    )



class RoomInGroup(Base):
    __tablename__ = "room_in_group"

    room_id: Mapped[int] = mapped_column(ForeignKey("room.id"), primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("room_group.id"), primary_key=True)

    room: Mapped["Room"] = relationship(
        "Room",
        back_populates="group_ids"
    )

    group: Mapped["RoomGroup"] = relationship(
        "RoomGroup",
        back_populates="room_ids"
    )



class AvailableRoom(Base):
    __tablename__ = "available_room"

    room_id: Mapped[int] = mapped_column(ForeignKey("room.id"), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    autoconfirm: Mapped[bool]

    user: Mapped["User"] = relationship(
        "User",
        back_populates="available_room_ids"
    )

    room: Mapped["Room"] = relationship(
        "Room",
        back_populates="organizers"
    )



class AdminedRoom(Base):
    __tablename__ = "admined_room"

    room_id: Mapped[int] = mapped_column(ForeignKey("room.id"), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)

    user: Mapped["User"] = relationship(
        "User",
        back_populates="admined_room_ids"
    )

    room: Mapped["Room"] = relationship(
        "Room",
        back_populates="admins"
    )



class Event(Base):
    __tablename__ = "event"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("room.id"))
    organizer_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(1000))
    starts_at: Mapped[datetime]
    ends_at: Mapped[datetime]
    free_entry: Mapped[bool]
    is_closed: Mapped[bool]
    status: Mapped[str]

    organizer: Mapped["User"] = relationship(
        "User",
        back_populates="organized_events"
    )

    room: Mapped["Room"] = relationship(
        "Room",
        back_populates="events"
    )

    invites: Mapped[list["Invite"]] = relationship(
        "Invite",
        back_populates="event"
    )

    registrations: Mapped[list["Registration"]] = relationship(
        "Registration",
        back_populates="event"
    )



class Invite(Base):
    __tablename__ = "invite"

    event_id: Mapped[int] = mapped_column(ForeignKey("event.id"), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    status: Mapped[str]

    event: Mapped["Event"] = relationship(
        "Event",
        back_populates="invites"
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="invites"
    )



class Registration(Base):
    __tablename__ = "registration"

    event_id: Mapped[int] = mapped_column(ForeignKey("event.id"), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    status: Mapped[str]

    event: Mapped["Event"] = relationship(
        "Event",
        back_populates="registrations"
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="registrations"
    )
