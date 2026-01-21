USE sales_project;
SHOW TABLES;
SELECT COUNT(*) FROM sample_superstore;
SELECT * FROM sample_superstore LIMIT 10;

-- Total Sales and Profit
SELECT 
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM sample_superstore;

-- Sales by Category
SELECT 
    Category,
    SUM(Sales) AS Category_Sales
FROM sample_superstore
GROUP BY Category;

-- Monthly Sales Trend
SELECT 
    MONTH(STR_TO_DATE(`Order Date`, '%m/%d/%Y')) AS Month,
    SUM(Sales) AS Monthly_Sales
FROM sample_superstore
GROUP BY Month
ORDER BY Month;

-- Top 10 Products by Profit
SELECT 
    `Product Name`,
    SUM(Profit) AS Total_Profit
FROM sample_superstore
GROUP BY `Product Name`
ORDER BY Total_Profit DESC
LIMIT 10;

DESCRIBE sample_superstore;
