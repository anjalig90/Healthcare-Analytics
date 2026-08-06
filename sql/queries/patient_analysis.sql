USE healthcare_analytics;


-- Total number of patients
SELECT 
    COUNT(*) AS total_patients
FROM patients;


-- Average patient age
SELECT
    AVG(age) AS average_age
FROM patients;


-- Gender distribution
SELECT
    gender,
    COUNT(*) AS patient_count
FROM patients
GROUP BY gender;


-- Most common medical conditions
SELECT
    medical_condition,
    COUNT(*) AS total_cases
FROM patients
GROUP BY 'Medical Condition'
ORDER BY total_cases DESC;


-- Average billing amount
SELECT
    AVG('Billing Amount') AS avg_bill
FROM patients;


-- Average length of stay
SELECT
    AVG('Length_of_Stay') AS avg_stay
FROM patients;