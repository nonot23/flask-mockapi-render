from flask import Flask, jsonify
from flask_cors import CORS
from flask import send_from_directory
import os

app = Flask(__name__)
CORS(app)


host_url = os.getenv("RENDER_EXTERNAL_URL", "http://localhost:5000")

courses = [
    {
        "id": 1,
        "name": "Intro to Python",
        "description": "Learn the basics of Python, a popular programming language for both beginners and experts.",
        "category": "Programming Fundamentals",
        "image": f"{host_url}/img/python.png",
        "lectures": [
            {
                "lectureTitle": "เข้าใจโครงสร้างพื้นฐานของภาษา Python",
                "totalDuration": "62 นาที",
                "videos": [
                    {
                        "title": "สรุปพื้นฐาน Python 3 ใน 1 ชั่วโมง - Part 1",
                        "duration": "29:27 นาที",
                        "video": "https://www.youtube.com/embed/Jw3h06aIHYk?list=PLcLc3KmtwXNRhXfBf6R46j5CU9Fy2qUSs"
                    },
                    {
                        "title": "สรุปพื้นฐาน Python 3 ใน 1 ชั่วโมง - Part 2",
                        "duration": "33:05 นาที",
                        "video": "https://www.youtube.com/embed/I_fpG3wrVaQ?list=PLcLc3KmtwXNRhXfBf6R46j5CU9Fy2qUSs&index=2"
                    }
                ]
            }
        ]
    },
    {
        "id": 2,
        "name": "Basic JavaScript",
        "description": "Take your JavaScript skills to the next level with this basic course.",
        "category": "Web Development",
        "image": f"{host_url}/img/js.png",
        "lectures": [
            {
                "lectureTitle": "เข้าใจโครงสร้างพื้นฐานของภาษา JavaScript",
                "totalDuration": "3 ชั่วโมง 16 นาที",
                "videos": [
                    {
                        "title": "สรุปพื้นฐาน JavaScript",
                        "duration": "3:16:22 นาที",
                        "video": "https://www.youtube.com/embed/PGZ7QiKdumo"
                    }
                ]
            }
        ]
    },
    {
        "id": 3,
        "name": "Machine Learning",
        "description": "Learn how to build machine learning",
        "category": "Machine Learning",
        "image": f"{host_url}/img/manchin.png",
        "lectures": [
            {
                "lectureTitle": "Machine Learning",
                "totalDuration": "8 นาที",
                "videos": [
                    {
                        "title": "เริ่มเขียน Machine Learning ใน 5 นาที",
                        "duration": "8:05 นาที",
                        "video": "https://www.youtube.com/embed/lA5MHygnFcg"
                    }
                ]
            }
        ]
    },
    {
        "id": 4,
        "name": "Data Science with R",
        "description": "Explore the world of data science using the R programming language.",
        "category": "Data Science",
        "image": f"{host_url}/img/R.png",
        "lectures": [
            {
                "lectureTitle": "เริ่มต้นใช้งานภาษา R",
                "totalDuration": "36 นาที",
                "videos": [
                    {
                        "title": "เริ่มต้นใช้งานภาษา R เพื่องาน DataScience",
                        "duration": "36:23 นาที",
                        "video": "https://www.youtube.com/embed/tlakIID89Rk"
                    }
                ]
            }
        ]
    },
    {
        "id": 5,
        "name": "html Basic",
        "description": "Explore the world html.",
        "category": "Web Development",
        "image": f"{host_url}/img/html.png",
        "lectures": [
            {
                "lectureTitle": "เข้าใจโครงสร้างพื้นฐานของภาษา html",
                "totalDuration": "11 นาที",
                "videos": [
                    {
                        "title": "มาเรียนเขียนเว็บด้วย HTML 5 !! ฉบับที่เร็วที่สุด !",
                        "duration": "11:08 นาที",
                        "video": "https://www.youtube.com/embed/-jzu5YH6OMQ"
                    }
                ]
            }
        ]
    },
    {
        "id": 6,
        "name": "CSS Basic",
        "description": "Explore the world css.",
        "category": "Web Development",
        "image": f"{host_url}/img/css.png",
        "lectures": [
            {
                "lectureTitle": "เข้าใจโครงสร้างพื้นฐานของภาษา CSS",
                "totalDuration": "22 นาที",
                "videos": [
                    {
                        "title": "มาหัดเขียน CSS3 ที่ช่วยให้เว็บสวยขึ้น แบบไว ๆ ใน 10 นาที",
                        "duration": "10:40 นาที",
                        "video": "https://www.youtube.com/embed/9H6ubALp8vo"
                    },
                    {
                        "title": "จัด Layout เว็บแบบไม่ซ้ำใคร!!! ด้วย Flexbox และ CSS Grid",
                        "duration": "12:08 นาที",
                        "video": "https://www.youtube.com/embed/UHPN0Wd2XLE"
                    }
                ]
            }
        ]
    }
]



@app.route('/')
def index():
  return """
<h1>Final API / API สำหรับโครงการ</h1>
<br>วิธีการใช้งาน API:<br>
<li><b>ดูรายละเอียดคอร์ส</b> ที่ /courses/<int:course_id> โดย course_id คือ ID ของแต่ละคอร์ส<br>
ตัวอย่าง: https://borntodev-final-project-api.borntodev.repl.co/courses/1</li>
<li><b>ดูคอร์สทั้งหมด</b> ที่ /courses เพื่อแสดงข้อมูลคอร์สทั้งหมด<br>
ตัวอย่าง: https://borntodev-final-project-api.borntodev.repl.co/courses</li>
<li><b>ดูหมวดหมู่ทั้งหมด</b> ที่ /categories เพื่อแสดงชื่อหมวดหมู่ทั้งหมด<br>
ตัวอย่าง: https://borntodev-final-project-api.borntodev.repl.co/categories</li>
<li><b>ดูคอร์สตามหมวดหมู่</b> ที่ /categories/<string:category_name>/courses โดยใส่ชื่อหมวดหมู่เพื่อดูคอร์สในหมวดนั้น<br>
ตัวอย่าง: https://borntodev-final-project-api.borntodev.repl.co/categories/Web%20Development/courses (ต้องตรงตัวพิมพ์ใหญ่-เล็ก)</li>
<p>ขอให้โชคดีกับโปรเจคของคุณ! 😊</p>
"""

@app.route('/img/<path:filename>')
def serve_image(filename):
    return send_from_directory('img', filename)

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

@app.route('/search', methods=['GET'])
def search_courses():
    keyword = request.args.get('keyword', '').lower()
    results = [
        course for course in courses
        if keyword in course["name"].lower()
    ]
    return jsonify(results)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)