# **Ethical Reflection: Predictive Model for Resource Allocation**

**Model Context:** The deployed model predicts a patient's **Resource Priority** (Low, Medium, High) based on clinical and biometric features from the Breast Cancer Wisconsin (Diagnostic) Dataset.

**Goal of Reflection:** To identify potential biases in the input data and detail how fairness tools can be used to ensure equitable resource allocation across patient demographics.

## **1\. Potential Biases in the Dataset**

The primary risk of bias stems from the *collection* and *composition* of the original clinical data, which can lead to systematically worse outcomes for certain patient groups when the model is applied to a diverse population.

| Category | Description | Impact on Resource Allocation |
| :---- | :---- | :---- |
| **Demographic Bias (Underrepresented Groups)** | The WDBC dataset primarily originates from a specific hospital in Wisconsin. If its patient population lacks diversity across **race, ethnicity, socioeconomic status, or age**, the model will not generalize well. | The model may systematically produce **false negatives (Medium/Low Priority)** for a severe case belonging to an underrepresented group, leading to *under-allocation* of resources (e.g., delayed imaging, slower specialist referral) compared to the majority group. |
| **Feature Bias (Synthetic Target)** | Our model’s High Priority status is synthetically engineered using mean radius as a proxy for severity. If certain demographics naturally exhibit different average tumor sizes for the same prognosis (due to biological or late-diagnosis factors), the Q3 threshold will unfairly penalize them. | Resource allocation becomes dependent on a feature that may not be equally predictive across all groups, creating a proxy for demographic bias. |
| **Measurement/Reporting Bias** | Data collection standards (e.g., biopsy procedures, equipment calibration) might have varied. If one team or clinic consistently under-reports tumor size, the model trained on this skewed data will inherently mis-prioritize those patients. | Inconsistent data quality translates directly into inconsistent resource prioritization, undermining fairness and reliability. |

## **2\. Mitigating Bias with IBM AI Fairness 360 (AIF360)**

IBM AI Fairness 360 is an open-source library that offers a comprehensive set of metrics for bias detection and algorithms for mitigation. If the company were to deploy this model, AIF360 could be integrated as follows:

### **A. Bias Detection (Measuring Disparity)**

To use AIF360, the company would first need to **augment the dataset** with non-sensitive demographic features (e.g., race, age group, geographic region) if they are available internally.

**Key Metrics Used:**

1. **Disparate Impact (DI):** Measures the ratio of the positive outcome rate (High Priority/Resource Allocation) for the unprivileged group compared to the privileged group.  
   * **Goal:** DI ratio should be close to 1.0 (ideally between 0.8 and 1.2). A ratio below 0.8 would indicate that the unprivileged group is less likely to receive High Priority resources.  
2. **Equal Opportunity Difference (EOD):** Measures the difference in **True Positive Rate (Recall)** between the privileged and unprivileged groups for the High Priority class.  
   * **Goal:** EOD should be close to 0\. This is the most critical metric in this scenario, as a non-zero EOD means the model is better at correctly identifying the "High Priority" cases in one group than another (i.e., higher false negative rate for the underserved group).

### **B. Bias Mitigation (Applying Algorithms)**

AIF360 provides three stages for intervention:

| Stage | Algorithm Example | How it Addresses Resource Allocation Bias |
| :---- | :---- | :---- |
| **Pre-Processing (Before Training)** | **Reweighting:** Assigns weights to the training samples to ensure the classifier has a balanced representation of the high-priority outcome across both privileged and unprivileged groups. | Balances the influence of different demographic groups in the training phase, ensuring the High Priority criteria are learned robustly for everyone. |
| **In-Processing (During Training)** | **Adversarial Debiasing:** Trains a classifier and an adversary network simultaneously. The adversary tries to predict the protected attribute (e.g., race) from the classifier's output, forcing the classifier to learn representations that are independent of the protected attribute. | Ensures that the prediction of High/Medium/Low priority is based purely on clinical factors, not on demographic proxies that might exist in the data. |
| **Post-Processing (After Training)** | **Reject Option Classification (ROC):** Modifies the final prediction for cases where the model is uncertain, pushing predictions for unprivileged groups toward the favorable outcome (High Priority) when the confidence is borderline. | Directly adjusts the resource allocation recommendations to correct for documented systemic disparities without retraining the underlying model. |

