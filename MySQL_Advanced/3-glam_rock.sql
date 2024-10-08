-- now count
SELECT band_name, 
10 as lifespan
FROM metal_bands
WHERE style like '%Glam rock%'
GROUP BY band_name
ORDER BY lifespan desc, band_name desc;