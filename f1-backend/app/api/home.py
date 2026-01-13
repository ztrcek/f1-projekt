from fastapi import APIRouter
import httpx

router = APIRouter()

@router.get("/home")
async def get_home():
    async with httpx.AsyncClient() as client:
        # --- Top 5 driverjev ---
        drivers_resp = await client.get("https://f1api.dev/api/drivers")
        drivers_json = drivers_resp.json()
        drivers_data = drivers_json.get("drivers", [])[:5]  # vzamemo prvih 5

        # --- Top 5 ekip ---
        constructors_resp = await client.get("https://f1api.dev/api/constructors")
        constructors_json = constructors_resp.json()
        constructors_data = constructors_json.get("constructors", [])[:5]  # preveri ključ v JSON

        # --- Naslednje 3 dirke ---
        races_resp = await client.get("https://f1api.dev/api/races")
        races_json = races_resp.json()
        next_races = races_json.get("races", [])[:3]  # vzamemo naslednje 3 dirke

    # --- Mock zadnja dirka ---
    last_race_results = [
        {"position": 1, "driver": "Max Verstappen", "time": "1:24:30.123"},
        {"position": 2, "driver": "Lewis Hamilton", "time": "1:24:45.567"},
        {"position": 3, "driver": "Charles Leclerc", "time": "1:25:10.890"}
    ]

    # --- Mock novice ---
    news = [
        {"title": "Verstappen wins dramatic race!", "source": "BBC", "url": "https://bbc.com/f1-news"},
        {"title": "Mercedes introduces new car upgrade", "source": "ESPN", "url": "https://espn.com/f1-news"},
        {"title": "Ferrari struggles in qualifying", "source": "Sky Sports", "url": "https://skysports.com/f1-news"}
    ]

    return {
        "drivers_top5": drivers_data,
        "constructors_top5": constructors_data,
        "next_races": next_races,
        "last_race_results": last_race_results,
        "news": news
    }
