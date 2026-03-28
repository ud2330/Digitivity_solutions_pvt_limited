---

# Health Insurance Premium Predictor

### Project Overview
This project provides a machine learning solution to estimate annual medical insurance premiums. By analyzing key demographic and lifestyle factors—such as age, BMI, and smoking status—the engine provides an immediate, data-driven cost estimate. This tool is designed to bridge the gap between complex actuarial data and user-friendly financial planning.

---

### Model Evolution & Optimization
To achieve high-precision results, the project followed an iterative development process:

* **Baseline Model (Random Forest):** Our initial implementation reached an accuracy of **88.0%**. This validated the feature set but showed limitations in capturing the non-linear cost spikes associated with high-risk profiles.
* **Optimized Model (XGBoost):** By transitioning to Gradient Boosting (XGBoost) and performing hyperparameter tuning, we improved the accuracy to **~90.1%**. This final model is significantly more robust against outliers and provides more reliable estimates for complex cases.

---

### Performance Metrics

**Accuracy (R² Score): 90.1%** The model successfully explains over 90% of the variance in insurance premiums. In healthcare financial forecasting, this level of accuracy is considered a professional standard for reliability.

**Mean Absolute Error (MAE): ~$2,100** On average, the predicted premium deviates by only $2,100 from the actual cost. This is a narrow margin considering individual premiums in the dataset can exceed $60,000.

**Root Mean Squared Error (RMSE): ~$3,950** This metric confirms the model's stability. The shift to XGBoost specifically helped minimize significant prediction "misses," ensuring more consistent performance across all user profiles.

---

### Key Technical Insights
* **Feature Synergy:** The model excels at identifying how lifestyle choices compound. For instance, the interaction between **Smoking Status** and **High BMI** was identified as the primary driver of premium increases.
* **Scalability:** The engine is built to handle standardized inputs, making it easily integrable into larger insurance platforms or financial dashboards.

---

### Technology Stack
* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-Learn, XGBoost
* **Deployment:** Flask (Web Interface), Joblib (Model Serialization)
* **Environment:** Jupyter Notebook (.ipynb)

---

### How to Run
1. Clone the repository.
2. Ensure `medical_model.pkl` and `scaler.pkl` are in the root directory.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run the application: `python app.py`.

---

> **Project Status:** Deployment Ready  
> **Version:** 1.1 (XGBoost Optimized)  
> **Final Accuracy:** 90.1%
