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
    "category": "Programming Fundamentals",
    "image": "https://i.ytimg.com/vi/0VoF_lc-16o/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLBWBjZihGempHZCXMcxLm4d7m8i8g",
    "lectures": [
      {
        
        {
          "id": 1,
          "title": "สรุปพื้นฐาน Python 3 ใน 1 ชั่วโมง - Part 1",
          "duration": "29:27",
          "video": "https://www.youtube.com/embed/Jw3h06aIHYk?list=PLcLc3KmtwXNRhXfBf6R46j5CU9Fy2qUSs"
        },
        {
          "id": 2,
          "title": "สรุปพื้นฐาน Python 3 ใน 1 ชั่วโมง - Part2",
          "duration": "33:5",
          "video": "https://www.youtube.com/embed/I_fpG3wrVaQ?list=PLcLc3KmtwXNRhXfBf6R46j5CU9Fy2qUSs&index=2"
        }
      } 
    ]
  } ,
    
  {
    "id": 2,
    "name": "Advanced JavaScript",
    "description":
    "Take your JavaScript skills to the next level with this advanced course.",
    "category": "Web Development",
    "image" : "https://i.ytimg.com/vi/PGZ7QiKdumo/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCSIt6eSRUWBtgXhw04BLeAHiEaug",
    "lectures": [
      
      {
        "id": 1,
        "title": "สรุปพื้นฐาน Python 3 ใน 1 ชั่วโมง - Part 1",
        "duration": "29:27",
        "video": "https://www.youtube.com/embed/Jw3h06aIHYk&list=PLcLc3KmtwXNRhXfBf6R46j5CU9Fy2qUSs"
      },
      {
        "id": 2,
        "title": "สรุปพื้นฐาน Python 3 ใน 1 ชั่วโมง - Part2",
        "duration": "10:32",
        "video": "https://www.youtube.com/embed/I_fpG3wrVaQ&list=PLcLc3KmtwXNRhXfBf6R46j5CU9Fy2qUSs&index=2"
      }
    ]
  },
  {
    "id": 3,
    "name": "Machine Learning ",
    "description":
    "Learn how to build machine learning ",
    "category": "Machine Learning",
    "image": "https://i.ytimg.com/vi/lA5MHygnFcg/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLCfEDjNHKsFdz7wTWhwuMTm-vgmqQ",
    "lectures": [
      {
        "id": 1,
        "title": "สรุปพื้นฐาน Python 3 ใน 1 ชั่วโมง - Part 1",
        "duration": "29:27",
        "video": "https://www.youtube.com/embed/Jw3h06aIHYk&list=PLcLc3KmtwXNRhXfBf6R46j5CU9Fy2qUSs"
      },
      {
        "id": 2,
        "title": "สรุปพื้นฐาน Python 3 ใน 1 ชั่วโมง - Part2",
        "duration": "10:32",
        "video": "https://www.youtube.com/embed/I_fpG3wrVaQ&list=PLcLc3KmtwXNRhXfBf6R46j5CU9Fy2qUSs&index=2"
      }
    ]
  },
  {
    "id": 4,
    "name": "Data Science with R",
    "description":
    "Explore the world of data science using the R programming language.",
    "category": "Data Science",
    "image": "https://i.ytimg.com/vi/tlakIID89Rk/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLB8u6INK0AOLJ02nTw9prJ4awh99w",
    "lectures": [
      {
        "id": 1,
        "title": "สรุปพื้นฐาน Python 3 ใน 1 ชั่วโมง - Part 1",
        "duration": "29:27",
        "video": "https://www.youtube.com/embed/Jw3h06aIHYk&list=PLcLc3KmtwXNRhXfBf6R46j5CU9Fy2qUSs"
      },
      {
        "id": 2,
        "title": "สรุปพื้นฐาน Python 3 ใน 1 ชั่วโมง - Part2",
        "duration": "10:32",
        "video": "https://www.youtube.com/embed/I_fpG3wrVaQ&list=PLcLc3KmtwXNRhXfBf6R46j5CU9Fy2qUSs&index=2"
      }
    ]
  },
  {
    "id": 5,
    "name": "CSS Basic",
    "description":
    "Explore the world css.",
    "category": "Web Development",
    "image": "https://i.ytimg.com/vi/9H6ubALp8vo/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLCNevF797NPW5aDzAejrtAOyLw2sA",
    "lectures": [
      {
        "id": 1,
        "title": "สรุปพื้นฐาน Python 3 ใน 1 ชั่วโมง - Part 1",
        "duration": "29:27",
        "video": "https://www.youtube.com/embed/Jw3h06aIHYk&list=PLcLc3KmtwXNRhXfBf6R46j5CU9Fy2qUSs"
      },
      {
        "id": 2,
        "title": "สรุปพื้นฐาน Python 3 ใน 1 ชั่วโมง - Part2",
        "duration": "10:32",
        "video": "https://www.youtube.com/embed/I_fpG3wrVaQ&list=PLcLc3KmtwXNRhXfBf6R46j5CU9Fy2qUSs&index=2"
      }
    ]
  },
  {
    "id": 6,
    "name": "HTML Basic",
    "description":
    "Explore the world html.",
    "category": "Web Development",
    "image": "https://i.ytimg.com/vi/-jzu5YH6OMQ/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLDFVaUm1ckDJw9Ypa2j3z3P8zUQ9Q",
    "lectures": [
      {
        "id": 1,
        "title": "สรุปพื้นฐาน Python 3 ใน 1 ชั่วโมง - Part 1",
        "duration": "29:27",
        "video": "https://www.youtube.com/embed/Jw3h06aIHYk&list=PLcLc3KmtwXNRhXfBf6R46j5CU9Fy2qUSs"
      },
      {
        "id": 2,
        "title": "สรุปพื้นฐาน Python 3 ใน 1 ชั่วโมง - Part2",
        "duration": "10:32",
        "video": "https://www.youtube.com/embed/I_fpG3wrVaQ&list=PLcLc3KmtwXNRhXfBf6R46j5CU9Fy2qUSs&index=2"
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
