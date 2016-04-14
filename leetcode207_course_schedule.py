class Solution(object):
    def canFinish(self, numCourses, prerequisites):
         queue = []
         finished_courses = []
         prereq_graph = {x: set() for x in range(numCourses)}
         for course, prereq in prerequisites:
              prereq_graph[course].add(prereq)
          
         for course in prereq_graph:
              if not prereq_graph[course]:
                  queue.append(course) 
         
         while queue:
              completed_course = queue.pop(0)
              for course, prereqs in prereq_graph.items():
                  if completed_course in prereqs:
                          prereqs.remove(completed_course)
                          if not prereqs:
                              queue.append(course)
              finished_courses.append(completed_course)
         return len(finished_courses) == numCourses                 
