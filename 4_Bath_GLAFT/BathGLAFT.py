import glaft
import matplotlib.pyplot as plt
import os
import pandas as pd
from osgeo import gdal

plt.rcParams.update({'font.size': 20})

# Configuration parameters
BASE_DIR = r""
STATIC_AREA = r'D:\yan1\iceflow\AiceFLOW\polar\058115\newshp\hand0115.shp'
GLAFT_BASE_DIR = os.path.join(BASE_DIR, "0115_bathglaft")

# List to store all results
all_data_list = []

# Process 10 groups of data (1–10)
for i in range(1, 11):
    # Create output directory for the current group
    save_dir = os.path.join(GLAFT_BASE_DIR, f"COSICORR{i}")
    os.makedirs(save_dir, exist_ok=True)

    vx_file = os.path.join(BASE_DIR, f"COSICORR{i}", "day", f"{i}_L820230124_L820231210_Vx.tif")
    vy_file = os.path.join(BASE_DIR, f"COSICORR{i}", "day", f"{i}_L820230124_L820231210_Vy.tif")
    # vx_file = os.path.join(BASE_DIR, f"COSICORR{i}", "day", f"{i}_L920230217_L920231218_Vx.tif")
    # vy_file = os.path.join(BASE_DIR, f"COSICORR{i}", "day", f"{i}_L920230217_L920231218_Vy.tif")

    # Check if files exist
    if not os.path.exists(vx_file) or not os.path.exists(vy_file):
        print(f"Warning: Files not found for group {i}. Skipping...")
        continue

    print(f"\nProcessing group {i}...")

    # Extract file name label
    base_name = os.path.basename(vx_file)
    name_without_ext = os.path.splitext(base_name)[0]
    label = name_without_ext.rsplit("_", 1)[0]

    # Store data for the current group
    group_data_list = []

    # Perform static terrain analysis
    try:
        experiment = glaft.Velocity(vxfile=vx_file, vyfile=vy_file, static_area=STATIC_AREA)
        experiment.static_terrain_analysis()

        # Collect results
        data = {
            'label': label,
            'delta_vx (m/d)': round(experiment.metric_static_terrain_x, 4),
            'delta_vy (m/d)': round(experiment.metric_static_terrain_y, 4),
            'KDE_vx (m/d)': round(experiment.kdepeak_x, 4),
            'KDE_vy (m/d)': round(experiment.kdepeak_y, 4),
            'Incorrect match (%)': round(100 * experiment.outlier_percent, 4)
        }

        # Append to both group list and global list
        group_data_list.append(data)
        all_data_list.append(data)

        # Create DataFrame for the current group
        group_df = pd.DataFrame(group_data_list)

        # Save group results to CSV
        group_csv_path = os.path.join(save_dir, f"{label}_results.csv")
        group_df.to_csv(group_csv_path, index=False)
        print(f"Group {i} results saved to: {group_csv_path}")

        # Plot and save Figure 1
        experiment.plot_full_extent(metric=1)
        plt.figtext(0.5, 0.015, label, ha='center', va='center')
        plt.xlabel('Static area Vx(m/d)')
        plt.ylabel('Static area Vy(m/d)')
        fig1_path = os.path.join(save_dir, f"{label}_figure_1.png")
        plt.savefig(fig1_path)
        # plt.xlim(-0.05, 0.05)  # Correct x-axis limits if needed
        # plt.ylim(-0.045, 0.045)  # Correct y-axis limits if needed
        plt.close()
        print(f"Saved figure 1: {fig1_path}")

        # Plot and save Figure 2
        # Generate zoomed plot (called only once)
        experiment.plot_zoomed_extent(metric=1)

        ax = plt.gca()  # Get current axes

        # # Set symmetric axis limits if needed
        # ax.set_xlim(-0.03, 0.03)
        # ax.set_ylim(-0.03, 0.001)

        # Set axis labels
        ax.set_xlabel('Static area Vx (m/d)')
        ax.set_ylabel('Static area Vy (m/d)')

        # Add figure label
        plt.figtext(0.5, 0.015, label, ha='center', va='center')

        # Add analysis result text
        results_text = (
            f'KDE peak location x: {experiment.kdepeak_x:.4f} (m/d)\n'
            f'KDE peak location y: {experiment.kdepeak_y:.4f} (m/d)\n'
            f'Incorrect match percentage: {100 * experiment.outlier_percent:.4f}%'
        )

        ax.text(0.97, 0.97, results_text,
                horizontalalignment='right',
                verticalalignment='top',
                fontsize=14,
                transform=ax.transAxes)

        fig2_path = os.path.join(save_dir, f"{label}_figure_2.png")
        plt.savefig(fig2_path)
        plt.close()
        print(f"Saved figure 2: {fig2_path}")

    except Exception as e:
        print(f"Error processing group {i}: {str(e)}")

# Save combined results from all groups
if all_data_list:
    # Ensure output directory exists
    os.makedirs(GLAFT_BASE_DIR, exist_ok=True)

    # Create DataFrame for all results
    all_df = pd.DataFrame(all_data_list)

    # Save combined results
    total_csv_path = os.path.join(GLAFT_BASE_DIR, "0115_L8_glaft_batch.csv")
    all_df.to_csv(total_csv_path, index=False)
    print(f"\nAll groups results saved to: {total_csv_path}")

    # Print summary statistics
    print("\nSummary Statistics:")
    print(all_df.describe())
else:
    print("\nNo data processed. Please check input files.")