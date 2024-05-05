from flask import Blueprint, jsonify, request
from courses.repository.course_repository import LocalCourseRepository

blueprint = Blueprint('course_controller', __name__)
repository = LocalCourseRepository()

# Endpoint to insert courses
@blueprint.route("/courses", methods=["POST"])
def insert_course():
    # Get the course data from the request
    course_data = request.get_json()

    # Add the new course to the list of courses
    course = repository.add(course_data["name"], course_data["description"])

    # If the course name is found, return a 400 error
    if course is None:
        return jsonify({"message": "Course already exists"}), 400

    # Return the newly inserted course
    return jsonify(course)


# Endpoint to retrieve courses based on its id
@blueprint.route("/courses/<course_id>", methods=["GET"])
def get_course(course_id):
    # Find the course with the given course_id
    
    course_found = repository.get(int(course_id))

    # If the course is not found, return a 404 error
    if course_found is None:
        return jsonify({"message": "Course not found"}), 404

    # Return the retrieved course
    return jsonify(course_found)