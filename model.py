from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

student_courses = db.Table(
    'student_course',
    db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('courses.id'), primary_key=True)
)

class School(db.Model):
    __tablename__ = 'schools'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    address = db.Column(db.String(100), nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)  
    students = db.relationship('Student', backref='school', lazy=True)
    courses = db.relationship('Course', backref='school', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'students': [student.as_dict() for student in self.students],
            'courses': [course.as_dict() for course in self.courses]
        }


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'), nullable=False)
    courses = db.relationship('Course', secondary=student_courses, back_populates='students')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def as_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'school_id': self.school_id,
            'courses': [course.as_dict() for course in self.courses]
        }


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'), nullable=False)
    students = db.relationship('Student', secondary=student_courses, back_populates='courses')

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'school_id': self.school_id,
            'students': [student.as_dict() for student in self.students]
        }


from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()

student_courses = db.Table('student_courses',
                           db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
                           db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True)
                           )

class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(100), nullable=True)
    password_hash = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    students = db.relationship('Student', backref='school', lazy=True)
    courses = db.relationship('Course', backref='school', lazy=True)

    def as_dict(self):
        return{
            'id':self.id,
            'name':self.name,
            'address':self.address,
            'password_hash':self.password_hash,
            'email':self.email,
            'students':[student.as_dict() for student in self.students],
            'courses':[course.as_dict() for course in self.courses]
        }
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Student(db.Model):
    __tablename__ = 'Students'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    courses = db.relationship('Course', back_populates='students', secondary= student_courses)

    def set_password(self, password):
        self.set_password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def as_dict(self):
        return{
            'id':self.id,
            'first_name':self.first_name,
            'last_name':self.last_name,
            'email':self.email,
            'password_hash':self.password_hash,
            'school_id':self.school_id,
            'courses':[course.as_dict() for course in self.courses]
        }
    
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(45), nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    students = db.relationship('Student', back_populates='course', secondary=student_courses)

    def as_dict(self):
        return{
            'id':self.id,
            'name':self.name,
            'description':self.description,
            'password_hash':self.password_hash,
            'school_id':self.school_id,
            'students':[student.as_dict() for student in self.students]
        }
    

    


