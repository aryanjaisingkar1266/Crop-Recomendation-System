import requests
from datetime import datetime
import json

class CropRecommender:
    def __init__(self):
        self.crops_db = {
            "wheat": {"temp_range": (15, 25), "rainfall": (400, 700), "wind_speed": (0, 20), "season": "winter"},
            "rice": {"temp_range": (20, 35), "rainfall": (1000, 2000), "wind_speed": (0, 15), "season": "summer"},
            "corn": {"temp_range": (15, 30), "rainfall": (500, 800), "wind_speed": (0, 25), "season": "summer"},
            "cotton": {"temp_range": (20, 35), "rainfall": (500, 700), "wind_speed": (0, 20), "season": "summer"},
            "potato": {"temp_range": (15, 20), "rainfall": (400, 600), "wind_speed": (0, 15), "season": "winter"},
            "tomato": {"temp_range": (18, 25), "rainfall": (400, 800), "wind_speed": (0, 20), "season": "summer"},
            "soybean": {"temp_range": (20, 30), "rainfall": (500, 900), "wind_speed": (0, 20), "season": "summer"},
            "barley": {"temp_range": (12, 20), "rainfall": (300, 500), "wind_speed": (0, 20), "season": "winter"}
        }
    
    def get_current_season(self):
        month = datetime.now().month
        if month in [12, 1, 2]:
            return "winter"
        elif month in [3, 4, 5]:
            return "spring"
        elif month in [6, 7, 8]:
            return "summer"
        else:
            return "autumn"
    
    def get_weather_data(self, location="Delhi"):
        try:
            api_key = "d5f8f9c8b7a6e5d4c3b2a1f0e9d8c7b6"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 200:
                rainfall = data.get("rain", {}).get("1h", 0)
                if rainfall == 0:
                    rainfall = data.get("clouds", {}).get("all", 50) * 2
                
                return {
                    "temperature": round(data["main"]["temp"], 1),
                    "rainfall": rainfall,
                    "wind_speed": round(data["wind"]["speed"] * 3.6, 1),
                    "humidity": data["main"]["humidity"]
                }
            else:
                print(f"Weather API Error for {location}: {data.get('message', 'Unknown error')}")
                return self._get_fallback_weather(location)
                
        except Exception as e:
            print(f"Error fetching weather data: {e}")
            return self._get_fallback_weather(location)
    
    def _get_fallback_weather(self, location):
        location_weather = {
            "delhi": {"temp": 28, "rain": 450, "wind": 12},
            "mumbai": {"temp": 30, "rain": 2200, "wind": 15},
            "pune": {"temp": 26, "rain": 700, "wind": 10},
            "yavatmal": {"temp": 27, "rain": 900, "wind": 11},
            "bangalore": {"temp": 24, "rain": 900, "wind": 8},
            "chennai": {"temp": 32, "rain": 1200, "wind": 14},
            "nagpur": {"temp": 29, "rain": 1200, "wind": 13},
            "punjab": {"temp": 24, "rain": 400, "wind": 8},
            "amritsar": {"temp": 24, "rain": 400, "wind": 8},
            "kolkata": {"temp": 31, "rain": 1600, "wind": 12},
            "hyderabad": {"temp": 27, "rain": 800, "wind": 9},
            "jaipur": {"temp": 32, "rain": 350, "wind": 14},
            "lucknow": {"temp": 29, "rain": 900, "wind": 11},
            "indore": {"temp": 26, "rain": 1100, "wind": 10},
            "ahmedabad": {"temp": 33, "rain": 650, "wind": 12},
            "surat": {"temp": 31, "rain": 1800, "wind": 13},
            "kanpur": {"temp": 30, "rain": 850, "wind": 11},
            "nagaland": {"temp": 22, "rain": 1800, "wind": 7},
            "gujarat": {"temp": 31, "rain": 650, "wind": 12},
            "rajasthan": {"temp": 33, "rain": 350, "wind": 14}
        }
        
        loc_key = location.lower()
        weather = location_weather.get(loc_key, {"temp": 25, "rain": 600, "wind": 10})
        
        return {
            "temperature": weather["temp"],
            "rainfall": weather["rain"],
            "wind_speed": weather["wind"],
            "humidity": 65
        }
    
    def calculate_crop_score(self, crop_data, weather_data, current_season):
        score = 0
        
        temp_min, temp_max = crop_data["temp_range"]
        if temp_min <= weather_data["temperature"] <= temp_max:
            score += 30
        elif abs(weather_data["temperature"] - temp_min) < 5 or abs(weather_data["temperature"] - temp_max) < 5:
            score += 15
        
        rain_min, rain_max = crop_data["rainfall"]
        if rain_min <= weather_data["rainfall"] <= rain_max:
            score += 30
        elif abs(weather_data["rainfall"] - rain_min) < 100 or abs(weather_data["rainfall"] - rain_max) < 100:
            score += 15
        
        wind_min, wind_max = crop_data["wind_speed"]
        if wind_min <= weather_data["wind_speed"] <= wind_max:
            score += 20
        
        if crop_data["season"] == current_season or current_season in ["spring", "autumn"]:
            score += 20
        
        return score
    
    def recommend_crops(self, location="Delhi"):
        weather_data = self.get_weather_data(location)
        current_season = self.get_current_season()
        
        crop_scores = {}
        for crop, data in self.crops_db.items():
            score = self.calculate_crop_score(data, weather_data, current_season)
            crop_scores[crop] = score
        
        recommended_crops = sorted(crop_scores.items(), key=lambda x: x[1], reverse=True)
        
        return recommended_crops[:3], weather_data, current_season

def main():
    print("🌾 Crop Recommendation System for Farmers 🌾")
    print("=" * 50)
    
    location = input("Enter your location (default: Delhi): ") or "Delhi"
    
    recommender = CropRecommender()
    recommended_crops, weather_data, current_season = recommender.recommend_crops(location)
    
    print(f"\n📍 Location: {location}")
    print(f"🌡️  Current Temperature: {weather_data['temperature']}°C")
    print(f"💧 Rainfall: {weather_data['rainfall']}mm")
    print(f"💨 Wind Speed: {weather_data['wind_speed']} km/h")
    print(f"📅 Season: {current_season.capitalize()}")
    print("\n🌱 Recommended Crops:")
    print("-" * 30)
    
    for i, (crop, score) in enumerate(recommended_crops, 1):
        print(f"{i}. {crop.capitalize()} - Score: {score}/100")
        crop_data = recommender.crops_db[crop]
        print(f"   Best Temp: {crop_data['temp_range'][0]}-{crop_data['temp_range'][1]}°C")
        print(f"   Best Rainfall: {crop_data['rainfall'][0]}-{crop_data['rainfall'][1]}mm")
        print()

if __name__ == "__main__":
    main()
