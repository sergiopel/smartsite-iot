from app.models.sensor import Sensor

sensor = Sensor(sensor_id="sensor_001", temperature="26.0", location="ambiente externo", limit=25.0)

print(f"Sensor: {sensor.sensor_id}")
print(f"Temperatura: {sensor.temperature}")
print(f"Status:  {sensor.get_status().value}")



