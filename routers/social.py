from fastapi import APIRouter, HTTPException
from services.social_services import get_social_media_links

router = APIRouter()

@router.get("/social_media_links", status_code=200)
def social_links():
    try:
        return get_social_media_links()
    except:
        raise HTTPException(
            status_code=500, detail="Internal Server Error"
        )
