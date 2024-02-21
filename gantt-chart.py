import cv2
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def image_to_point_cloud(image_path, scale_factor=0.01):
    # Read the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Get image dimensions
    height, width = img.shape

    # Create arrays to store point cloud data
    points = []
    intensities = []

    # Iterate through each pixel
    for y in range(height):
        for x in range(width):
            # Get intensity value (pixel value)
            intensity = img[y, x]

            # Calculate 3D coordinates from pixel coordinates
            z = intensity * scale_factor
            points.append([x, y, z])
            intensities.append(intensity)

    return np.array(points), np.array(intensities)

def export_ply(points, intensities, output_file):
    with open(output_file, 'w') as f:
        # Write PLY header
        f.write("ply\n")
        f.write("format ascii 1.0\n")
        f.write("element vertex {}\n".format(len(points)))
        f.write("property float x\n")
        f.write("property float y\n")
        f.write("property float z\n")
        f.write("property uchar red\n")
        f.write("property uchar green\n")
        f.write("property uchar blue\n")
        f.write("end_header\n")

        # Write point cloud data
        for i in range(len(points)):
            x, y, z = points[i]
            intensity = intensities[i]
            # Normalize intensity to [0, 255] for color
            intensity = np.clip(intensity, 0, 255)
            red = green = blue = intensity
            f.write("{} {} {} {} {} {}\n".format(x, y, z, red, green, blue))

if __name__ == "__main__":
    image_path = "me.jpg"
    output_ply_file = "me.ply"
    scale_factor = 0.01  # Adjust this factor to scale the z-coordinate

    points, intensities = image_to_point_cloud(image_path, scale_factor)
    export_ply(points, intensities, output_ply_file)
    print("Point cloud saved to:", output_ply_file)
