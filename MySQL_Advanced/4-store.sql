-- Create the trigger to update item quantity after inserting a new order
DELIMITER //
CREATE TRIGGER update_item_quantity AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Decrease the item quantity based on the new order
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
//
DELIMITER ;
