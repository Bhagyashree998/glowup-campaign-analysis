# GlowUp Campaign Performance Analysis

## 📌 Project Objective
[1–3 sentences. What question are you answering, and why does it matter?
Example: Analyze GlowUp's marketing campaign data to identify which channels and
campaign types drive the highest conversions and revenue, so the marketing team
can allocate budget more effectively.]

## 📂 Dataset
- **Source:** [where the data came from, e.g. provided as part of a course / Kaggle link]
- **Size:** [e.g. 5,000 rows × 12 columns]
- **Key columns:** [e.g. campaign_id, channel, spend, impressions, clicks, conversions, revenue]

## 🗂️ Project Structure
```
glowup-campaign-analysis/
├── data/
│   └── glowup_campaigns.csv      # Raw campaign dataset
├── notebooks/
│   └── GlowUp_EDA.ipynb          # Full exploratory data analysis
├── src/
│   └── data_cleaning.py          # Reusable loading & cleaning functions
├── images/                       # Saved charts used in this README
├── requirements.txt              # Python dependencies
└── README.md
```

## ▶️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Bhagyashree998/glowup-campaign-analysis.git
   cd glowup-campaign-analysis
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Open the notebook:
   ```bash
   jupyter notebook notebooks/GlowUp_EDA.ipynb
   ```
4. Run all cells (Kernel → Restart & Run All).

## 📊 Key Analysis & Insights

### 1. [Chart title, e.g. Revenue by Channel]
![Revenue by Channel](images/revenue_by_channel.png)

**Insight:** [1–2 sentences on what the chart shows and why it matters.
Example: Instagram generated 42% of total revenue despite receiving only 25% of spend,
making it the most cost-efficient channel.]

### 2. [Chart title]
![Chart 2](images/conversion_rate_by_month.png)

**Insight:** [Your finding.]

### 3. [Chart title]
![Chart 3](images/correlation_heatmap.png)

**Insight:** [Your finding.]

## 💻 Key Code Snippets

**Data cleaning**
```python
df = df.drop_duplicates()
df["revenue"] = df["revenue"].fillna(0)
df["date"] = pd.to_datetime(df["date"])
```

**Calculating conversion rate / ROI by channel**
```python
channel_summary = df.groupby("channel").agg(
    total_spend=("spend", "sum"),
    total_revenue=("revenue", "sum")
)
channel_summary["ROI"] = channel_summary["total_revenue"] / channel_summary["total_spend"]
```

## ✅ Conclusion
[3–5 sentences summarizing the most important findings and what action they suggest.
Example: Social media channels outperformed email and display ads on ROI.
Campaign performance peaked in festive months. Budget should be shifted toward
high-ROI channels and seasonal timing.]

## 🚀 Future Scope
- [e.g. Build a predictive model to forecast campaign conversions]
- [e.g. Create an interactive dashboard using Power BI / Streamlit]
- [e.g. A/B test campaign creatives to measure impact more precisely]
- [e.g. Include customer demographic data for segmentation]

## 🛠️ Tools Used
Python · Pandas · NumPy · Matplotlib · Seaborn · Jupyter Notebook

## 👤 Author
**Bhagyashree** – [GitHub](https://github.com/Bhagyashree998)