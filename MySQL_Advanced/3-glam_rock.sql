-- count years as split - formed
SELECT band_name,
(IFNULL(split, YEAR(CURDATE())) - IFNULL(formed, YEAR(CURDATE()) -1)) AS lifespan 
FROM metal_bands
WHERE TRIM(LOWER(style)) LIKE '%glam rock%'
ORDER BY lifespan DESC;
