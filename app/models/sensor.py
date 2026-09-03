from enum import Enum

from pydantic import BaseModel


class SensorStatus(str, Enum):
    NORMAL = "normal"
    ALERT = "alert"


class Sensor(BaseModel):
    sensor_id: str
    temperature: float
    location: str
    limit: float

    def is_temperature_alert(self) -> bool:
        return self.temperature > self.limit

    def get_status(self) -> SensorStatus:
        if self.is_temperature_alert():
            return SensorStatus.ALERT
        else:
            return SensorStatus.NORMAL

