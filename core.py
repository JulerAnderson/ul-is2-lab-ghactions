from datetime import datetime, timezone

def payload():
    return {
        "ok": False,
        "ts": datetime.now(timezone.utc).isoformat()
    }
