ALTER TABLE player_bios
ADD COLUMN height_inches NUMERIC;

UPDATE player_bios
SET height_inches = 12*split_part(height, '-',1)::integer + split_part(height, '-',2)::integer;

ALTER TABLE player_bios
DROP COLUMN height;

ALTER TABLE player_bios
RENAME COLUMN height_inches TO height;

SELECT firstname, lastname, height FROM player_bios limit 5;

