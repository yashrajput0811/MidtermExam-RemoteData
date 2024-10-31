from flask import Blueprint, request, jsonify
from app.models import db, Student

bp = Blueprint('students', __name__, url_prefix='/students')

def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
    db.init_app(app)
    db.create_all(app=app)
    app.register_blueprint(bp)

@bp.route('/', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{'id': s.id, 'name': s.name, 'grade': s.grade, 'email': s.email} for s in students])

@bp.route('/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify({'id': student.id, 'name': student.name, 'grade': student.grade, 'email': student.email})

@bp.route('/', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(name=data['name'], grade=data['grade'], email=data['email'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'id': new_student.id}), 201

@bp.route('/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()
    student.name = data['name']
    student.grade = data['grade']
    student.email = data['email']
    db.session.commit()
    return jsonify({'id': student.id})

@bp.route('/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return '', 204