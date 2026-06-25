-- =====================================
-- Query 1: Top 5 Funds by AUM
-- =====================================

SELECT
    d.scheme_name,
    d.fund_house,
    a.aum
FROM fact_aum a
JOIN dim_fund d
ON a.fund_id = d.fund_id
ORDER BY a.aum DESC
LIMIT 5;


-- =====================================
-- Query 2: Average NAV Per Month
-- =====================================

SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav),2) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- =====================================
-- Query 3: SIP YoY Growth
-- =====================================

SELECT
    month,
    yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;


-- =====================================
-- Query 4: Transactions by State
-- =====================================

SELECT
    state,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount),2) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;


-- =====================================
-- Query 5: Funds with Expense Ratio < 1%
-- =====================================

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- =====================================
-- Query 6: Top 10 Funds by 5-Year Return
-- =====================================

SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- =====================================
-- Query 7: Number of Schemes by Fund House
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
    sub_category,
    COUNT(*) AS scheme_count
FROM dim_fund
GROUP BY sub_category
ORDER BY scheme_count DESC;


-- =====================================
-- Query 9: Top 10 Portfolio Holdings by Weight
-- =====================================

SELECT
    stock_name,
    sector,
    weight_pct
FROM portfolio_holdings
ORDER BY weight_pct DESC
LIMIT 10;


-- =====================================
-- Query 10: Category-wise Net Inflows
-- =====================================

SELECT
    category,
    ROUND(SUM(net_inflow_crore),2) AS total_inflow
FROM category_inflows
GROUP BY category
ORDER BY total_inflow DESC;