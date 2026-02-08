# Sales Data Analysis using Pandas

## Objective
The objective of this project is to perform data cleaning and exploratory data analysis (EDA) on a real-world messy sales dataset using Python Pandas and extract meaningful business insights.

## Dataset
The dataset contains 2,823 records and 25 columns related to sales transactions, including:
- Order details  
- Customer information  
- Product categories  
- Sales values  

## Tools Used
- Python  
- Pandas  

## Project Workflow

### 1. Data Loading
Loaded the dataset using Pandas and inspected its structure, data types, and summary statistics.

### 2. Data Cleaning
- Converted column names to lowercase for consistency  
- Converted order date to datetime format  
- Handled missing values using business logic:  
  - addressline2 → "Not Provided"  
  - state → "Unknown"  
  - postalcode → "000000"  

### 3. Adding Columns
Created new analytical features:
- year extracted from order date  
- month extracted from order date  
- revenue calculated as quantityordered × priceeach  

### 4. Output
Exported the cleaned dataset as `cleaned_sales_data.csv` for further analysis or dashboarding.

### 5. Exploratory Data Analysis (EDA)
Key business questions answered:
- Which year generated the highest revenue?  
- Which product line performs best?  
- Which country contributes the most sales?  
- Who are the top 10 customers by revenue?  
- Is there any seasonal trend in monthly sales?  

## Key Insights
- 2004 was the highest revenue year.  
- Classic Cars is the top-performing product category.  
- USA is the largest contributing market.  
- Medium-sized deals generate the highest total revenue.  
- A small group of customers contributes a significant portion of overall sales.  

## Skills Demonstrated
- Data cleaning and preprocessing  
- Feature engineering  
- GroupBy analysis  
- Business-focused data interpretation  
- End-to-end analytics workflow  

## Author
Shivangi Chouhan

