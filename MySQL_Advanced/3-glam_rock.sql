-- lists all bands with Glam rock as their main style
--  ranked by their longevity
SELECT 
    name AS band_name,
    CASE 
        WHEN split IS NOT NULL THEN split - formed
        ELSE YEAR(CURDATE()) - formed
    END AS lifespan
FROM bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
