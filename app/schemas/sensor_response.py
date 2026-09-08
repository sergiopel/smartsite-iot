from pydantic import BaseModel

from app.models.sensor import SensorStatus


class SensorResponse(BaseModel):
    sensor_id: str
    temperature: float
    limit: float
    status: SensorStatus
