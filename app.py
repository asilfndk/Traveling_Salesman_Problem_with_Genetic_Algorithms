# app.py
from flask import Flask, render_template, request, jsonify
from ga import GeneticAlgorithm
from geopy.distance import geodesic
import random
import copy

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

registered_points = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_points():
    data = request.get_json()
    points = data.get('points', [])
    global registered_points
    registered_points = points
    return jsonify({'message': 'Points saved.'})

@app.route('/distance')
def calculate_distance():
    distance_matrix = []
    for i in range(len(registered_points)):
        distance_matrix.append([])
        for j in range(len(registered_points)):
            distance_matrix[i].append(
                geodesic((registered_points[i]['lat'], registered_points[i]['lng']),
                         (registered_points[j]['lat'], registered_points[j]['lng'])).kilometers
            )
    return jsonify({'distance_matrix': distance_matrix})

@app.route('/genetic_algorithm', methods=['POST'])
def run_genetic_algorithm():
    data = request.form
    population_size = int(data['population_size'])
    iteration_count = int(data['iteration_count'])
    crossover_rate = float(data['crossover_rate'])
    mutation_rate = float(data['mutation_rate'])

    points = [f"Point {i+1}" for i in range(len(registered_points))]
    distance_matrix = []
    for i in range(len(registered_points)):
        distance_matrix.append([])
        for j in range(len(registered_points)):
            distance_matrix[i].append(
                geodesic((registered_points[i]['lat'], registered_points[i]['lng']),
                         (registered_points[j]['lat'], registered_points[j]['lng'])).kilometers
            )

    genetic_algorithm = GeneticAlgorithm(population_size, iteration_count, crossover_rate, mutation_rate, points, distance_matrix)
    best_path, best_fitness = genetic_algorithm.optimize()

    return render_template('result.html', best_path=best_path, best_fitness=best_fitness, registered_points=registered_points)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
