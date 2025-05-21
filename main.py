from fastapi import FastAPI, HTTPException

app = FastAPI()

players = [
    {"jersey_no": 10, "name": "Lionel Messi", "club_name": "FC Barcelona", "mvp": True},
    {"jersey_no": 7, "name": "Cristiano Ronaldo", "club_name": "Juventus FC", "mvp": False},
    {"jersey_no": 11, "name": "Neymar Jr.", "club_name": "Paris Saint-Germain", "mvp": True},
    {"jersey_no": 9, "name": "Robert Lewandowski", "club_name": "Bayern Munich", "mvp": False},
    {"jersey_no": 17, "name": "Kylian Mbappé", "club_name": "Paris Saint-Germain", "mvp": True},
    {"jersey_no": 8, "name": "Paul Pogba", "club_name": "Manchester United", "mvp": False},
    {"jersey_no": 4, "name": "Virgil van Dijk", "club_name": "Liverpool FC", "mvp": True},
    {"jersey_no": 1, "name": "Alisson Becker", "club_name": "Liverpool FC", "mvp": False},
    {"jersey_no": 5, "name": "Mohamed Salah", "club_name": "Liverpool FC", "mvp": True},
    {"jersey_no": 3, "name": "Eden Hazard", "club_name": "Real Madrid", "mvp": False}
]


@app.get("/")
async def index() -> dict[str, str]:
    return {"message": "Hello World"}

@app.get("/")
async def index() -> dict[str, str]:
    return {"message": "Hello World"}
@app.get("/players")
async def about() -> list[dict]:
    return players


@app.get("/players/{jersey_no}")
async def player_jerseyno(jersey_no: int) -> dict:
    for player in players:
        if player["jersey_no"] == jersey_no:
            return player
    return {"message": "Player not found"}


@app.get("/players/{name}")
async def get_player(name: str) -> dict:
    player = next((player for player in players if player["name"] == name), None)
    if player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

