--  displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(value) as avg_temp FROM hbtn_0c_0.temperatures WHERE month="July" OR month="August" GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
