from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Numeric,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'Artist'
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String(120))

class Album(Base):
    __tablename__ = 'Album'
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String(160), nullable=False)
    ArtistId = Column(Integer, ForeignKey('Artist.ArtistId'))

class Employee(Base):
    __tablename__ = 'Employee'
    EmployeeId = Column(Integer, primary_key=True)
    LastName = Column(String(20), nullable=False)
    FirstName = Column(String(20), nullable=False)
    Title = Column(String(30))
    ReportsTo = Column(Integer)
    BirthDate = Column(String)
    HireDate = Column(String)
    Address = Column(String(70))
    City = Column(String(40))
    State = Column(String(40))
    Country = Column(String(40))
    PostalCode = Column(String(10))
    Phone = Column(String(24))
    Fax = Column(String(24))
    Email = Column(String(60))

class Customer(Base):
    __tablename__ = 'Customer'

    CustomerId = Column(Integer, primary_key=True)
    FirstName = Column(String)
    LastName = Column(String)
    Company = Column(String)
    Address = Column(String)
    City = Column(String)
    State = Column(String)
    Country = Column(String)
    PostalCode = Column(String)
    Phone = Column(String)
    Fax = Column(String)
    Email = Column(String)
    SupportRepId = Column(Integer, ForeignKey('support_reps.id'))


class Genre(Base):
    __tablename__ = 'Genre'
    GenreId = Column(Integer, primary_key=True)
    Name = Column(String(120))

class Invoice(Base):
    __tablename__ = 'Invoice'
    InvoiceId = Column(Integer, primary_key=True)
    CustomerId = Column(Integer, nullable=False)
    InvoiceDate = Column(DateTime, nullable=False)
    BillingAddress = Column(String(70))
    BillingCity = Column(String(40))
    BillingState = Column(String(40))
    BillingCountry = Column(String(40))
    BillingPostalCode = Column(String(10))
    Total = Column(Numeric(10,2), nullable=False)

    
class MediaType(Base):
    __tablename__ = 'MediaType'
    MediaTypeId = Column(Integer, primary_key=True)
    Name = Column(String(120))

class Playlist(Base):
    __tablename__ = 'Playlist'
    PlaylistId = Column(Integer, primary_key=True)
    Name = Column(String(120))


class Track(Base):
    __tablename__ = 'Track'
    
    TrackId = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(200), nullable=False)
    AlbumId = Column(Integer, ForeignKey('Album.AlbumId'))  
    MediaTypeId = Column(Integer, ForeignKey('MediaType.MediaTypeId'), nullable=False) 
    GenreId = Column(Integer, ForeignKey('Genre.GenreId'))
    Composer = Column(String(220))
    Milliseconds = Column(Integer, nullable=False)
    Bytes = Column(Integer)
    UnitPrice = Column(Numeric(10,2), nullable=False)

class PlaylistTrack(Base):
    __tablename__ = 'PlaylistTrack'
    
    PlaylistId = Column(Integer, ForeignKey('Playlist.PlaylistId'), primary_key=True)  # Assuming there's a Playlist table with PlaylistId as PK
    TrackId = Column(Integer, ForeignKey('Track.TrackId'), primary_key=True)          # Assuming there's a Track table with TrackId as PK

class InvoiceLine(Base):
    __tablename__ = 'InvoiceLine'
    
    InvoiceLineId = Column(Integer, primary_key=True)
    InvoiceId = Column(Integer, ForeignKey('Invoice.InvoiceId'))  # Assuming there's an Invoice table with InvoiceId as PK
    TrackId = Column(Integer, ForeignKey('Track.TrackId'))        # Assuming there's a Track table with TrackId as PK
    UnitPrice = Column(Numeric(10, 2))
    Quantity = Column(Integer)
