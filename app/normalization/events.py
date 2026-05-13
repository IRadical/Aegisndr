from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ZeekConnection(BaseModel):
    ts: float
    uid: str
    id_orig_h: str
    id_orig_p: int
    id_resp_h: str
    id_resp_p: int
    proto: str
    service: Optional[str] = None
    duration: Optional[float] = None
    orig_bytes: Optional[int] = None
    resp_bytes: Optional[int] = None
    conn_state: Optional[str] = None

class SuricataAlert(BaseModel):
    timestamp: datetime
    event_type: str
    src_ip: str
    src_port: int
    dest_ip: str
    dest_port: int
    proto: str
    signature_id: int
    signature: str
    category: str
    severity: int

    mitre_tactic: Optional[str] = None
    mitre_technique: Optional[str] = None