-- Counts for Senate
SELECT
    'Senate' AS legislator_type,
    gender,
    COUNT(*) AS count
FROM
    Senator
GROUP BY
    legislator_type,
    gender

UNION

-- Counts for House of Representatives
SELECT
    'HREP' AS legislator_type,
    gender,
    COUNT(*) AS count
FROM
    HREP
GROUP BY
    legislator_type,
    gender;
