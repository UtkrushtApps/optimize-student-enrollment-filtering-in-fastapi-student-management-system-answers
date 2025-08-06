# Solution Steps

1. Analyze the existing PostgreSQL query for the student enrollment filtering endpoint using the EXPLAIN ANALYZE statement (in tools like psql or DBeaver) to identify bottlenecks such as full table scans on the enrollments table.

2. Identify that the slow performance is caused by missing indexes on enrollments.course_id, enrollments.status, and enrollments.student_id columns involved in the filtering and joining process.

3. Create a new database migration (using Alembic or a similar tool) that adds composite and individual indexes to the enrollments table (e.g., (course_id, status), student_id), and a simple index on students.id for fast lookups.

4. Modify the SQLAlchemy Enrollment model to declare these indexes using SQLAlchemy's 'Index' construct in __table_args__, ensuring migrations and table definitions are consistent.

5. Ensure all index definitions match the filtering/joining access patterns (course_id+status for filtering, student_id for join, students.id for join).

6. Ensure the API's filtering query (in CRUD/data-access functions) uses SQL joins and where clauses that benefit from these indexes, and loads only the required fields (reduce over-joining and unnecessary columns).

7. Re-run the Alembic migration to apply index changes to the database.

8. Test the student filtering endpoint with a large dataset to confirm significant performance improvement (i.e., verify that queries use indexes and no longer perform full table scans).

