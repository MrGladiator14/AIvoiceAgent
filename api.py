import random
from typing import Annotated
from livekit.agents import llm
import logging

logger = logging.getLogger("weather-api")
logger.setLevel(logging.INFO)


class WeatherApi(llm.FunctionContext):
    @llm.ai_callable(description="Get the current weather in a specific city")
    def get_weather(
        self,
        city: Annotated[
            str,
            llm.TypeInfo(description="The city to get the weather for, e.g. 'San Francisco'"),
        ],
    ):
        logger.info("getting weather for city %s", city)
        temp = random.randint(5, 30)
        conditions = ["sunny", "cloudy", "rainy", "windy"]
        condition = random.choice(conditions)
        return f"The weather in {city} is {condition} with a temperature of {temp} degrees Celsius."
