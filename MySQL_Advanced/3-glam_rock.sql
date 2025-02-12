-- count years as split - formed
SELECT band_name,
isnull(ABS(split - formed), 0) as lifespan
FROM metal_bands
WHERE style = 'Glam rock'
GROUP BY band_name
ORDER BY lifespan desc, band_name desc;