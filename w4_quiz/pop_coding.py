import pickle
import numpy as np

with open('pop_coding_3.4.pickle', 'rb') as f:
    data = pickle.load(f)

def compute_weightedVec(responses, codings):
    vec = []
    for response, coding in zip(responses, codings):
        normalized_response = response / response.max()
        mean_vec = np.outer(normalized_response, coding).mean(axis=0)
        mean_vec /= np.linalg.norm(mean_vec)  # Normalization
        vec.append(mean_vec)
    return vec

def compute_popVec(basis_vec):
    pop_vec = np.nansum(basis_vec, axis=0)
    pop_vec /= np.linalg.norm(pop_vec)
    return pop_vec

def polar(vec):
    # Convert Cartesian to polar coordinates.
    return np.arctan2(vec[1], vec[0])

responses = [data[key] for key in ['r1', 'r2', 'r3', 'r4']]
codings = [data[key] for key in ['c1', 'c2', 'c3', 'c4']]

basisVec = compute_weightedVec(responses, codings)
basisVec = [vec for vec in basisVec if not np.isnan(vec).any()] # check NaN

popVec = compute_popVec(basisVec)

print('Weighted basis vectors:', basisVec)
print('Population Vector (X, Y):', popVec)

polar_angle = polar(popVec)
print('Population vector in polar coordinates (rad):', polar_angle)
