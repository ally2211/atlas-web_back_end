-- creates a stored procedure ComputeAverageScoreForUser 
-- that computes and store the average score for a student. 

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id_param  INT
)
BEGIN
    DECLARE avg_score DECIMAL(10,2);

    -- Compute the average score for the given user_id
    SELECT AVG(score) INTO avg_score 
    FROM corrections 
    WHERE user_id = user_id_param ;

    -- Update the user's average score in the users table
    UPDATE users 
    SET average_score = avg_score 
    WHERE id = user_id_param ;
END$$

DELIMITER ;
