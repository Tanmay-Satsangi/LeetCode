# Write your MySQL query statement below

-- self join 

select w2.id 
from Weather w1, Weather w2
where DateDiff(w2.recordDate, w1.recordDate) = 1 and w2.temperature > w1.temperature
