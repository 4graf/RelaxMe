from microservices.stress_recognizer.services.stress_recognizer_service import StressRecognizerService


async def get_recognizer_stress_service() -> StressRecognizerService:
    return StressRecognizerService()
