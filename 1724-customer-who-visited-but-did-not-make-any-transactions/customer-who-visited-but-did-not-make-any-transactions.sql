# Write your MySQL query statement below
# Select  v.customer_id,COUNT(v.visit_id) as count_no_trans from Visits v left join Transactions t ON v.visit_id = t.visit_id where t.transaction_id is NULL group by v.customer_id;

select v.customer_id, count(v.visit_id) as count_no_trans from Visits v left join Transactions t on v.visit_id  = t.visit_id where t.visit_id is NULL group by v.customer_id;



# Select  v.customer_id,COUNT(v.visit_id) as count_no_trans from Visits v left join Transactions t ON v.visit_id = t.visit_id where t.transaction_id is NULL group by v.visit_id;