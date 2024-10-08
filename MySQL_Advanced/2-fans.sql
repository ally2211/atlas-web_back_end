-- first create a table index on origin and then perform count
CREATE INDEX idx_origin ON metal_bands(origin);
-- now count
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans origin desc;
