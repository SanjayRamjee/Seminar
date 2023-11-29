SELECT
    state || '|' || lname || '|' || fname || '|' || round((julianday('now') - julianday(birthday))/365.25, 0) AS result
FROM
    Senator
WHERE
    round((julianday('now') - julianday(birthday))/365.25,0) < 50
ORDER BY
    round((julianday('now') - julianday(birthday))/365.25,0)ASC;
