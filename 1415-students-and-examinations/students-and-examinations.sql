# # Write your MySQL query statement below
# select 
# st.student_id,
# st.student_name,
# e.subject_name,
# count(e.subject_name)
#  as attended_exams from Students st join Subjects su left join Examinations e on st.student_id = e.student_id and su.subject_name = e.subject_name 
# group by st.student_id,su.subject_name 
# order by student_id asc,subject_name asc;


SELECT
    Students.student_id,
    Students.student_name,
    Subjects.subject_name,
    COUNT(Examinations.subject_name) AS attended_exams
FROM Students
JOIN Subjects
LEFT JOIN Examinations
ON Students.student_id = Examinations.student_id
AND Subjects.subject_name = Examinations.subject_name
GROUP BY Students.student_id, Subjects.subject_name
ORDER BY student_id ASC, subject_name ASC