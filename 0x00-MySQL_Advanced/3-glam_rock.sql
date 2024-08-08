-- List all Glam rock bands ranked by their longevity
SELECT
  band_name,
  (2022 - formed) AS lifespan
FROM
  metal_bands
WHERE
  style = 'Glam rock'
ORDER BY
  lifespan DESC;
