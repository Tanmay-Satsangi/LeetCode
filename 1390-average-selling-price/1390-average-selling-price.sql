# Write your MySQL query statement below

-- Use IFNULL() to convert NULL values to 0.

-- Still I did not understand it. 

-- Tricky question if I used where at line 11 then it gives different output.
-- Why They Yield Different Outputs
-- Query 1 returns all products (even those with no sales during the date range) with an average price of 0 if there are no matching sales.
-- Query 2 returns only products with sales in the specified date range, excluding those with no sales, which leads to a different output set.
-- Understanding when the filter is applied (during the join vs. after the join) is key to grasping the difference between these two queries.

select p.product_id, IFNULL(round(sum(u.units * p.price) / sum(u.units), 2), 0) as average_price
from Prices p 
left join UnitsSold u
on p.product_id = u.product_id
and u.purchase_date between p.start_date and p.end_date
group by p.product_id
