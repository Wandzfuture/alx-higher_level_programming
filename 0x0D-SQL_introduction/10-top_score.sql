-- lists all records of second_table ordered by
-- score of the database of MySQL server
-- execute: cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT score, name FROM second_table ORDER BY score DESC;
