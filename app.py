from flask import Flask, render_template, request, jsonify
from crop_recommendation import CropRecommender

app = Flask(__name__)
recommender = CropRecommender()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    location = request.form.get('location', 'Delhi')
    recommended_crops, weather_data, current_season = recommender.recommend_crops(location)
    
    return jsonify({
        'location': location,
        'weather': weather_data,
        'season': current_season,
        'crops': recommended_crops
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)
