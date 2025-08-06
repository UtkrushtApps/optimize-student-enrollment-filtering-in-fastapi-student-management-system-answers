from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from sqlalchemy import and_
from app.db.models import Student, Course, Enrollment, EnrollmentStatusEnum

async def get_students_by_course_and_status(db: AsyncSession, course_id: int, status: str = None):
    # Direct join using indexed columns, load only necessary fields
    q = (
        select(Student)
        .join(Enrollment, Enrollment.student_id == Student.id)
        .where(Enrollment.course_id == course_id)
    )
    if status:
        q = q.where(Enrollment.status == status)

    # Optionally we can use joinedload if we need Enrollment backref
    result = await db.execute(q)
    return result.scalars().all()
