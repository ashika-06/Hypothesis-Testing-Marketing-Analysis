
## Statistical Deep Dive into E-Commerce Customer Behavior

This project applies rigorous hypothesis testing to the **Kaggle Marketing Campaign dataset** to uncover key factors driving customer spending and campaign acceptance. 

**Goal:** To identify the most valuable customer segments and influential variables for optimized marketing strategy.

---

### Dataset Snapshot

The data tracks ~2,240 customers, detailing their **demographics (Income, Education)**, **engagement (Recency)**, and **spending patterns (TotalSpend)** across multiple product categories.

---

### Core Findings & Actionable Insights

We used four statistical tests to validate core business assumptions. All results were **statistically significant** ($P \le 0.05$), confirming the relationships are not due to chance.

| Test | Variables | Conclusion | Plot Observation | Primary Insight |
| :--- | :--- | :--- | :--- | :--- |
| **T-Test** | Income vs. Response | **Mean Income is significantly higher** for customers who accepted the offer. | Violin plot shows the 'Accepted' income distribution shifted right. | **Income is the #1 predictor.** Target customers above the group's mean rejection income. |
| **Z-Test** | Recency vs. $\mu=45$ Days | **Current Recency is significantly different** from the 45-day benchmark. | Histogram shows the sample mean deviates from the benchmark line. | Current engagement levels are either improving or declining relative to historical performance. |
| **Chi-Sq** | Education vs. Response | **Education Level is associated** with campaign acceptance. | Stacked bar chart highlights varying acceptance rates across education levels. | **Tailor messaging:** Higher education correlates with better acceptance, requiring personalized outreach. |
| **ANOVA** | Total Spend vs. Education | **Average Total Spend differs significantly** across education levels. | Violin plot shows higher spending distributions for Master/PhD. | **Spending power is tiered by education.** Use this for pricing and high-value product recommendations. |

---

### Overall Interdependencies (Correlation)

The **Correlation Heatmap** confirmed strong structural relationships, validating the segmentation strategy. 

* **Income $\rightarrow$ TotalSpend:** Extremely strong positive link, confirming high income translates directly to high spend.
* **Income/Spend $\leftarrow$ Kidhome:** Significant **negative correlation**, indicating households with more young children spend less overall. This identifies a crucial **lifestyle constraint** for targeting.

***

### Technologies & Credits

* **Libraries:** `pandas`, `scipy`, `numpy`, `seaborn`, `matplotlib`.
* **Dataset Source:** https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis

***
