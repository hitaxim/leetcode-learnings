SELECT 
    user_id, 
    AVG(pins_count) AS avg_pins
FROM (
    SELECT 
        pins.user_id, 
        boards.board_id, 
        COUNT(pins.pin_id) AS pins_count
    FROM 
        boards 
    INNER JOIN 
        pins ON boards.board_id = pins.board_id
    WHERE 
        pins.user_id = 123
    GROUP BY 
        user_id, board_id
) AS user_boards
GROUP BY 
    user_id;
