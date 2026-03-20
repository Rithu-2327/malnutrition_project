# Child Malnutrition Risk Predictor

## Project Overview
This project predicts the risk of malnutrition among children under five years old using health and nutrition indicators. A **Random Forest  Classifier** is trained on child nutrition data to classify children as **Low Risk** or **High Risk** for malnutrition. The project includes a **mini web app** built with Streamlit to input indicators and get instant predictions.

---

## Dataset
The dataset contains child nutrition data by country. Key columns:

| Column Name              | Description                                         |
|---------------------------|-----------------------------------------------------|
| Country                   | Name of the country                                 |
| Income Classification     | Country income group                                |
| Severe Wasting            | Percentage of children severely wasted             |
| Wasting                   | Percentage of children wasted                      |
| Overweight                | Percentage of overweight children                  |
| Stunting                  | Percentage of children stunted                     |
| Underweight               | Percentage of underweight children                 |
| U5 Population             | Population of children under 5 (in 1000s)          |

---

## Features and Target

| Type      | Columns Used                                 |
|-----------|----------------------------------------------|
| Features  | Severe Wasting, Wasting, Overweight, Stunting, Underweight |
| Target    | Malnutrition Risk (0 = Low, 1 = High)       |

- **Malnutrition Risk** is created based on thresholds:

| Indicator         | Threshold (Risk = 1)          |
|------------------|-------------------------------|
| Wasting          | > 5%                           |
| Stunting         | > 10%                          |
| Underweight      | > 5%                           |

---

## Model
- **Algorithm:** Random Forest Classifier  
- **Train/Test Split:** 80% train, 20% test  
- **Evaluation Metrics:** Accuracy, Confusion Matrix  

## Mini Web App

Built with Streamlit.

Input fields for Severe Wasting, Wasting, Overweight, Stunting, Underweight (%).

Displays Low / High Malnutrition Risk instantly.

Sample Input / Output
Severe Wasting (%)	Wasting (%)	Overweight (%)	Stunting (%)	Underweight (%)	Predicted Risk
2	6	4	12	5	HIGH
1	3	4	8	2	LOW
---
Installation

Clone the repository.

Install dependencies:
```
pip install -r requirements.txt
```
Run the app:

streamlit run malnutrition_app.py


## License

This project is licensed under the MIT License. See the LICENSE
 file for details.
