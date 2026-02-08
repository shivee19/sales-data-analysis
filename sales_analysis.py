import pandas as pd
df =pd.read_csv("sales_data_sample.csv", encoding="latin1")
print(df)
#Step1- load and inspect data
df.head()
print(f'Shape; {df.shape}')
print(f'Column Names; {df.columns}')
print(df.describe())

#Step2- Data Quality check(Mess detection)
#Missing Values
print("\nMissing Values per Column:")
print(df.isnull().sum())

#Duplicates rows
print("\nDuplicates rows",df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

#Step3- Cleaning data
#1.Clean column names
df.columns = df.columns.str.lower()
print(df.columns)

#2.Convert date
df['orderdate'] = pd.to_datetime(df['orderdate'])
print(df['orderdate'].dtypes)

#3.Handling missing values
before = df[['addressline2','state','postalcode']].isnull().sum()

df['addressline2'] = df['addressline2'].fillna("Not Provided")
df['state'] = df['state'].fillna("Unkown")
df['postalcode'] = df['postalcode'].fillna("00000")

after = df[['addressline2','state','postalcode']].isnull().sum()
print("Before Clean:\n", before)
print("\nAfter clean:\n", after)

#4. Add new Columns
df['year'] = df['orderdate'].dt.year
df['month'] = df['orderdate'].dt.month
df['revenue'] = df['quantityordered'] * df['priceeach']

print(df.head())
print(df.describe())
print(df[['year','month','revenue']].sample(5))

#Step5- Save clean data
df.to_csv("cleaned_sales_data.csv", index=False)

#Step6- Explore data analysis
print(df.shape)
print(df.columns)

#Total Revenue by Year
revenue_by_year = df.groupby('year')['revenue'].sum()
print(revenue_by_year)

#Monthly Sales Trend
monthly_sales = df.groupby('month')['revenue'].sum()
print(monthly_sales)

#Top 10 Customers
top_customers = df.groupby('customername')['revenue'].sum().sort_values(ascending=False).head(10)
print(top_customers)

#Best Selling Product line
product_preformance = df.groupby('productline')['revenue'].sum().sort_values(ascending=False)
print(product_preformance)

#Country-wise Revenue
country_sales = df.groupby('country')['revenue'].sum().sort_values(ascending=False)
print(country_sales)

#Deal Size Impact
deal_revenue = df.groupby('dealsize')['revenue'].sum()
print(deal_revenue)




