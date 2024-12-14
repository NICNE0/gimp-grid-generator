#!/usr/bin/env python

"""
Grid and Background Plugin for GIMP

Author: NICNE0
License: MIT
Version: 1.0.0
Website: https://www.brundisium.org/recursos/plugins

Description:
This plugin generates a customizable grid with an optional background layer. 
It is useful for creating design templates, guides, and other grid-based 
layouts. Users can define grid thickness, cell size, colors, and include or 
exclude a background layer.
"""

from gimpfu import *

def create_grid_with_background(thickness, cols, rows, grid_color, grid_width, grid_height, bg_color, include_bg):
    # Validate inputs
    if thickness <= 0 or grid_width <= 0 or grid_height <= 0:
        pdb.gimp_message("Thickness, grid width, and grid height must be positive values.")
        return

    if cols <= 0 or rows <= 0:
        pdb.gimp_message("Number of columns and rows must be positive integers.")
        return

    # Convert parameters to integers where necessary
    thickness = int(thickness)
    rows = int(rows)
    cols = int(cols)
    grid_width = int(grid_width)
    grid_height = int(grid_height)

    # Calculate the full image dimensions
    image_width = grid_width * cols + thickness * (cols + 1)
    image_height = grid_height * rows + thickness * (rows + 1)

    # Create the image
    image = gimp.Image(image_width, image_height, RGB)

    # Add a background layer if needed
    if include_bg:
        bg_layer = gimp.Layer(image, "Background", image_width, image_height, RGB_IMAGE, 100, NORMAL_MODE)
        image.add_layer(bg_layer, -1)  # Ensure the background layer is always at the bottom
        gimp.set_background(bg_color)
        pdb.gimp_drawable_fill(bg_layer, FILL_BACKGROUND)

    # Add the grid layer
    grid_layer = gimp.Layer(image, "Grid", image_width, image_height, RGBA_IMAGE, 100, NORMAL_MODE)
    image.add_layer(grid_layer, 0)
    pdb.gimp_drawable_fill(grid_layer, FILL_TRANSPARENT)  # Make the grid layer transparent
    gimp.set_foreground(grid_color)

    # Draw the grid
    for i in range(rows + 1):  # Include the last row line
        y_start = i * (grid_height + thickness)
        pdb.gimp_rect_select(image, 0, y_start, image_width, thickness, CHANNEL_OP_REPLACE, False, 0)
        pdb.gimp_edit_fill(grid_layer, FILL_FOREGROUND)  # Fill horizontal line

    for j in range(cols + 1):  # Include the last column line
        x_start = j * (grid_width + thickness)
        pdb.gimp_rect_select(image, x_start, 0, thickness, image_height, CHANNEL_OP_REPLACE, False, 0)
        pdb.gimp_edit_fill(grid_layer, FILL_FOREGROUND)  # Fill vertical line

    # Add a border around the entire grid
    pdb.gimp_rect_select(image, 0, 0, image_width, thickness, CHANNEL_OP_REPLACE, False, 0)  # Top border
    pdb.gimp_edit_fill(grid_layer, FILL_FOREGROUND)
    pdb.gimp_rect_select(image, 0, image_height - thickness, image_width, thickness, CHANNEL_OP_REPLACE, False, 0)  # Bottom border
    pdb.gimp_edit_fill(grid_layer, FILL_FOREGROUND)
    pdb.gimp_rect_select(image, 0, 0, thickness, image_height, CHANNEL_OP_REPLACE, False, 0)  # Left border
    pdb.gimp_edit_fill(grid_layer, FILL_FOREGROUND)
    pdb.gimp_rect_select(image, image_width - thickness, 0, thickness, image_height, CHANNEL_OP_REPLACE, False, 0)  # Right border
    pdb.gimp_edit_fill(grid_layer, FILL_FOREGROUND)

    pdb.gimp_selection_none(image)  # Clear the selection

    # Display the image
    display = gimp.Display(image)
    pdb.gimp_displays_flush()

register(
    "python_fu_grid_generator",
    "Create a customizable grid with optional background",
    "This plugin generates a customizable grid with an optional background layer.\n\n"
    "Parameters:\n"
    "- Thickness: Thickness of the grid lines in pixels.\n"
    "- Columns & Rows: Define the number of grid squares horizontally and vertically.\n"
    "- Grid Color: Choose the color of the grid lines.\n"
    "- Grid Cell Dimensions: Set the width and height of each grid cell in pixels.\n"
    "- Background Color: Select the background layer color (if included).\n"
    "- Include Background: Enable or disable the background layer.\n\n"
    "Usage:\n"
    "1. Open the plugin from Toolbox > Filters > Custom > Grid Generator.\n"
    "2. Configure the grid settings and click 'OK' to generate the grid.",
    "NICNE0",
    "MIT",
    "2024",
    "<Toolbox>/Filters/Custom/Grid Generator",
    "",
    [
        (PF_INT, "thickness", "Grid thickness (pixels)", 1),
        (PF_INT, "cols", "Number of columns", 15),
        (PF_INT, "rows", "Number of rows", 10),
        (PF_COLOR, "grid_color", "Grid color", (0, 0, 0)),
        (PF_SPINNER, "grid_width", "Grid cell width (pixels)", 16, (1, 1000, 1)),
        (PF_SPINNER, "grid_height", "Grid cell height (pixels)", 16, (1, 1000, 1)),
        (PF_COLOR, "bg_color", "Background color", (0, 74.5, 74.5)),
        (PF_TOGGLE, "include_bg", "Include background layer", True),
    ],
    [],
    create_grid_with_background
)

main()