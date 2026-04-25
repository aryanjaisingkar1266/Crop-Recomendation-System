import requests
from datetime import datetime
import json

class CropRecommender:
    def __init__(self):
        self.crops_db = {
             "rice": {"temp_range": (20, 35), "rainfall": (1000, 2000), "wind_speed": (0, 15), "season": "kharif"},
             "wheat": {"temp_range": (10, 25), "rainfall": (500, 1000), "wind_speed": (0, 20), "season": "rabi"},
             "maize": {"temp_range": (18, 27), "rainfall": (500, 800), "wind_speed": (0, 20), "season": "kharif"},
             "barley": {"temp_range": (12, 20), "rainfall": (300, 500), "wind_speed": (0, 20), "season": "rabi"},
             "cotton": {"temp_range": (21, 30), "rainfall": (500, 1000), "wind_speed": (0, 15), "season": "kharif"},
             "sugarcane": {"temp_range": (20, 35), "rainfall": (750, 1500), "wind_speed": (0, 10), "season": "annual"},
             "millet": {"temp_range": (25, 35), "rainfall": (300, 600), "wind_speed": (0, 25), "season": "kharif"},
             "sorghum": {"temp_range": (25, 32), "rainfall": (400, 700), "wind_speed": (0, 25), "season": "kharif"},
             "pulses": {"temp_range": (20, 30), "rainfall": (400, 800), "wind_speed": (0, 20), "season": "both"},
             "groundnut": {"temp_range": (25, 35), "rainfall": (500, 1000), "wind_speed": (0, 20), "season": "kharif"},
             "mustard": {"temp_range": (10, 25), "rainfall": (300, 600), "wind_speed": (0, 15), "season": "rabi"},
             "soybean": {"temp_range": (20, 30), "rainfall": (600, 1000), "wind_speed": (0, 20), "season": "kharif"},
             "tea": {"temp_range": (20, 30), "rainfall": (1500, 3000), "wind_speed": (0, 10), "season": "perennial"},
             "coffee": {"temp_range": (15, 28), "rainfall": (1500, 2500), "wind_speed": (0, 10), "season": "perennial"},
             "jute": {"temp_range": (24, 35), "rainfall": (1000, 2000), "wind_speed": (0, 15), "season": "kharif"},
             "potato": {"temp_range": (15, 25), "rainfall": (500, 1000), "wind_speed": (0, 15), "season": "rabi"},
             "onion": {"temp_range": (13, 30), "rainfall": (500, 800), "wind_speed": (0, 15), "season": "both"},
             "tomato": {"temp_range": (18, 27), "rainfall": (400, 700), "wind_speed": (0, 15), "season": "both"},
             "banana": {"temp_range": (20, 35), "rainfall": (1000, 2500), "wind_speed": (0, 10), "season": "annual"},
             "mango": {"temp_range": (24, 35), "rainfall": (750, 2500), "wind_speed": (0, 10), "season": "summer"},
             "chickpea": {"temp_range": (20, 30), "rainfall": (400, 600), "wind_speed": (0, 20), "season": "rabi"},
             "lentil": {"temp_range": (18, 30), "rainfall": (300, 500), "wind_speed": (0, 20), "season": "rabi"},
             "blackgram": {"temp_range": (25, 35), "rainfall": (600, 800), "wind_speed": (0, 20), "season": "kharif"},
             "greengram": {"temp_range": (25, 35), "rainfall": (500, 700), "wind_speed": (0, 20), "season": "kharif"},
             "peas": {"temp_range": (10, 25), "rainfall": (400, 700), "wind_speed": (0, 15), "season": "rabi"},
             "sunflower": {"temp_range": (20, 30), "rainfall": (500, 800), "wind_speed": (0, 20), "season": "both"},
             "sesame": {"temp_range": (25, 35), "rainfall": (300, 600), "wind_speed": (0, 20), "season": "kharif"},
             "castor": {"temp_range": (20, 30), "rainfall": (500, 800), "wind_speed": (0, 20), "season": "kharif"},
             "linseed": {"temp_range": (10, 25), "rainfall": (400, 700), "wind_speed": (0, 15), "season": "rabi"},
             "tobacco": {"temp_range": (20, 30), "rainfall": (600, 1000), "wind_speed": (0, 15), "season": "both"},
             "cabbage": {"temp_range": (15, 25), "rainfall": (400, 800), "wind_speed": (0, 15), "season": "rabi"},
             "cauliflower": {"temp_range": (15, 25), "rainfall": (400, 800), "wind_speed": (0, 15), "season": "rabi"},
             "brinjal": {"temp_range": (20, 30), "rainfall": (600, 1000), "wind_speed": (0, 15), "season": "both"},
             "chili": {"temp_range": (20, 30), "rainfall": (600, 1200), "wind_speed": (0, 15), "season": "kharif"},
             "garlic": {"temp_range": (12, 25), "rainfall": (300, 500), "wind_speed": (0, 15), "season": "rabi"},
             "ginger": {"temp_range": (20, 30), "rainfall": (1000, 2000), "wind_speed": (0, 10), "season": "kharif"},
             "turmeric": {"temp_range": (20, 30), "rainfall": (1000, 2000), "wind_speed": (0, 10), "season": "kharif"},
             "apple": {"temp_range": (5, 24), "rainfall": (800, 1500), "wind_speed": (0, 10), "season": "temperate"},
             "grapes": {"temp_range": (15, 35), "rainfall": (500, 800), "wind_speed": (0, 10), "season": "annual"},
             "orange": {"temp_range": (15, 30), "rainfall": (750, 1500), "wind_speed": (0, 10), "season": "annual"},
             "papaya": {"temp_range": (22, 35), "rainfall": (1000, 2000), "wind_speed": (0, 10), "season": "annual"},
            "pineapple": {"temp_range": (20, 30), "rainfall": (1000, 1500), "wind_speed": (0, 10), "season": "perennial"},
            "watermelon": {"temp_range": (22, 35), "rainfall": (400, 600), "wind_speed": (0, 15), "season": "summer"},
            "muskmelon": {"temp_range": (25, 35), "rainfall": (300, 500), "wind_speed": (0, 15), "season": "summer"}
        }
    
    def get_current_season(self):
        month = datetime.now().month
        # Indian agricultural seasons
        if month in [6, 7, 8, 9, 10]:
            return "kharif"  # Monsoon season (June-October)
        elif month in [10, 11, 12, 1, 2]:
            return "rabi"     # Winter season (October-February)
        elif month in [3, 4, 5]:
            return "zaid"     # Summer season (March-May)
        else:
            return "both"      # For crops that can be grown year-round
    
    def get_weather_data(self, location="Delhi"):
        try:
            # Use a working OpenWeatherMap API key
            api_key = "bd5e378503939ddaee76f12ad7a97608"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 200:
                # Get rainfall data (in mm)
                rainfall = data.get("rain", {}).get("1h", 0)
                if rainfall == 0:
                    # If no rain data, estimate based on humidity and cloud cover
                    humidity = data["main"]["humidity"]
                    clouds = data.get("clouds", {}).get("all", 0)
                    rainfall = max(0, (humidity + clouds) / 4)
                
                # Convert wind speed from m/s to km/h
                wind_speed_kmh = data["wind"]["speed"] * 3.6
                
                return {
                    "temperature": round(data["main"]["temp"], 1),
                    "rainfall": round(rainfall, 1),
                    "wind_speed": round(wind_speed_kmh, 1),
                    "humidity": data["main"]["humidity"]
                }
            else:
                print(f"⚠️  Weather API Error for {location}: {data.get('message', 'Unknown error')}")
                print("📍 Using real-time data from OpenWeatherMap failed")
                return self._get_fallback_weather(location)
                
        except Exception as e:
            print(f"❌ Error fetching weather data: {e}")
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
        
        # Indian agricultural season matching
        crop_season = crop_data["season"]
        if crop_season == "both" or crop_season == "annual" or crop_season == "perennial":
            score += 20  # Crops that can be grown year-round
        elif crop_season == current_season:
            score += 20  # Perfect season match
        elif crop_season in ["kharif", "rabi"] and current_season in ["zaid", "both"]:
            score += 10  # Partial match for flexible seasons
        
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
