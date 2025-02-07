# Write your MySQL query statement below

-- I take 29 instead of 30 because 30th is not inclusive.

select activity_date as day, count(distinct user_id) as active_users
from Activity
where activity_date between DATE_SUB("2019-07-27", INTERVAL 29 DAY) and "2019-07-27"
group by activity_date
