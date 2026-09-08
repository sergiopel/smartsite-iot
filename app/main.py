from fastapi import FastAPI, HTTPException, status

from app.models.sensor import Sensor
from app.schemas.sensor_response import SensorResponse
from app.mappers.sensor_mapper import to_sensor_response

app = FastAPI()

sensors = {}

@app.get("/")
def root():
    return {"message": "SmartSite IoT API v1"}


@app.get(
    "/sensors/{sensor_id}",
    response_model=SensorResponse
)
def get_sensor(sensor_id: str) -> SensorResponse:
    if sensor_id not in sensors:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sensor not found"
        )
    sensor = sensors[sensor_id]

    return to_sensor_response(sensor)


@app.get("/sensors", response_model=list[SensorResponse])
def get_sensors() -> list[SensorResponse]:
    result = []

    for sensor in sensors.values():
        result.append(
            to_sensor_response(sensor)
        )

    return result


@app.post(
    "/sensors",
    status_code=status.HTTP_201_CREATED,
    response_model=SensorResponse
)
def create_sensor(sensor: Sensor) -> SensorResponse:
    sensors[sensor.sensor_id] = sensor

    return to_sensor_response(sensor)
