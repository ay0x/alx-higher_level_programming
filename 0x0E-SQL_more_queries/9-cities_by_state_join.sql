-- Join Cities and States
SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states on states.id = cities.states_id
ORDER BY cities.id ASC;