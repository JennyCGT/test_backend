from re import S, T
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=True) 
    last_name = Column(String(50), nullable=True) 
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    department = Column(String(),nullable= True)
    company = Column(String(),nullable=True)
    role = Column(String(),nullable=True)
    title = Column(String(),nullable= True)
    address = Column(String(), nullable=True)
    city = Column(String(),nullable= True)
    state = Column(String(),nullable= True)
    zip= Column(String(),nullable= True)
    country= Column(String(),nullable= True)
    language = Column(String(),nullable=True)
    items = relationship("Item", back_populates="owner")
    role =Column('group_id', Integer, ForeignKey('tg_group.group_id',onupdate="CASCADE",ondelete="CASCADE"),primary_key=True)

class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(), nullable= True)
    description = Column(String(), nullable=True)
    

class UserGroup(Base):
    __tablename__ = 'user_group_role'
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_id = Column('group_id', Integer, ForeignKey('group.id',onupdate="CASCADE",ondelete="CASCADE"),primary_key=True)
    user_id = Column('user_id', Integer, ForeignKey('users.id',onupdate="CASCADE",ondelete="CASCADE"),primary_key=True)
    # role = Column('roles_id', Integer, ForeignKey('role.id',onupdate="CASCADE",ondelete="CASCADE"),primary_key=True)


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String,nullable=True)
