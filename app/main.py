from pydantic import BaseModel

# sensor = {
#     "sensor_id": "sensor_001",
#     "temperature": 29.0,
#     "location": "ambiente externo",
#     "limit": 30.0
# }

class Sensor(BaseModel):
    sensor_id: str
    temperature: float
    location: str
    limit: float

sensor = Sensor(sensor_id="sensor_001", temperature="26.5", location="ambiente externo", limit=25.0)

def is_temperature_alert(temperature: float, limit: float) -> bool:
    return temperature > limit

#resultado = is_temperature_alert(sensor["temperature"], sensor["limit"])
resultado = is_temperature_alert(sensor.temperature, sensor.limit)
print(resultado)

print(sensor.temperature)
print(type(sensor.temperature))

