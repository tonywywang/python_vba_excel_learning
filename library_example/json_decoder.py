import io
import json

header = b'{"squadName": "Super hero squad", "homeTown": "Metro City", "formed": 2016, "secretBase": "Super tower", "active": true}'


tiow = io.TextIOWrapper(
            io.BytesIO(header), encoding="utf-8", newline=""
        )

bj = json.loads(header)
print(json.dumps(bj))
print(bj["homeTown"])
tiow.close()