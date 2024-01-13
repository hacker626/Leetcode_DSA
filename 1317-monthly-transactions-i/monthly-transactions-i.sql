# Write your MySQL query statement below
# select LEFT(trans_date,7) month,T.country,
# count(T.id) trans_count,
# count(case when state = "approved" then 1 else 0 end) approved_count,sum(T.amount) trans_total_amount,sum(CASE when state = "approved" then amount else 0 end) 
# approved_total_amount
#  from Transactions T 
# group by month,T.country;



SELECT LEFT(T.trans_date, 7) month, T.country, COUNT(T.id) trans_count,
        sum(CASE WHEN state= "approved" THEN 1 ELSE 0 END) approved_count,
        SUM(T.amount) trans_total_amount,
        sum(CASE WHEN state='approved' THEN amount ELSE 0 END) approved_total_amount

FROM Transactions T
GROUP BY month, T.country;
