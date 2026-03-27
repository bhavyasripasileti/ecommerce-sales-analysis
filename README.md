<div align="center">

# 📊 E-Commerce Sales Data Analysis

### Transform raw sales data into actionable business intelligence.

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

<br/>

> An end-to-end data analysis project that uncovers sales trends, category performance, regional distribution, and customer demographics from e-commerce data — presented through an interactive, deployment-ready Streamlit dashboard.

<br/>

**[🚀 Live Demo](#-live-app) · [📖 Analysis Overview](#-analysis-performed) · [🐛 Report Bug](../../issues) · [✨ Request Feature](../../issues)**

</div>

---

## 🌐 Live App

> 🔗 **[Click here to explore the dashboard »](https://ecommerce-sales-analysis-cyqc3pcyncscatnogyfxzw.streamlit.app)**


---

## 📋 Table of Contents

- [Overview](#-overview)
- [Objectives](#-objectives)
- [Dataset Description](#-dataset-description)
- [Data Preprocessing](#-data-preprocessing)
- [Analysis Performed](#-analysis-performed)
- [Dashboard Features](#-dashboard-features)
- [Tech Stack](#️-tech-stack)
- [Getting Started](#-getting-started)
- [Deployment](#-deployment)
- [Challenges & Learnings](#-challenges--learnings)
- [Roadmap](#-roadmap)
- [Author](#-author)

---

## 🔍 Overview

This project was developed as part of an **Industry Internship** and demonstrates a complete, production-oriented data analysis workflow — from raw data ingestion and preprocessing through to interactive visualization and cloud deployment.

The goal is to give business stakeholders a clear, visual understanding of e-commerce performance across time, product categories, regions, and customer demographics — enabling faster, data-driven decisions.

---

## 🎯 Objectives

- Analyze historical e-commerce sales data to surface meaningful patterns
- Identify sales trends over time
- Measure category-wise and region-wise performance
- Understand customer age demographics
- Build an interactive, user-friendly dashboard
- Deploy the solution as a publicly accessible web application

---

## 📂 Dataset Description

The dataset is an **E-Commerce Sales Dataset (CSV format)** containing order-level transaction records.

| Column | Description |
|---|---|
| `Order Date` | Date the order was placed |
| `Sales` | Revenue generated per order |
| `Category` | Top-level product category |
| `Sub-Category` | Product sub-category |
| `Region` | Geographic region of the customer |
| `Customer Age` | Age of the customer |

> **Note:** This dataset is used strictly for analytical and academic purposes.

---

## 🔧 Data Preprocessing

| Step | Action Taken |
|---|---|
| Missing Values | Identified and handled null entries |
| Date Formatting | Converted `Order Date` to proper `datetime` format |
| Type Validation | Verified and corrected column data types |
| Performance | Optimized data loading with Streamlit `@st.cache_data` |

---

## 📊 Analysis Performed

### Key Performance Indicators (KPIs)

| KPI | Description |
|---|---|
| 💰 Total Sales | Sum of all revenue across orders |
| 📦 Total Orders | Count of all transactions |
| 📈 Average Sales | Mean revenue per order |

### Deep-Dive Analysis

- **Sales Trend Analysis** — Time-series chart of sales patterns over months/years
- **Category-wise Sales** — Comparative bar charts across product categories
- **Region-wise Distribution** — Regional contribution to total sales
- **Customer Age Distribution** — Histogram of customer demographics

---

## 📈 Dashboard Features

- 📊 Interactive Plotly charts (zoom, hover, filter)
- 🔢 KPI summary metrics displayed prominently at the top
- 🗂 Category and region breakdowns side by side
- 👤 Customer demographic visualizations
- 📱 Clean, responsive layout accessible to non-technical users

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Language | Python 3.9+ |
| Data Manipulation | Pandas |
| Visualization | Plotly Express |
| Dashboard Framework | Streamlit |
| Version Control | Git & GitHub |
| Deployment | Streamlit Cloud |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/your-username/ecommerce-sales-analysis.git
cd ecommerce-sales-analysis
```

**2. (Optional) Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the dashboard**
```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

---

## 🌍 Deployment

This project is deployed on **Streamlit Cloud** for live public access.

To deploy your own instance:

1. Push the repository to GitHub with the following files:
   ```
   ├── app.py
   ├── requirements.txt
   └── your_dataset.csv
   ```
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in
3. Click **New App** and connect your GitHub repository
4. Set the main file path to `app.py`
5. Click **Deploy** — your app goes live in minutes

---

## 🧩 Challenges & Learnings

### Challenges Faced

| Challenge | Resolution |
|---|---|
| Visualization alignment & formatting | Tuned Plotly layout parameters and column widths |
| Histogram clarity for age distribution | Adjusted bin sizes and axis labels for readability |
| Streamlit layout & performance | Applied caching and reorganized component structure |

### Key Learnings

- Hands-on experience with real-world messy data
- Best practices for interactive data visualization
- Building and deploying Streamlit dashboards end-to-end
- Communicating analytical findings to non-technical audiences
- Professional documentation and project presentation

---

## 🗺 Roadmap

- [ ] 🔮 Predictive analytics & sales forecasting module
- [ ] 👥 Customer segmentation (RFM Analysis)
- [ ] 🔌 Real-time data source integration
- [ ] 🔎 Advanced filtering options (date range, category, region)
- [ ] 📤 Export functionality (PDF / CSV reports)

---

## 👤 Author

**Bhavya Sri Pasileti**

> Data Science & AI Enthusiast
> Developed as part of an Industry Internship, demonstrating practical skills in data analysis, visualization, and deployment.

[LinkedIn](https://www.linkedin.com/in/bhavya-sri-pasileti-16565a2a1)

---

<div align="center">

**Found this project useful? Give it a ⭐ — it goes a long way!**

*Built with ❤️ by Bhavya Sri Pasileti*

</div>
