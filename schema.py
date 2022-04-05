import urllib.request    # needed for download of the example database
import shutil            # needed for unziping of the example database
import os                # for checking existence/removing of a file

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

base = declarative_base()
class Task(base):
    _tablename_ = "Task"
    taskid = Column(Integer,primary_key=True)
    title = Column(string(50))
    content = Column(string(50))
    assignment_r = relationship("Assignment")
    task_q_r = relationship("Task_question")
    
class Assignment(base):
    _tablename_ = "Assignment"
    assignmentid = Column(Integer,primary_key=True)
    universityid = Column(ForeignKey('Student.universityid'))
    taskid = Column(ForeignKey('Task.taskid'), nullable=True)
    submission_r = relationship("Submission")
    
class Task_question(base):
    _tablename_ = "Task_question"
    taskid = Column(ForeignKey('Task.taskid'))
    questionid = Column(ForeignKey('Question.questionid'), nullable=True)

class Student(base):
    _tablename_ = "Student"
    universityid = Column(Integer,primary_key=True)
    name = Column(string)
    email = Column(string)
    sttudent_r = relationship("Assignment")
    
class Submission(base):
    _tablename_ = "Submission"
    submissionid = Column(Integer,primary_key=True)
    assignmentid = Column(ForeignKey('Assignment.assignmentid'), nullable=True)
    eval_r = relationship("EvaluationRequest")
    answers_r = relationship("Answers")
    
class EvaluationRequest(base):
    _tablename_ = "EvaluationRequest"
    requestid = Column(Integer,primary_key=True)
    submissionid = Column(ForeignKey('Submission.submissionid'), nullable=True)
    eval_r = relationship("Evaluation")
    
class Question(base):
    _tablename_ = "Question"
    questionid = Column(Integer,primary_key=True)
    title = Column(String(50))
    content = Column(string(50))
    task_q_r = relationship("Task_question")
    answer_r = relationship("Answer")
    
class Answers(base):
    _tablename_ = "Answers"
    answerid = Column(Integer,primary_key=True)
    content = Column(string(1000))
    questionId = Column(ForeignKey('Question.questionid'), nullable=True)
    sumissionid = Column(ForeignKey('Submission.submissionid'))
    scores_r = relationship("Scores")
    
class Evaluation(base):
    _tablename_ = "Evaluation"
    evaluationid = Column(Integer, primary_key = True)
    requestid = Column(ForeignKey('EvaluationRequest.requestid'), nullable=True)
    evaluation_f_r = relationship("EvaluationFinished")
    scores_r = relationship("Scores")

class Scores(base):
    _tablename_ = "Scores"
    scoreid = Column(Integer, primary_key = True)
    value = Column(Integer)
    answerid = Column(ForeignKey('Answers.answerid'),nullable = True)
    evaluationid = Column(ForeignKey('Evaluation.evaluationid'))
    
class EvaluationFinished(base):
    _tablename_ = "EvaluationFinished"
    finishedid = Column(Integer, primary_key = True)
    evaluationid = Column(ForeignKey('Evaluation.evaluationid'),nullable = True)