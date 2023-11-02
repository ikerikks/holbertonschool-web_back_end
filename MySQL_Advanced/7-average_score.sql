-- Create the stored procedure ComputeAverageScoreForUser
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE average FLOAT;
    
    -- Calculate the average score for the user
    SELECT AVG(score) INTO average
    FROM corrections
    WHERE user_id = user_id;
    
    -- Update the user's average score
    UPDATE users
    SET average_score = average
    WHERE id = user_id;
    
END;
//
DELIMITER ;
