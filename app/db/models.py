from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from .base import Base

class NetworkEvent(Base):
    __tablename__ = 'network_events'

    id = Column (Integer, primary_key=True, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    source_ip = Column(String, index=True)
    source_port = Column(Integer)
    destination_ip = Column(String, index=True)
    destination_port = Column(Integer)
    protocol = Column(String)
    event_type = Column(String)
    raw_payload = Column(String)

class Alert(Base):
    __tablename__ = 'alerts'

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey('network_events.id'))
    signature = Column(String)
    severity = Column(Integer)
    category = Column(String)
    mitre_tactic = Column(str, nullable=True)
    mitre_technique = Column(str, nullable=True)


