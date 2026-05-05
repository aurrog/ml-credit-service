import logging
import json
from datetime import datetime, UTC


logger = logging.getLogger("api_logger")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("logs/api.log", encoding="utf-8")
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)


def log_event(data: dict):
    log_record = {
        "timestamp": datetime.now(UTC).isoformat(),
        **data
    }

    logger.info(json.dumps(log_record, ensure_ascii=False))