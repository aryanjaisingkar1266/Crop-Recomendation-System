# 🌾 Crop Recommendation System

A smart agricultural tool that helps farmers make data-driven decisions about which crops to cultivate based on real-time weather conditions, seasonal patterns, and environmental factors.

## 🚀 Features

- **Real-time Weather Integration**: Fetches live weather data for any location
- **Web Interface**: Beautiful, responsive web application for easy access
- **Location-Specific Recommendations**: Different suggestions for different regions
- **Smart Scoring Algorithm**: Ranks crops based on 100-point compatibility score
- **20+ Indian Cities**: Pre-configured weather data for major agricultural regions
- **Command-line & Web**: Use both terminal and web interface

## 🌐 Web Application

The project includes a modern web interface with:
- Clean, gradient-based design
- Real-time weather display
- Interactive crop recommendations
- Mobile-responsive layout
- Smooth animations and transitions

## 📋 Available Crops

The system recommends from 8 common crops:
- **Wheat** (Winter crop) - Best for cooler, drier regions
- **Rice** (Summer crop) - Ideal for high rainfall areas
- **Corn** (Summer crop) - Versatile for moderate conditions
- **Cotton** (Summer crop) - Good for warm climates
- **Potato** (Winter crop) - Prefers cooler temperatures
- **Tomato** (Summer crop) - Moderate rainfall needs
- **Soybean** (Summer crop) - Adaptable to various conditions
- **Barley** (Winter crop) - Cold-tolerant grain

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7+
- pip package manager

Quick Start

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/crop-recommendation-system.git
cd crop-recommendation-system
```

2. **Create virtual environment**:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Run the web application**:
```bash
python app.py
```

5. **Open your browser** and go to `http://localhost:5001`

### Command-line Usage

```bash
python crop_recommendation.py
```

## 📊 How It Works

The system analyzes four key factors:

1. **Temperature Match** (30 points): Current temperature vs crop's optimal range
2. **Rainfall Match** (30 points): Current rainfall vs crop's water requirements  
3. **Wind Conditions** (20 points): Wind speed impact on crop growth
4. **Seasonal Fit** (20 points): Crop's preferred growing season

Each crop receives a score out of 100, with higher scores indicating better suitability.

## � Supported Locations

The system includes pre-configured weather data for major Indian agricultural regions:
- **North India**: Delhi, Punjab, Amritsar, Lucknow, Kanpur
- **West India**: Mumbai, Pune, Ahmedabad, Surat, Rajasthan, Gujarat
- **East India**: Kolkata
- **South India**: Bangalore, Chennai, Hyderabad
- **Central India**: Nagpur, Yavatmal, Indore
- **Northeast**: Nagaland

## 🌤️ Weather API Integration

The system uses OpenWeatherMap API for real-time weather data:
1. **Free API Key**: Sign up at [OpenWeatherMap](https://openweathermap.org/api)
2. **Fallback Data**: Works with pre-configured data if API is unavailable
3. **Error Handling**: Graceful degradation with location-specific defaults

## 📱 Web Application Features

- **Modern UI**: Gradient design with smooth animations
- **Real-time Updates**: Live weather data fetching
- **Mobile Responsive**: Works on all devices
- **Interactive Elements**: Dynamic content loading
- **Weather Cards**: Beautiful display of current conditions
- **Crop Cards**: Detailed recommendations with scores

## 🎯 Example Results

**Punjab** (Cooler, Dry Climate):
```
📍 Location: Punjab
🌡️ Temperature: 24°C
💧 Rainfall: 400mm
🌱 Top Crops: Wheat (100/100), Tomato (100/100), Potato (85/100)
```

**Mumbai** (Coastal, High Rainfall):
```
📍 Location: Mumbai
🌡️ Temperature: 30°C
💧 Rainfall: 2200mm
🌱 Top Crops: Rice (70/100), Corn (70/100), Cotton (70/100)
```

## 🤝 Impact for Farmers

- **Data-Driven Decisions**: Based on real weather conditions
- **Risk Reduction**: Recommends crops suited to current conditions
- **Yield Optimization**: Aligns crops with optimal growing seasons
- **Simple Interface**: Easy for farmers without technical knowledge
- **Cost Effective**: Helps avoid crop failures due to weather mismatch

## 🔧 Technology Stack

- **Backend**: Python with Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **API**: OpenWeatherMap Weather API
- **Data**: Location-specific weather database
- **Design**: Responsive web design with modern UI

## 📈 Future Enhancements

- [ ] More crops and regions
- [ ] Historical weather analysis
- [ ] Crop yield predictions
- [ ] Mobile application
- [ ] Weather alerts system
- [ ] Soil type integration

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

For questions or suggestions, please open an issue on GitHub.
