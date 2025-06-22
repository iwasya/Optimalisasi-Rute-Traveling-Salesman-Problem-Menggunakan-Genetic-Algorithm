import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# === STEP 1: Load dataset tanpa header ===
file_path = r'C:\Users\ACER\Downloads\AG TSP\medium (1).csv'  # sesuaikan path ini
data = pd.read_csv(file_path, header=None)
data.columns = ['x', 'y']  # beri nama kolom manual
coords = data[['x', 'y']].values
num_cities = len(coords)

# === STEP 2: Hitung jarak antar kota (Euclidean) ===
def calc_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i, j] = np.linalg.norm(coords[i] - coords[j])
    return dist_matrix

distance_matrix = calc_distance_matrix(coords)

# === STEP 3: Hitung total jarak dari rute ===
def route_distance(route):
    dist = 0
    for i in range(len(route) - 1):
        dist += distance_matrix[route[i], route[i+1]]
    dist += distance_matrix[route[-1], route[0]]  # kembali ke kota awal
    return dist

# === STEP 4: Inisialisasi populasi acak ===
def init_population(pop_size, num_cities):
    return [list(np.random.permutation(num_cities)) for _ in range(pop_size)]

# === STEP 5: Seleksi tournament ===
def tournament_selection(population, fitnesses, k=3):
    selected = random.sample(list(zip(population, fitnesses)), k)
    selected.sort(key=lambda x: x[1])
    return selected[0][0]

# === STEP 6: Ordered Crossover ===
def ordered_crossover(parent1, parent2):
    size = len(parent1)
    child = [None]*size
    start, end = sorted(random.sample(range(size), 2))
    child[start:end+1] = parent1[start:end+1]
    fill_pos = (end + 1) % size
    parent2_pos = (end + 1) % size
    while None in child:
        if parent2[parent2_pos] not in child:
            child[fill_pos] = parent2[parent2_pos]
            fill_pos = (fill_pos + 1) % size
        parent2_pos = (parent2_pos + 1) % size
    return child

# === STEP 7: Mutasi dengan swap ===
def swap_mutation(route, mutation_rate):
    route = route.copy()
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]
    return route

# === STEP 8: Genetic Algorithm Utama ===
def genetic_algorithm(pop_size=100, generations=500, mutation_rate=0.02):
    population = init_population(pop_size, num_cities)
    best_route = None
    best_distance = float('inf')
    fitness_history = []
    
    for gen in range(generations):
        fitnesses = [route_distance(ind) for ind in population]
        gen_best_distance = min(fitnesses)
        gen_best_route = population[fitnesses.index(gen_best_distance)]
        
        if gen_best_distance < best_distance:
            best_distance = gen_best_distance
            best_route = gen_best_route
        
        fitness_history.append(best_distance)
        
        new_population = []
        for _ in range(pop_size):
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)
            child = ordered_crossover(parent1, parent2)
            child = swap_mutation(child, mutation_rate)
            new_population.append(child)
        
        population = new_population
        
        if (gen+1) % 50 == 0 or gen == 0:
            print(f"Generasi {gen+1}: Jarak terbaik = {best_distance:.4f}")
    
    return best_route, best_distance, fitness_history

# === STEP 9: Jalankan Algoritma ===
best_route, best_distance, fitness_history = genetic_algorithm()

# === STEP 10: Visualisasi Rute Terbaik ===
def plot_route(coords, route):
    plt.figure(figsize=(10,6))
    route_coords = coords[route + [route[0]]]  # kembali ke awal
    plt.plot(route_coords[:, 0], route_coords[:, 1], 'o-', color='blue')
    for i, (x, y) in enumerate(coords):
        plt.text(x, y, str(i), fontsize=8, color='red')
    plt.title(f'Rute Terbaik dengan Total Jarak: {best_distance:.4f}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

plot_route(coords, best_route)

# === STEP 11: Visualisasi Konvergensi Fitness ===
plt.figure(figsize=(10,4))
plt.plot(fitness_history, color='green')
plt.title('Konvergensi Fitness (Jarak Terbaik per Generasi)')
plt.xlabel('Generasi')
plt.ylabel('Jarak Terbaik')
plt.grid(True)
plt.tight_layout()
plt.show()

# Visualisasi titik kota sebelum dijalankan GA
plt.figure(figsize=(6,6))
plt.scatter(coords[:, 0], coords[:, 1], color='orange')
for i, (x, y) in enumerate(coords):
    plt.text(x, y, str(i), fontsize=8)
plt.title('Peta Kota (Sebelum GA)')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.tight_layout()
plt.show()
