# Data Scraping and Preprocessing using Python and Scrapy

**Name:** Shaikh Mohammed Wasim  
**Student ID:** 202618007  
**Course:** Fundamentals of Machine Learning  

---

## Project Overview

This project demonstrates a complete data pipeline using Python and Scrapy. Book information was scraped from the **Books to Scrape** website, cleaned and transformed using Pandas, and analyzed through visualizations to identify meaningful patterns in the dataset.

Website used: http://books.toscrape.com/

---

## Objectives

- Scrape book information using Scrapy.
- Extract relevant product details from individual book pages.
- Clean and preprocess the collected data.
- Perform feature engineering.
- Generate visualizations for exploratory data analysis.
- Interpret the results and derive meaningful insights.

---

## Dataset

A total of **200 books** were scraped from the first **10 catalogue pages** of the website.

### Extracted Attributes

- Title
- Category
- Price
- Rating
- Availability
- Product Description
- UPC
- Number of Reviews
- Product URL

---

## Data Preprocessing

The following preprocessing steps were performed:

- Removed duplicate books using UPC.
- Cleaned whitespace and inconsistent text formatting.
- Handled missing product descriptions.
- Converted prices from text to numeric values.
- Converted ratings from text (One–Five) to integers (1–5).
- Extracted the available stock count.
- Converted availability into a binary Yes/No field.

### Engineered Features

- **description_word_count** – Number of words in each book description.
- **price_band** – Price grouped into four categories using quartiles.
- **value_score** – Rating divided by price.
- **affordability_score** – Relative affordability on a scale from 1 (least affordable) to 10 (most affordable).

---

## Visualizations

The following visualizations were created:

- Price Distribution
- Rating Distribution
- Average Price by Category
- Price vs Rating
- Word Cloud of Book Descriptions
- Top 10 Books by Value Score

---

## Project Structure

```
lab_01/
│
├── data/
│   ├── books_raw.csv
│   └── books_clean.csv
│
├── notebook/
│   ├── pre_processing.ipynb
│   ├── visualization.ipynb
│   └── insighs_and_interpretations.ipynb
│
├── plots/
│   ├── average_price_by_category.png
│   ├── price_distribution.png
│   ├── price_vs_rating.png
│   ├── rating_distribution.png
│   ├── top_value_books.png
│   └── wordcloud.png
│
├──scrapy_project/
│   └── spiders/
│       └── book_spider.py
│
├── scrapy.cfg
└── README.md
```

---

## Technologies Used

- Python
- Scrapy
- Pandas
- NumPy
- Matplotlib
- Seaborn
- WordCloud
- Jupyter Notebook

---

## How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
cd lab_01
```

### 2. Install the required libraries

```bash
pip install scrapy pandas numpy matplotlib seaborn wordcloud notebook
```

### 3. Run the Scrapy spider

```bash
scrapy crawl bookspider -O data/books_raw.csv
```

### 4. Run the notebooks

Execute the notebooks in the following order:

1. `pre_processing.ipynb`
2. `visualization.ipynb`
3. `insighs_and_interpretations.ipynb`

---

## Results

The project successfully demonstrates a complete workflow consisting of:

- Web scraping using Scrapy
- Data cleaning and preprocessing
- Feature engineering
- Exploratory data analysis
- Data visualization
- Insight generation

---

## Limitations

- Only the first 10 catalogue pages (200 books) were scraped.
- The website is intended for scraping practice and does not represent a real online bookstore.
- Some product descriptions in the source HTML contain duplicated or truncated text.
- Customer review text is unavailable; therefore, textual analysis is based only on product descriptions.
