#frontend->jobs
#backend -> job

#frontend -> ask if job is done
#backend -> report status

#if job is done, backend can send story


from sqlalchemy import Column, Integer, String,DateTime
from sqlalchemy.sql import func


from db.database import Base

class StoryJob(Base):
    __tablename__ = "story_jobs"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, index=True, unique=True)
    session_id = Column(String, index=True)
    theme = Column(String)
    status = Column(String)  # e.g., 'pending', 'in_progress', 'completed'
    story_id = Column(Integer,nullable=True)  # Link to generated story
    error = Column(String,nullable=True)  # Error message if any
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True),nullable=True)