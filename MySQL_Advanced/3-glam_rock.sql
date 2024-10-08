-- now count
SELECT band_name, 
(split - formed) as lifespan
FROM metal_bands
WHERE style = 'Glam rock'
GROUP BY band_name
ORDER BY lifespan desc, band_name desc;