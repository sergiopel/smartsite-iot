from app.models.sensor import Sensor
from app.schemas.sensor_response import SensorResponse


def to_sensor_response(sensor: Sensor) -> SensorResponse:
    return SensorResponse(
        sensor_id=sensor.sensor_id,
        temperature=sensor.temperature,
        limit=sensor.limit,
        status=sensor.get_status()
    )
