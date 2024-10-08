-- now count
SELECT band_name, 
isnull(split, year(curdate())) - formed as lifespan
FROM metal_bands
WHERE style = 'Glam rock'
GROUP BY band_name
ORDER BY formed desc, band_name desc;