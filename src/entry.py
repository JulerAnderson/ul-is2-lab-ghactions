import json
from src.core import payload

def on_fetch(request):
    from workers import Response
    return Response(json.dumps(payload()),
                    headers={"content-type": "application/json"})
