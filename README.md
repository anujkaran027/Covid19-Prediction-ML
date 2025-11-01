# COVID-19 Symptom Prediction App

A simple **Streamlit** web app that predicts whether a person is likely to have COVID-19 based on reported symptoms.  
The model is a **Random Forest** classifier trained on the public *Covid Dataset.csv*.

---

## Local setup

### 1. Clone the repo
```bash
git clone https://github.com/anujkaran027/Covid19-Prediction-ML.git
```

### 2. (Optional) create a virtual environment
```bash
python -m venv venv
# mac & linux
source venv/bin/activate
# Windows 
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the model (only if there is no `model.pkl`)
```bash
python src/model_training.py
```

### 5. Run the app
```bash
streamlit run app.py
```

---

## Exploratory Notebook (Google Colab)

The folder **`notebooks/`** contains a **Google Colab** notebook:

### What the notebook does
| Step | Description |
|------|-------------|
| **Data loading & cleaning** | Same logic as `src/data_cleaning.py` – drops irrelevant columns, label-encodes everything |
| **Visualization** | Uses **`matplotlib`** and **`seaborn`** to plot symptom distributions, correlation heatmaps, and class balance |
| **Model experiments** | Three classifiers were evaluated on a 80/20 train-test split: |
| | • **LogisticRegression** → **97.24 %** accuracy |
| | • **KNeighborsClassifier** → **97.52 %** accuracy |
| | • **RandomForestClassifier** → **98.44 %** accuracy (chosen for the final app) |

> The notebook is fully executable in **Google Colab** – just open the link, upload `data/Covid Dataset.csv`, and run all cells.

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend / UI** | **Streamlit** (`app.py`) |
| **Backend / Prediction** | **Python 3.11**, **NumPy**, **scikit-learn** |
| **Model** | **RandomForestClassifier** (saved as `model.pkl`) |
| **Data processing** | **pandas** |
| **Exploratory analysis** | **Jupyter / Google Colab**, **matplotlib**, **seaborn** |
| **Version control** | **Git** + **GitHub** |
| **Deployment** | **Streamlit Community Cloud** |

---

*All dependencies are listed in `requirements.txt` (only the packages needed for the deployed app).*

---

## Notes
* The dataset is public and does not contain personal identifiers.
* The model is illustrative – not a medical diagnostic tool.