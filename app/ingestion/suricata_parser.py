import json
from typing import List
from app.normalization.schemas import SuricataAlert

class SuricataParser:
    def parse_alerts(self, file_path: str) -> List[SuricataAlert]:
        alerts = []
        with open(file_path, 'r') as f:
            for line in f:
                try:
                    data = json.loads(line)
                    if data.get("event_type") == "alert":
                        alerta_data = data.get("alert", {})
                        normalized = SuricataAlert(
                            timestamp=data.get("timestamp"),
                            src_ip=data.get("src_ip"),
                            src_port=data.get("src_port"),
                            dest_ip=data.get("dest_ip"),
                            dest_port=data.get("dest_port"),
                            proto=data.get("proto"),
                            signature_id=alerta_data.get("signature_id"),
                            signature=alerta_data.get("signature"),
                            category=alerta_data.get("category"),
                            severity=alerta_data.get("severity"),
                        )
                        alerts.append(normalized)
                except (json.JSONDecodeError, KeyError) as e:
                    continue
        return alerts