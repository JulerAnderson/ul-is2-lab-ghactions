import json
import core
from workers import Response

def on_fetch(request):
    return Response(json.dumps(payload()),
                    headers={"content-type": "application/json"})
