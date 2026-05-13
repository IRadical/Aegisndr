from sqlalchemy.orm import Session
from app.db.models import NetworkEvent
from app.normalization.schemas import ZeekConnection

class EventService:
    def __init__(self, db: Session):
        self.db = db

    def save_zeek_event(self, event_data: ZeekConnection):
        db_event = NetworkEvent(
            source_ip=event_data.id_orig_h,
            source_port=event_data.id_orig_p,
            destination_ip=event_data.id_resp_h,
            destination_port=event_data.id_resp_p,
            protocol=event_data.proto,
            event_type="connection",
            raw_payload=str(event_data.dict())
        )
        self.db.add(db_event)
        self.db.commit()
        self.db.refresh(db_event)
        return db_event