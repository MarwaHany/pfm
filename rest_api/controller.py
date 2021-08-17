import pandas as pd
from flask import Blueprint, request, jsonify
from product_recommender.recommender import predict


prediction_app = Blueprint("prediction_app", __name__)

@prediction_app.route("/health", methods=["GET"])
def health():
    if request.method == "GET":
        return "Working Fine"

@prediction_app.route("/recommend/products", methods=['POST'])
def get_recommended_products():
    if request.method == 'POST':
        input_data = request.get_json()
        print(input_data)
        predictions = predict(input_data)
        return jsonify({'predictions': predictions})