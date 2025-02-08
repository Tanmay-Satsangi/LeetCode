# Write your MySQL query statement below

-- https://www.youtube.com/watch?v=xtA5_1G0i24

select user_id, 
    CONCAT(UPPER(LEFT(name, 1)), LOWER(RIGHT(name, LENGTH(name) - 1))) as name
from Users
order by user_id
