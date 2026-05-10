# <img width="30" height="30" alt="image" src="https://github.com/user-attachments/assets/cfee9560-55c2-4215-b214-fca0f395340b" />  
# 🛰️ Performance Assessment of Landsat 9 OLI-2 for Glacier Velocity Mapping

[![Python ≥3.8](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)](https://jupyter.org/)
[![COSI-Corr](https://img.shields.io/badge/COSI--Corr-ENVI-green)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Project Overview

Glacier surface velocity is a key parameter for understanding glacier dynamics and ice-sheet mass balance. Launched in September 2021, **Landsat 9** carries the Operational Land Imager-2 (OLI-2) sensor and operates alongside **Landsat 8**, reducing revisit time to 8 days and providing improved radiometric performance.This repository provides a complete and reproducible workflow to:
- Evaluate the radiometric and geolocation performance of Landsat 9 OLI-2  
- Simulated displacement experiment using Landsat 8/9 underfly imagery
- Compare Landsat 8 and Landsat 9 results in real glacier velocity mapping

## Workflow

### 1️⃣ Simulated Displacement Experiments

Folder: `1_Simulated_Image/`

 Generate synthetic displacement fields using Landsat 8/9 underfly imagery [Affine_Transformation.ipynb](https://github.com/GaoYirong/Performance-of-Landsat-9-Operational-Land-Imager-2-OLI-2-for-mapping-glacier-velocity/blob/master/1_Simulated_image/Affine_Transformation.ipynb) and [Simulated_Displacement.ipynb](https://github.com/GaoYirong/Performance-of-Landsat-9-Operational-Land-Imager-2-OLI-2-for-mapping-glacier-velocity/blob/master/1_Simulated_image/Simulated_Displacement.ipynb)
- Calculate the error values of Landsat 8 and Landsat 9 to quantify the impact of radiometric resolution [offset_error_calculation.ipynb](https://github.com/GaoYirong/Performance-of-Landsat-9-Operational-Land-Imager-2-OLI-2-for-mapping-glacier-velocity/tree/master/3_Comparative_Validation/3_1_Error%20Calculation)
---

### 2️⃣ Velocity Extraction

Folder: `2_COSI_Corr/`

Displacement fields are derived using **COSI-Corr** (ENVI plugin).

The workflow includes:

- Image preprocessing  
- Co-registration  
- Subpixel correlation  
- Displacement vector extraction  

Outputs:

- East–West (E–W) displacement  
- North–South (N–S) displacement
- The demo data in [demo data](https://github.com/GaoYirong/Performance-of-Landsat-9-Operational-Land-Imager-2-OLI-2-for-mapping-glacier-velocity/tree/master/2_COSI_Corr)

### 3️⃣ Comparative Validation

Folder: `3_Comparative_Validation/`

This module performs quantitative evaluation including:

- Mean Absolute Error (MAE);Root Mean Square Error(RMSE);Systematic Bias;Percent Difference should be calculate in code: [offset_error_calculation.ipynb](https://github.com/GaoYirong/Performance-of-Landsat-9-Operational-Land-Imager-2-OLI-2-for-mapping-glacier-velocity/blob/master/3_Comparative_Validation/3_1_Error%20Calculation/offset_error_calculation.ipynb)
- Statistical significance tests should be calculate in code:[Difference_Examination.ipynb](https://github.com/GaoYirong/Performance-of-Landsat-9-Operational-Land-Imager-2-OLI-2-for-mapping-glacier-velocity/blob/master/3_Comparative_Validation/3_2_Statistically%20Significant/Difference_Examination.ipynb)
- Five indicators of GLAFT 
---

### 4️⃣ GLAFT-Based Evaluation

Folder: `4_GLAFT_Batch/`
- Stable bedrock masking  
- Kernel Density Estimation (KDE)  
- Batch statistical evaluation  
- Automated accuracy assessment  
**GLAFT (Glacier Feature Tracking Testkit)**
Reference:
Zheng, Whyjay, et al. (2023). GLAcier Feature Tracking testkit (GLAFT): a statistically and physically based framework for evaluating glacier velocity products derived from optical satellite image feature tracking. *The Cryosphere*, 17(9), 4063–4078. https://doi.org/10.5194/tc-17-4063-2023  
---
### Requirements
- Python ≥ 3.8  
- Jupyter Notebook  
- ENVI [COSI-Corr](https://www.tectonics.caltech.edu/slip_history/spot_coseis/download_software.html)

## Author

Email: gaoyr26@mail2.sysu.edu.cn  
School of Geospatial Engineering and Science  
Sun Yat-sen University  

For questions, suggestions, or collaboration, please open an issue or contact the author.

---

_Last updated: May. 10, 2026_
