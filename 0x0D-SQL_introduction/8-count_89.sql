-- displays number of records with id of 89 in the table
-- of the database hbtn_0c_0 in your MySQL server.
-- execute: cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
SELECT count(*) FROM first_table WHERE `id` = 89;

