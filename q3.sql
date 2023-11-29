SELECT
    state,
    COUNT(*) AS num_representatives
FROM
    HREP
GROUP BY
    state
HAVING
    num_representatives >= 10
ORDER BY
    num_representatives DESC;
