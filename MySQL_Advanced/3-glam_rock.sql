-- List Glam rock bands ranked by their longevity
SELECT band_name, 
       CASE 
         WHEN split = 'now' THEN 0
         ELSE CAST(split AS SIGNED) - CAST(formed AS SIGNED)
       END as lifespan
FROM metal_bands
WHERE split IS NOT NULL
AND band_style = 'Glam rock'
ORDER BY lifespan DESC;
