import abc
from courses.model.course_model import Course

class CourseRespository(abc.ABC):

    @abc.abstractmethod
    def add(self, name: str, description: str) -> Course:
        raise NotImplementedError
    
    @abc.abstractmethod
    def get(self, id: int) -> Course:
        raise NotImplementedError
    
class LocalCourseRepository(CourseRespository):
    
    def __init__(self):
        self.courses = []
    
    def add(self, name: str, description: str) -> Course:
        
        for course in self.courses:
            if course.name == name:
                return None

        course = Course(
            id=len(self.courses) + 1,
            name=name,
            description=description
        )
        self.courses.append(course)
        return course
    
    def get(self, id: int) -> Course:
        course_found = None
        for course in self.courses:
            if course.id == id:
                course_found = course
                break
        return course_found
