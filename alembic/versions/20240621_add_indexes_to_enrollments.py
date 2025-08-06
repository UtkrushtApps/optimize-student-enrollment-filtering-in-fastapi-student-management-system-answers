"""
Revision ID: 20240621_add_indexes_to_enrollments
Revises: 
Create Date: 2024-06-21 12:34:56.000000

"""
from alembic import op
import sqlalchemy as sa

down_revision = None
revision = '20240621_add_indexes_to_enrollments'
branch_labels = None
depends_on = None

def upgrade():
    # Index to speed up lookup of enrollments by course and status
    op.create_index('ix_enrollments_courseid_status', 'enrollments', ['course_id', 'status'])
    # Index to speed up lookup of enrollments by student
    op.create_index('ix_enrollments_studentid', 'enrollments', ['student_id'])
    # Index to speed up lookup of students
    op.create_index('ix_students_id', 'students', ['id'])

def downgrade():
    op.drop_index('ix_enrollments_courseid_status', table_name='enrollments')
    op.drop_index('ix_enrollments_studentid', table_name='enrollments')
    op.drop_index('ix_students_id', table_name='students')
