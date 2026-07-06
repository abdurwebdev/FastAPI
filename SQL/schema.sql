CREATE TABLE jobs(
     id SERIAL PRIMARY KEY,
     title VARCHAR(100),
	 company VARCHAR(100),
	 location VARCHAR(100),
	 salary INTEGER,
	 is_remote BOOLEAN,
	 experience INTEGER
);

INSERT INTO jobs
(
      title,
	  company,
	  location,
	  salary,
	  is_remote,
	  experience
)
VALUES (
       'Backend Developer',
	   'Codeaza Technologies',
	   'Rawalpindi',
	   8000000,
	   FALSE,
	   5
);

SELECT * FROM jobs;

UPDATE jobs
SET salary = 12000000
WHERE id = 1;

DELETE FROM jobs
WHERE id = 1

INSERT INTO jobs(
     title,
	 company,
	 location,
	 salary,
	 is_remote,
	 experience
)
VALUES (
     'Front end Developer',
	 'Codeaza',
	 'Rawalpindi',
	 12000000,
	 TRUE,
	 5
),(
     'Backend Developer',
	 'Codeaza',
	 'Islamabad',
	 300000,
	 FALSE,
	 7
),
(
     'AI Engineer',
	 'Enabling Systems',
	 'Karachi',
	 500000,
	 TRUE,
	 9
);

UPDATE jobs
SET salary = 1200000000
WHERE id = 1;

DELETE FROM jobs
WHERE id = 2;

SELECT * FROM jobs;