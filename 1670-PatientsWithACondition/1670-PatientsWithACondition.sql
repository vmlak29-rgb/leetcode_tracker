-- Last updated: 17/07/2026, 14:59:27
# Write your MySQL query statement below
SELECT
    patient_id,
    patient_name,
    conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%'
   OR conditions LIKE '% DIAB1%';