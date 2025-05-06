import numpy as np
import open3d as o3d

# Load XYZ coordinates
xyz = np.load('/home/arghya/isaacsim/generated_synthetic_data/pointcloud_0006.npy')  # Update path

# Load RGBA colors
rgba = np.load('/home/arghya/isaacsim/generated_synthetic_data/pointcloud_rgb_0006.npy')  # Update path

print(f"XYZ shape: {xyz.shape}")
print(f"RGBA shape: {rgba.shape}")

# Ensure both arrays have the same length
assert xyz.shape[0] == rgba.shape[0], "XYZ and RGBA arrays have different lengths."

# Normalize RGB (ignore alpha) from [0,255] to [0,1]
rgb = rgba[:, :3] / 255.0

# Create Open3D point cloud
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(xyz)
pcd.colors = o3d.utility.Vector3dVector(rgb)

# Visualize
o3d.visualization.draw_geometries([pcd])

