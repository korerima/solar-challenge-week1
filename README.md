# Solar Challenge Week 1 – 10 Academy

Welcome to my submission for the 10 Academy Artificial Intelligence Mastery (AIM) Week 0 Challenge! 
This project explores solar irradiance data from a given dataset to identify regions with the highest potential for solar energy investment. 

---

## Project Objective

Acting as a data analyst for **MoonLight Energy Solutions**, the goal is to:

- Analyze environmental data (solar radiation, temperature, wind, humidity, etc.)
- Clean and profile datasets from 3 countries
- Compare solar metrics across regions
- Deliver insights to support solar installation strategy
- (For later on) Build a Streamlit dashboard to visualize findings

---

## Project Structure
solar-challenge-week1/ 

 ├── .github/workflows/ # GitHub Actions CI pipeline 

 ├── notebooks/ # EDA notebooks for each country 

 │ ├── benin_eda.ipynb 

 │ ├── togo_eda.ipynb 

 │ └── sierra_leone_eda.ipynb 

 ├── data/ # Raw and cleaned datasets (gitignored) 

 ├── requirements.txt # Python dependencies 

 ├── .gitignore 

 ├── README.md 


---

## Getting Started

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/korerima/solar-challenge-week1.git
   cd solar-challenge-week1
2. **Create and activate a virtual environment**
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate (Windows)

3. **Install dependencies**
   pip install -r requirements.txt

4. **Run EDA notebooks**
    Launch Jupyter or VSCode and explore the notebooks in /notebooks.
   
6.  CI/CD
  This project uses GitHub Actions to verify the environment setup. The CI workflow runs on every push to ensure requirements.txt installs correctly and that Python is available.

7. Task Overview
  Task	Description
    Task 1 – Git & Env Setup	Initialized GitHub repo, created environment, setup CI
    Task 2 – Data Profiling & EDA	Performed EDA on solar datasets (Benin, Togo, Sierra Leone)
    Task 3 – Cross-Country Comparison: Compared irradiance metrics across countries
    Later – Dashboard (Optional)	Streamlit dashboard for interactive visualization

9. Sample Visualizations
  Solar irradiance over time (GHI, DNI, DHI)
  Cleaning impact on sensor readings
  Correlation heatmaps
  Bubble charts of GHI vs Temp with RH
  Wind direction histograms
  Country comparisons using boxplots and ANOVA

10. Key Tools & Libraries  
  Python (Pandas, NumPy, Seaborn, Matplotlib)
  Jupyter Notebooks
  Git & GitHub
  GitHub Actions (CI/CD)
  Streamlit (Bonus)
  Scikit-learn & SciPy (for stats & cleaning)

11. Author   
  Samuel Kiros
  10 Academy Cohort, AIM 2025 Week 0 Challenge
