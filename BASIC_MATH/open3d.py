import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def draw_rect_prism(ax, center, size, color='b'):
    """Draws a rectangular prism centered at `center` with the given `size`."""
    x, y, z = center
    dx, dy, dz = size
    # Vertices of the rectangular prism
    vertices = np.array([
        [x - dx / 2, y - dy / 2, z - dz / 2],
        [x + dx / 2, y - dy / 2, z - dz / 2],
        [x + dx / 2, y + dy / 2, z - dz / 2],
        [x - dx / 2, y + dy / 2, z - dz / 2],
        [x - dx / 2, y - dy / 2, z + dz / 2],
        [x + dx / 2, y - dy / 2, z + dz / 2],
        [x + dx / 2, y + dy / 2, z + dz / 2],
        [x - dx / 2, y + dy / 2, z + dz / 2]
    ])
    
    # Define the six faces of the rectangular prism
    faces = [
        [vertices[j] for j in [0, 1, 2, 3]],  # Bottom
        [vertices[j] for j in [4, 5, 6, 7]],  # Top
        [vertices[j] for j in [0, 1, 5, 4]],  # Front
        [vertices[j] for j in [2, 3, 7, 6]],  # Back
        [vertices[j] for j in [0, 3, 7, 4]],  # Left
        [vertices[j] for j in [1, 2, 6, 5]]   # Right
    ]
    
    # Add the faces to the plot
    ax.add_collection3d(Poly3DCollection(faces, facecolors=color, linewidths=1, edgecolors='r', alpha=.25))

def draw_wheel(ax, center, radius, height, color='k'):
    """Draws a cylindrical wheel using `matplotlib`."""
    x, y, z = center
    # Create a cylinder
    theta = np.linspace(0, 2*np.pi, 30)
    z_cylinder = np.linspace(-height / 2, height / 2, 2)
    theta, z_cylinder = np.meshgrid(theta, z_cylinder)
    
    x_cylinder = radius * np.cos(theta) + x
    y_cylinder = radius * np.sin(theta) + y
    z_cylinder = z_cylinder + z
    
    # Plot the surface
    ax.plot_surface(x_cylinder, y_cylinder, z_cylinder, color=color)

def create_car(ax):
    # Draw car body (rectangular prism)
    draw_rect_prism(ax, center=(0, 0, 0), size=(1.5, 0.6, 0.5), color='b')
    
    # Draw car roof (smaller rectangular prism)
    draw_rect_prism(ax, center=(0, 0, 0.5), size=(0.8, 0.4, 0.3), color='r')
    
    # Draw wheels (4 cylinders)
    wheel_radius = 0.15
    wheel_height = 0.2
    for x in [-0.6, 0.6]:  # Left and right wheels
        for y in [-0.3, 0.3]:  # Front and back wheels
            draw_wheel(ax, center=(x, y, -0.25), radius=wheel_radius, height=wheel_height)

# Main code to create the 3D car and visualize it
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the aspect of the plot to be equal
ax.set_box_aspect([2, 1, 1])  # Aspect ratio of the plot

# Create the car and draw it
create_car(ax)

# Set axis limits
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# Show the plot
plt.show()
