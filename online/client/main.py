import asyncio

from httpx import AsyncClient

from online.client.EEG.services.EEG_device_service import EEGDeviceService
from online.stress_recognizer.services.stress_recognizer_service import StressRecognizerService
from online.stress_recognizer.util.constants import DataMode

eeg_device_service = EEGDeviceService()

# stress_recognizer_service = StressRecognizerService()


async def do_predict():
    eeg_device_service.start()
    await asyncio.sleep(5)
    data = eeg_device_service.get_data(only_eeg=True)

    # prediction = await stress_recognizer_service.predict_stress(data, DataMode.RAW)
    async with AsyncClient() as client:
        response = await client.post('http://localhost:3000/api/v1/stress/predict', json={'data': data.tolist()})
        prediction = response.json()
    print(prediction)

asyncio.run(do_predict())
