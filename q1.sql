SELECT
    'Hrep' AS legislator_type,
    state,
    lname,
    fname,
    gender,
    birthday
FROM
    HREP
WHERE
    strftime('%m', birthday) = '10'

UNION

SELECT
    'Senator' AS legislator_type,
    state,
    lname,
    fname,
    gender,
    birthday
FROM
    Senator
WHERE
    strftime('%m', birthday) = '10'
ORDER BY
    legislator_type,
    state,
    lname;
