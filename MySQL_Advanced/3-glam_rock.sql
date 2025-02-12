-- count years as split - formed
SELECT band_name,
(IFNULL(split, YEAR(CURDATE())) - formed) AS lifespan 
FROM metal_bands
WHERE style = 'Glam rock'
GROUP BY band_name
ORDER BY lifespan desc, band_name desc;