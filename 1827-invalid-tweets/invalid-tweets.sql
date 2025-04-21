# Write your MySQL query statement below
SELECT tweet_id FROM Tweets
GROUP BY content
HAVING LENGTH(content) > 15