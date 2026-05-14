from sqlalchemy.orm import Session
from app.db.models import NetworkEvent, Alert
from datetime import datetime, timedelta

class DetectionEngine:
    def __init__(self, db: Session):
        self.db = db
    
    def analyze_port_scan(self, target_ip: str, threshold: int = 10):
        time_limit = datetime.utcnow() - timedelta(minutes=5)
        
        recent_events = self.db.query(NetworkEvent).filter(
            NetworkEvent.source_ip == target_ip,
            NetworkEvent.timestamp >= time_limit
        ).all()

        unique_ports = {event.destination_port for event in recent_events}

        if len(unique_ports) >= threshold:
            self.create_detection_alert(
                target_ip,
                "Potential Port Scan Detected",
            )
        
        def create_detection_alert(self, source_ip: str, message: str):
            new_alert = Alert(
                signature=message,
                severity=3,
                category="Reconnaissance",
                mitre_tactic="Discovery",
            )
            self.db.add(new_alert)
            self.db.commit()