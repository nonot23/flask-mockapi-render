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
    "video": "https://www.youtube.com/embed/0VoF_lc-16o"
  },
  {
    "id": 2,
    "name": "Advanced JavaScript",
    "description":
    "Take your JavaScript skills to the next level with this advanced course.",
    "category": "Web Development",
    "image" : "https://i.ytimg.com/vi/PGZ7QiKdumo/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCSIt6eSRUWBtgXhw04BLeAHiEaug",
    "video": "https://www.youtube.com/embed/PGZ7QiKdumo"
  },
  {
    "id": 3,
    "name": "Machine Learning ",
    "description":
    "Learn how to build machine learning ",
    "category": "Machine Learning",
    "image": "https://i.ytimg.com/vi/lA5MHygnFcg/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLCfEDjNHKsFdz7wTWhwuMTm-vgmqQ",
    "video": "https://www.youtube.com/embed/lA5MHygnFcg&pp=ygUaYm9ybnRvZGV2IG1hY2hpbmUgbGVhcm5pbmc%3D"
  },
  {
    "id": 4,
    "name": "Data Science with R",
    "description":
    "Explore the world of data science using the R programming language.",
    "category": "Data Science",
    "image": "https://i.ytimg.com/vi/tlakIID89Rk/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLB8u6INK0AOLJ02nTw9prJ4awh99w",
    "video" : "https://www.youtube.com/embed/tlakIID89Rk"
  },
  {
    "id": 5,
    "name": "CSS Basic",
    "description":
    "Explore the world css.",
    "category": "Web Development",
    "image": "https://i.ytimg.com/vi/9H6ubALp8vo/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLCNevF797NPW5aDzAejrtAOyLw2sA",
    "video" : "https://www.youtube.com/embed/9H6ubALp8vo"
  },
  {
    "id": 6,
    "name": "HTML Basic",
    "description":
    "Explore the world html.",
    "category": "Web Development",
    "image": "https://i.ytimg.com/vi/-jzu5YH6OMQ/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLDFVaUm1ckDJw9Ypa2j3z3P8zUQ9Q",
    "video" : "https://www.youtube.com/embed/-jzu5YH6OMQ"
  }
  
]


@app.route('/')
def index():
  return "<h1>Final API</h1><br>Here's how to use the API: <br><li><b>Access course details</b> available at /courses/<int:course_id> where course_id is the ID of each course<br>Example: https://borntodev-final-project-api.borntodev.repl.co/courses/1</li><li><b>View all courses</b> available at /courses to display all course information<br>Example: https://borntodev-final-project-api.borntodev.repl.co/courses</li><li><b>View all categories</b> available at /categories to display all category names<br>Example: https://borntodev-final-project-api.borntodev.repl.co/categories</li><li><b>View courses by category</b> available at /categories/<string:category_name>/courses where you input the category name to get all courses in that category<br>Example: https://borntodev-final-project-api.borntodev.repl.co/categories/Web%20Development/courses (Case sensitive)</li><p>Good luck with your Final Project! 😊</p>"


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
