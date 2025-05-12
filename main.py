from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

courses = [
  {
    "id": 1,
    "name": "Intro to Python",
    "description":
    "Learn the basics of Python, a popular programming language for both beginners and experts.",
    "category": "Programming Fundamentals"
  },
  {
    "id": 2,
    "name": "Advanced JavaScript",
    "description":
    "Take your JavaScript skills to the next level with this advanced course.",
    "category": "Web Development"
  },
  {
    "id": 3,
    "name": "Machine Learning with TensorFlow",
    "description":
    "Learn how to build machine learning models using the popular TensorFlow library.",
    "category": "Machine Learning"
  },
  {
    "id": 4,
    "name": "Data Science with R",
    "description":
    "Explore the world of data science using the R programming language.",
    "category": "Data Science"
  },
  # ... add more courses here ...
]


@app.route('/')
def index():
  return "<h1>Final API</h1><br>สำหรับวิธีการเข้าใช้งาน API สามารถเข้าใช้งานได้ดังนี้ <br><li><b>การเข้าถึงรายละเอียดแต่ละคอร์ส</b> สามารถเข้าได้ที่ /courses/<int:course_id> โดย course_id คือ ไอดีของแต่ละหลักสูตร<br>เช่น https://borntodev-final-project-api.borntodev.repl.co/courses/1</li><li><b>ดูรายการหลักสูตรทั้งหมด</b> สามารถเข้าได้ที่ /courses จะแสดงข้อมูลหลักสูตรทั้งหมดออกมา<br>เช่น https://borntodev-final-project-api.borntodev.repl.co/courses</li><li><b>ดูรายการหมวดหมู่ทั้งหมด</b> สามารถเข้าได้ที่ /categories จะแสดงชื่อหมวดหมู่ทั้งหมดออกมา<br>เช่น https://borntodev-final-project-api.borntodev.repl.co/categories</li><li><b>ดูรายการหมวดหมู่ทั้งหมด</b> สามารถเข้าได้ที่ /categories/<string:category_name>/courses โดยเราจะใส่ชื่อหมวดหมู่ลงไป เราจะได้หลักสูตรทั้งหมดในหมวดหมู่นั้น ๆ ออกมา<br>เช่น https://borntodev-final-project-api.borntodev.repl.co/categories/Web%20Development/courses (ตัวพิมพ์เล็ก และ ใหญ่มีผล)</li><p>ขอให้ทุกคนพยายามอย่างเต็มที่กับ Project Final ของหลักสูตรนี้นะครับ 😊</p>"


@app.route('/courses', methods=['GET'])
def get_all_courses():
  return jsonify(courses)


@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
  course = next((course for course in courses if course["id"] == course_id),
                None)
  if course is not None:
    return jsonify(course)
  else:
    return jsonify({"message": "Course not found"}), 404


@app.route('/categories', methods=['GET'])
def get_categories():
  categories = list(set(course['category'] for course in courses))
  return jsonify(categories)


@app.route('/categories/<string:category_name>/courses', methods=['GET'])
def get_courses_in_category(category_name):
  category_courses = [
    course for course in courses if course["category"] == category_name
  ]
  if category_courses:
    return jsonify(category_courses)
  else:
    return jsonify({"message": "No courses found in this category"}), 404


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
