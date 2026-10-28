# GlowUp Campaign Performance Analysis

Exploratory data analysis of GlowUp's marketing campaigns to find which channels deliver the best return on marketing spend.

## 📌 Project Objective
GlowUp runs marketing campaigns across four channels: Email, Influencer, Event and Social Media.
This project analyzes campaign spend, revenue, and conversions to answer one question:
**Which channels give the best return for every rupee spent, and where should the marketing budget go next?**

## 📂 Dataset
- **File:** `data/glowup_campaigns.csv`
- **Size:** 30 campaigns × 11 columns
- **Columns:** `CampaignID`, `CampaignName`, `StartDate`, `EndDate`, `Channel`, `Spend`, `LeadsGenerated`, `Conversions`, `RevenueGenerated`, `Clicks`, `Impressions`
- **Note:** Event campaigns have no impression or click data recorded (offline channel), so click-based metrics were calculated only for online channels.

## 🗂️ Project Structure
```
glowup-campaign-analysis/
├── data/
│   └── glowup_campaigns.csv              # Raw campaign dataset
├── notebooks/
│   └── GlowUp_EDA.ipynb                  # EDA, KPI calculation and charts
├── src/
│   └── data_cleaning.py                  # Load & Clean data                              
├── images/                               # Charts used in this README
│   ├── revenue_by_channel.png
│   ├── roi_by_channel.png
│   └── cost_per_conversion_by_channel.png
├── requirements.txt                      # Python dependencies
├── .gitignore
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
4. Run all cells (Kernel → Restart & Run All). Charts are saved to the `images/` folder.

## 📊 Key Analysis & Insights

### 1. Total Revenue by Channel
![Revenue by Channel](images/revenue_by_channel.png)

**Insight:** Events generated the most revenue (₹3.25 lakh, about 63% of the total), but they also consumed about 66% of the total budget. High revenue here comes mainly from high spending, not from efficiency.

### 2. ROI by Channel
![ROI by Channel](images/roi_by_channel.png)

**Insight:** Email delivered the highest ROI at **117.8%**, more than double what it cost, while using only about 4% of the budget. Influencer campaigns returned 36.6% and Events only 10.7%. **Social Media lost money (−39.6% ROI)**, earning back less than it cost.

### 3. Cost per Conversion by Channel
![Cost per Conversion by Channel](images/cost_per_conversion_by_channel.png)

**Insight:** Each Email conversion cost about **₹24.8**, roughly 4× cheaper than Social Media (**₹97.8**). Social Media had the most impressions (16.4 lakh) but the lowest conversion rate from clicks (1.8% vs 6.6% for Email), so its reach isn't turning into customers.

## 💻 Key Code Snippets

**ROI by channel**
```python
channel_summary = df.groupby("Channel")[["Spend", "RevenueGenerated"]].sum()
channel_summary["ROI_%"] = (
    (channel_summary["RevenueGenerated"] - channel_summary["Spend"])
    / channel_summary["Spend"] * 100
)
```

**Funnel metrics (CTR and conversion rate)**
```python
funnel = df.groupby("Channel")[["Impressions", "Clicks", "Conversions"]].sum()
funnel["CTR_%"] = funnel["Clicks"] / funnel["Impressions"] * 100
funnel["Conversion_Rate_%"] = funnel["Conversions"] / funnel["Clicks"] * 100
```

**Cost per conversion**
```python
cost = df.groupby("Channel")[["Spend", "Conversions"]].sum()
cost["Cost_per_Conversion"] = cost["Spend"] / cost["Conversions"]
```

## ✅ Conclusion
Across 30 campaigns, GlowUp spent ₹4.46 lakh and generated ₹5.12 lakh in revenue, an overall ROI of about 14.9%.
Email is the most efficient channel by far, with the highest ROI and the lowest cost per conversion, yet it receives the smallest share of the budget.
Events bring in the most revenue but at a low return, and Social Media is currently losing money.
**Recommendation:** increase investment in Email and Influencer campaigns, review the cost structure of Events, and pause or redesign Social Media campaigns until they become profitable.

## 🚀 Future Scope
- Track impressions and clicks for Event campaigns to compare them fairly with online channels
- Analyze performance over time using `StartDate` and `EndDate` to find the best campaign months and durations
- Use `LeadsGenerated` to study the lead-to-conversion funnel per channel
- Build a budget-allocation model to suggest the best spend mix across channels
- Create an interactive dashboard (Power BI or Streamlit) for the marketing team

## 🛠️ Tools Used
Python · Pandas · Matplotlib · Jupyter Notebook · VS Code · Git & GitHub

## 👤 Author
**Bhagyashree** – [GitHub](https://github.com/Bhagyashree998)