CREATE TABLE new_table (
player INTEGER references more_player_stats,
prl NUMERIC,
position TEXT
);

INSERT INTO new_table (player, prl)
(SELECT id, per-67*round(va/(gp*minutes),1) FROM more_player_stats);

\d new_table

UPDATE new_table
SET position = CASE
WHEN prl >= 11.3 THEN 'PF'
WHEN prl >= 10.8 and prl < 11.3 THEN 'PG'
WHEN prl >= 10.6 and prl < 10.8 THEN 'C'
ELSE 'SG/SF'
END
;

SELECT * FROM new_table limit 10;

