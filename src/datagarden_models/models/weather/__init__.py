from pydantic import BaseModel, Field
from typing import Literal, Optional

TEMP_SCALES: Literal["CELSIUS", "FAHRENHEID"]


class WeatherV1Keys:
	MIN_TEMP = "min_temp"
	MAX_TEMP = "max_temp"
	MEAN_TEMP = "mean_temp"
	RAIN_FALL_MM = "rain_fall_mm"
	SEA_LEVEL_PRESSURE_HPA = "sea_level_pressure_hpa"
	CLOUD_COVER_OKTA = "cloud_cover_okta"
	TEMP_SCALE = "temp_scale"
	WIND_DIRECTION = "wind_direction"
	WIND_SPEED_M_S = "wind_speed_m_s"
	MAX_WIND_GUST_M_S = "max_wind_gust_m_s"
	SUN_HOURS = "sun_hours"
	SNOW_DEPTH_CM = "snow_depth_cm"
	RADIATION_PER_SQUARE_M = "radiation_per_square_m"
	HUMIDITY = "humidity"
	DATAGARDEN_MODEL_NAME = "WeatherData"


class WaetherV1Legends:
	MIN_TEMP = "min_temp"
	MAX_TEMP = "max_temp"
	MEAN_TEMP = "mean_temp"
	RAIN_FALL_MM = "rain_fall_mm"
	SEA_LEVEL_PRESSURE_HPA = "sea_level_pressure_hpa"
	CLOUD_COVER_OKTA = "cloud_cover_okta"
	TEMP_SCALE = "temp_scale"
	WIND_DIRECTION = "wind_direction"
	WIND_SPEED_M_S = "wind_speed_m_s"
	MAX_WIND_GUST_M_S = "max_wind_gust_m_s"
	SUN_HOURS = "sun_hours"
	SNOW_DEPTH_CM = "snow_depth_cm"
	RADIATION_PER_SQUARE_M = "radiation_per_square_m"
	HUMIDITY = "humidity"


L = WaetherV1Legends


class WeatherData(BaseModel):
	min_temp: float = Field(..., ge=-70, le=70)
	max_temp: float = Field(..., ge=-70, le=70)
	mean_temp: Optional[float] = Field(None, ge=-70, le=70)
	rain_fall_mm: Optional[float] = Field(None, ge=0)
	sea_level_pressure_hpa: Optional[float] = Field(None, ge=850, le=1100)
	cloud_cover_okta: Optional[int] = Field(None, ge=0, le=8)
	temp_scale: Literal["CELSIUS", "FAHRENHEID"] = "CELSIUS"
	wind_direction: Optional[int] = Field(None, ge=0, le=359)
	wind_speed_m_s: Optional[float] = Field(None, ge=0, le=110)
	max_wind_gust_m_s: Optional[float] = Field(None, ge=0, le=110)
	sun_hours: Optional[float] = Field(None, ge=0, le=24)
	snow_depth_cm: Optional[float] = Field(None, ge=0, le=10000)
	radiation_per_square_m: Optional[float] = Field(None, ge=-100, le=2000)
	humidity: Optional[float] = Field(None, ge=0, le=100)
