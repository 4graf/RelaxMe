from online.stress_recognizer.services.recognizer_service import RecognizerService


async def get_recognizer_stress_service() -> RecognizerService:
    return RecognizerService()
