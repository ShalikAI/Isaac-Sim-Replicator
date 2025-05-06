import numpy as np
import open3d as o3d

# Load point cloud data from .npy file
points = np.load('/home/arghya/isaacsim/generated_synthetic_data/pointcloud_0006.npy')  # Update this path accordingly

# Check the shape of your data
print(f"Point cloud shape: {points.shape}")

# If your data contains only XYZ coordinates (Nx3)
if points.shape[1] == 3:
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)

# If your data contains XYZ + RGB (Nx6)
elif points.shape[1] == 6:
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points[:, :3])
    pcd.colors = o3d.utility.Vector3dVector(points[:, 3:6] / 255.0)  # Normalize RGB values

# Visualize the point cloud
o3d.visualization.draw_geometries([pcd])
