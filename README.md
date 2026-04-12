# <img width="25" height="25" alt="image" src="https://github.com/user-attachments/assets/cfee9560-55c2-4215-b214-fca0f395340b" />  Performance of Landsat 9 OLI-2 for Mapping Glacier Velocity 

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![COSI-Corr](https://img.shields.io/badge/COSI--Corr-ENVI-green.svg)]()
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


## 📖Contents

* [📌 Objective](#-objective)
* [🧩 Repository Structure](#-repository-structure)
* [🛠️ Modules](#️-modules)

  * [1️⃣ Simulated image](#1️⃣-simulated-image-generation)
  * [2️⃣ Displacement Extraction](#2️⃣-displacement-extraction)
  * [3️⃣ Comparative Validation](#3️⃣-comparative-validation)
  * [4️⃣ GLAFT Batch Processing](#4️⃣-glaft-batch-processing)
* [📦 Dependencies](#-dependencies)
* [🚀 Quick Start](#-quick-start)
* [📄 License](#-license)
* [✉️ Contact](#️-contact)

---

## 📌 Objective

Glacier surface velocity is a key parameter for understanding glacier dynamics and ice-sheet mass balance.Launched in September 2021, **Landsat 9 OLI-2** operates alongside Landsat 8, reducing revisit time to **8 days** and providing the first **14-bit radiometric resolution** in the Landsat series.

This repository provides:

* 🔬 **Simulated displacement experiments** using Landsat 8/9 underfly imagery
* 🧊 **Real glacier velocity retrievals** (Greenland & Antarctica)
* 📊 **Quantitative accuracy assessment** (radiometric & geometric performance)

> 📖 **Key findings**
>
> * Landsat 8 & 9 show strong consistency (**MAE < 0.95 m**)
> * Landsat 9 improves accuracy by **0.46%–2.81%** under extreme radiance
> * Exhibits improved coregistration stability

---

## 🧩 Repository Structure

```bash
.
├── 1_Simulated_Image/
│   ├── Simulated_Displacement.ipynb
│   └── Affine_Transformation.ipynb
├── 2_COSI_Corr/
│   ├── Simulated_Displacement_Corr/
│   └── Glacier_Displacement_Corr/
├── 3_Comparative_Validation/
│   ├── Error_Calculation.ipynb
│   └── Statistical_Significance.ipynb
├── 4_GLAFT_Batch/
│   └── GLAFT_Batch_Processing.ipynb
├── data/
├── results/
└── README.md
```

---

## 🛠️ Modules

### 1️⃣ Simulated image

📂 Folder: [`1_Simulated_Image`](./1_Simulated_Image)

| Notebook                                                                           | Description                                                    |
| ---------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| [`Simulated_Displacement.ipynb`](https://github.com/GaoYirong/Performance-of-Landsat-9-Operational-Land-Imager-2-OLI-2-for-mapping-glacier-velocity/blob/master/1_Simulated_image/Simulated_Displacement.ipynb) | Generate 2D sinusoidal displacement field                      |
| [`Affine_Transformation.ipynb`](./1_Simulated_Image/Affine_Transformation.ipynb)   | Apply displacement using affine transform + sinc interpolation |

🎯 **Purpose**
Isolate the impact of **radiometric resolution** under ideal conditions (no atmosphere / no geolocation error)

---

### 2️⃣ Displacement Extraction

📂 Folder: [`2_COSI_Corr`](./2_COSI_Corr)

* Simulated image pairs → [`Simulated_Displacement_Corr`](./2_COSI_Corr/Simulated_Displacement_Corr)
* Real glacier image pairs → [`Glacier_Displacement_Corr`](./2_COSI_Corr/Glacier_Displacement_Corr)

⚙️ Processed using **COSI-Corr (ENVI plugin)**

Key parameters:

* Initial window size
* Final window size
* Step size
* SNR threshold

🎯 **Purpose**
Extract **E–W and N–S displacement components**

---

### 3️⃣ Comparative Validation

📂 Folder: [`3_Comparative_Validation`](./3_Comparative_Validation)

| Notebook                                                                                      | Description                     |
| --------------------------------------------------------------------------------------------- | ------------------------------- |
| [`Error_Calculation.ipynb`](./3_Comparative_Validation/Error_Calculation.ipynb)               | MAE, RMSE, Bias, Percent Change |
| [`Statistical_Significance.ipynb`](./3_Comparative_Validation/Statistical_Significance.ipynb) | Two-sample t-test               |

🎯 **Purpose**
Quantify and statistically validate performance differences

---

### 4️⃣ GLAFT Batch Processing

📂 Folder: [`4_GLAFT_Batch`](./4_GLAFT_Batch)

| Notebook                                                                       | Description                           |
| ------------------------------------------------------------------------------ | ------------------------------------- |
| [`GLAFT_Batch_Processing.ipynb`](./4_GLAFT_Batch/GLAFT_Batch_Processing.ipynb) | Batch evaluation using improved GLAFT |

Based on **GLAFT (Zheng et al., 2023)**

Includes:

* Kernel Density Estimation (KDE)
* Stable bedrock filtering
* Batch accuracy evaluation

🎯 **Purpose**
Automated large-scale accuracy assessment

---

## 📦 Dependencies

### Core

* Python ≥ 3.8
* Jupyter Notebook


### Python Packages

```bash
numpy
scipy
matplotlib
pandas
scikit-learn
gdal
```

## 🚀 Quick Start

### 1️⃣ Clone repository

```bash
git clone https://github.com/yourusername/Performance-of-Landsat-9-Operational-Land-Imager-2-OLI-2-for-mapping-glacier-velocity.git
cd Performance-of-Landsat-9-Operational-Land-Imager-2-OLI-2-for-mapping-glacier-velocity
```

---

### 2️⃣ Prepare data

Download Landsat imagery from USGS:

👉 https://earthexplorer.usgs.gov/

Place data into:

```
/data
```

---

### 3️⃣ Run simulation

```bash
1_Simulated_Image/Simulated_Displacement.ipynb
1_Simulated_Image/Affine_Transformation.ipynb
```

---

### 4️⃣ Run COSI-Corr

* Use ENVI GUI
* Export results as GeoTIFF / ENVI format
* Save into:

```
/results
```

---

### 5️⃣ Compute statistics

```bash
3_Comparative_Validation/Error_Calculation.ipynb
3_Comparative_Validation/Statistical_Significance.ipynb
```

---

### 6️⃣ Run GLAFT evaluation

```bash
4_GLAFT_Batch/GLAFT_Batch_Processing.ipynb
```

---


## 📄 License

This project is licensed under the MIT License
📎 See [`LICENSE`](./LICENSE)

---
    
## 📄 Reference
Zheng, Whyjay, et al. "GLAcier Feature Tracking testkit (GLAFT): a statistically and physically based framework for evaluating glacier velocity products derived from optical satellite image feature tracking." The Cryosphere 17.9 (2023): 4063-4078.[https://doi.org/10.5194/tc-17-4063-2023](https://doi.org/10.5194/tc-17-4063-2023)


## ✉️ Contact

📧 [gaoyr26@mail2.sysu.edu.cn](mailto:gaoyr26@mail2.sysu.edu.cn)
🏫 School of Geospatial Engineering and Science, Sun Yat-sen University

If you have any questions, suggestions, or would like to collaborate, please open an issue or contact the maintainer of this repository.

---

_Last updated: Apr. 12, 2026_
---
