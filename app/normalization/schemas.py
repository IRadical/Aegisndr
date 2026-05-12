import json
from typing import List, Dict, Any
from app.normalization.schemas import ZeekConnection

class ZeekParser:

    def parse_conn_log(self, file_path: str) -> List[ZeekConnection]:
        events = []
        with open(file_path, 'r') as f:
            for line in f:
                try:
                    data = json.loads(line)
                    event=ZeekConnection(**data)
                    events.append(event)
                except (json.JSONDecodeError, ValueError) as e:
                    continue
        return events
    
    