from pydantic import BaseModel, Field


class HealthBaseKeys:
	MALE = "male"
	FEMALE = "female"
	TOTAL = "total"


class HealthBaseLegends:
	MALE = "Statistics specified for male population. "
	FEMALE = "Statistics specified for female population. "
	TOTAL = "Statistics specified for total population. "


L = HealthBaseLegends


class ByGender(BaseModel):
	male: dict = Field(default_factory=dict, description=L.MALE)
	female: dict = Field(default_factory=dict, description=L.FEMALE)
	total: dict = Field(default_factory=dict, description=L.TOTAL)