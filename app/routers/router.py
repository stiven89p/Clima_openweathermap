from fastapi import APIRouter, HTTPException, Form
import httpx


API_KEY = "90c26ebc8e5a3ba5a06e8506ea511684"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

router = APIRouter(
    prefix="/categorias",
    tags=["categorias"],
)

@router.get("/{ciudad}")
async def obtener_clima(ciudad: str):
    params = {
        "q": ciudad,
        "appid": API_KEY,
        "units": "metric",  
        "lang": "es"       
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            "ciudad": data["name"],
            "temperatura": data["main"]["temp"],
            "descripcion": data["weather"][0]["description"],
            "humedad": data["main"]["humidity"],
            "presion": data["main"]["pressure"],
        }
    else:
        return {
            "error": f"No se pudo obtener el clima ({response.status_code})",
            "detalle": response.text
        }
