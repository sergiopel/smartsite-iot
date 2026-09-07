from fastapi import FastAPI, HTTPException, status

from app.models.sensor import Sensor


app = FastAPI()

sensors = {}


@app.get("/")
def root():
    return {"message": "SmartSite IoT API"}


@app.get("/sensors/{sensor_id}")
def get_sensor(sensor_id: str) -> dict:
    if sensor_id not in sensors:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sensor not found"
        )
    sensor = sensors[sensor_id]

    return {
        "sensor_id": sensor.sensor_id,
        "temperature": sensor.temperature,
        "limit": sensor.limit,
        "status": sensor.get_status().value
    }


@app.get("/sensors")
def get_sensors() -> list:
    result = []

    for sensor in sensors.values():
        result.append({
            "sensor_id": sensor.sensor_id,
            "temperature": sensor.temperature,
            "limit": sensor.limit,
            "status": sensor.get_status().value
        })

    return result


@app.post("/sensors", status_code=status.HTTP_201_CREATED)
def create_sensor(sensor: Sensor) -> dict:
    sensors[sensor.sensor_id] = sensor

    return {
        "sensor_id": sensor.sensor_id,
        "temperature": sensor.temperature,
        "limit": sensor.limit,
        "status": sensor.get_status().value
    }
