-- count years as split - formed
SELECT band_name,
(IFNULL(split, YEAR(DATE())) - formed) AS lifespan 
FROM metal_bands
WHERE style like '%Glam rock%'
ORDER BY lifespan desc;