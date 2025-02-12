-- DELIMITER $$: Changes the delimiter to $$ so that MySQL can interpret the full body
-- of the trigger without ending prematurely due to the default semicolon ;.
DELIMITER $$

CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

DELIMITER ;