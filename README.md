# 🏡 California Housing Price Prediction 

An end-to-end Machine Learning project predicting real estate property values (`log_price`) over **74,111 listings** using robust preprocessing and advanced gradient boosting frameworks (XGBoost, LightGBM, CatBoost). Includes an interactive Plotly Dash visualization app.

**Live Space:** https://huggingface.co/spaces/hellosara/California_Housing_Dash

<img width="1334" height="573" alt="image" src="https://github.com/user-attachments/assets/e1a98e57-9964-4be4-9533-a7e1f97a2c09" />
<img width="1336" height="592" alt="image" src="https://github.com/user-attachments/assets/0de8b7c2-9bb5-44af-a5e1-a7cd467c3825" />

---

### 📂 Repository Structure
```bash
california_housing_project/
├── plotly_dash_app/          # Interactive UI Application
│   ├── assets/ & pages/      # Styling assets and multi-page configurations
│   └── app.py                # Main deployment application entrypoint
├── 1-Exploratory_Data_Analysis.ipynb
├── 2-Model_Training_Benchmarking.ipynb
└── README.md

# 1. Clone & Navigate
git clone [https://github.com/Latrechesara/california_housing_project.git](https://github.com/Latrechesara/california_housing_project.git)
cd california_housing_project

# 2. Setup Environment
pip install -r requirements.txt

# 3. Spin up Dashboard locally
cd plotly_dash_app
python app.py

Application runs instantly at: http://127.0.0.1:8050/

👩‍💻 Author
Sara Latreche — Data Scientist & Technical Curriculum Designer
