# Grid and Background Plugin for GIMP

**Version:** 1.0.0  
**Website:** [Check our website](https://www.brundisium.org/recursos/plugins)

## Overview
This plugin generates a customizable grid with an optional background layer. It is perfect for creating design templates, guides, and other grid-based layouts. The user can define the grid's thickness, cell size, colors, and choose to include or exclude a background layer.

## Features
- Create grids with customizable thickness and dimensions.
- Define the number of rows and columns.
- Customize grid and background colors.
- Optionally include a background layer.
- Suitable for design templates, grids, or layout guides.

## Installation
> [Download latest release now](https://github.com/NICNE0/gimp-grid-generator/archive/refs/tags/v1.0.0.zip)

1. Find your Plug-in folder by checking  `Preferences > Folders > Plug-ins`:
      - On macOS: `~/Library/Application Support/GIMP/2.10/plug-ins`
      - On Linux: `~/.config/GIMP/2.10/plug-ins`
      - On Windows: `%AppData%\GIMP\2.10\plug-ins`
        
   <img width="623" alt="image" src="https://github.com/user-attachments/assets/ce3d553d-bd07-4d9a-84db-6e99dabe8409" />


2. Save the plugin script `grid_gen.py` into your GIMP plug-ins directory
   
3. Make the script executable by running:
   ```bash
   cd <Your Plug-in directory>
   chmod +x grid_gen.py
   ```
   
4. Restart GIMP.
   
5. The plugin will appear under: `Toolbox > Filters > Custom > Grid Generator`.
   
<a href="default_prompt"><img src="https://github.com/user-attachments/assets/81f029a5-47ff-48f5-9ff1-9da540ed9ebb"  width="480" ></a>
   - **Grid Thickness:** Specify the thickness of the grid lines in pixels.
   - **Columns and Rows:** Define the number of columns and rows.
   - **Grid Color:** Choose the color of the grid lines.
   - **Grid Cell Dimensions:** Set the width and height of each grid cell in pixels.
   - **Background Color:** Select the background layer color (if included).
   - **Include Background:** Enable or disable the background layer.
4. Click "OK" to generate the grid.

## Example Configurations
- **Basic Grid:**
  - Thickness: 2 pixels
  - Columns: 10
  - Rows: 10
  - Grid Color: Black
  - Grid Cell Dimensions: 50 x 50 pixels
  - Background: None

- **Grid with Background:**
  - Thickness: 3 pixels
  - Columns: 5
  - Rows: 5
  - Grid Color: Blue
  - Grid Cell Dimensions: 100 x 100 pixels
  - Background Color: White

## Troubleshooting
- **The plugin doesn’t appear in the menu:**
  - Ensure the script is saved in the correct plug-ins directory.
  - Verify the file is executable (`chmod +x`).
  - Restart GIMP.
- **Error: "Invalid parameter values":**
  - Ensure thickness, width, height, rows, and columns are positive values.

## Contributing
Feel free to contribute by suggesting features or reporting bugs on [GitHub](https://github.com/NICNE0/gimp-grid-generator).

## Licensing and Additional Information

This project is licensed under the MIT License. See the LICENSE file for more details.

You can include additional examples, configurations, or frequently asked questions in this README as the project evolves.
