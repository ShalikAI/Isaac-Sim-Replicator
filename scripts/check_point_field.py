import numpy as np

points = np.load('/home/arghya/isaacsim/generated_synthetic_data/pointcloud_0000.npy')  # update this path

print(f"Shape of the point cloud: {points.shape}")
print(f"Number of fields per point: {points.shape[1]}")

# Inspect first 5 points for clarity
print("First 5 points:")
print(points[:5])
