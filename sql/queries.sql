-- =====================================
-- Query 1: Top 5 Funds by AUM
-- =====================================

SELECT
d.scheme_name,
a.aum
FROM fact_aum a
JOIN dim_fund d
ON a.fund_id = d.fund_id
ORDER BY a.aum DESC
LIMIT 5;

-- =====================================
-- Query 2: Average NAV by Fund
-- =====================================

SELECT
d.scheme_name,
ROUND(AVG(n.nav),2) AS avg_nav
FROM fact_nav n
JOIN dim_fund d
ON n.fund_id = d.fund_id
GROUP BY d.scheme_name
ORDER BY avg_nav DESC;

-- =====================================
-- Query 3: Total Transactions Amount by Fund
-- =====================================

SELECT
d.scheme_name,
SUM(t.amount) AS total_amount
FROM fact_transactions t
JOIN dim_fund d
ON t.fund_id = d.fund_id
GROUP BY d.scheme_name
ORDER BY total_amount DESC;

-- =====================================
-- Query 4: Funds with Expense Ratio < 1%
-- =====================================

SELECT
scheme_name,
fund_house,
expense_ratio
FROM dim_fund
WHERE expense_ratio < 1
ORDER BY expense_ratio;

-- =====================================
-- Query 5: Top 10 Funds by 5-Year Return
-- =====================================

SELECT
d.scheme_name,
p.return_5yr
FROM fact_performance p
JOIN dim_fund d
ON p.fund_id = d.fund_id
ORDER BY p.return_5yr DESC
LIMIT 10;

-- =====================================
-- Query 6: Average Returns Across All Funds
-- =====================================

SELECT
ROUND(AVG(return_1yr),2) AS avg_1yr_return,
ROUND(AVG(return_3yr),2) AS avg_3yr_return,
ROUND(AVG(return_5yr),2) AS avg_5yr_return
FROM fact_performance;

-- =====================================
-- Query 7: Number of Schemes per Fund House
-- =====================================

SELECT
fund_house,
COUNT(*) AS total_schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY total_schemes DESC;

-- =====================================
-- Query 8: Number of Schemes by Category
-- =====================================

SELECT
category,
COUNT(*) AS scheme_count
FROM dim_fund
GROUP BY category
ORDER BY scheme_count DESC;

-- =====================================
-- Query 9: Highest NAV Recorded
-- =====================================

SELECT
d.scheme_name,
MAX(n.nav) AS highest_nav
FROM fact_nav n
JOIN dim_fund d
ON n.fund_id = d.fund_id
GROUP BY d.scheme_name
ORDER BY highest_nav DESC
LIMIT 10;

-- =====================================
-- Query 10: Fund-wise AUM Summary
-- =====================================

SELECT
d.scheme_name,
d.fund_house,
a.aum
FROM fact_aum a
JOIN dim_fund d
ON a.fund_id = d.fund_id
ORDER BY a.aum DESC;
