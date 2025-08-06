from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.session import Base
import enum

class EnrollmentStatusEnum(str, enum.Enum):
    active = "active"
    inactive = "inactive"

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    # relationships
    enrollments = relationship("Enrollment", back_populates="student")

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    # relationships
    enrollments = relationship("Enrollment", back_populates="course")

class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False, index=True)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False, index=True)
    status = Column(Enum(EnrollmentStatusEnum), nullable=False, index=True)

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

    __table_args__ = (
        # Composite index to support frequent course/status filtering
        sa.Index('ix_enrollments_courseid_status', 'course_id', 'status'),
        sa.Index('ix_enrollments_studentid', 'student_id'),
    )
