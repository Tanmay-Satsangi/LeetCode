# Write your MySQL query statement below

-- select e.student_id, student_name, subject_name, COUNT(e.subject_name)
-- from Students s
-- CROSS JOIN Examinations e
-- on s.student_id = e.student_id
-- group by e.student_id, student_name, e.subject_name
-- order by e.student_id, e.subject_name


select s.student_id, s.student_name, sub.subject_name, count(e.subject_name) as attended_exams
from Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e
on s.student_id = e.student_id and sub.subject_name = e.subject_name
group by s.student_id, s.student_name, sub.subject_name
order by s.student_id, sub.subject_name






