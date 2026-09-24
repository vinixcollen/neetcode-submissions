class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while count < len(students):
            if students[0] != sandwiches[0]:
                temp = students.pop(0)
                students.append(temp)
                count += 1
            else:
                students.pop(0)
                sandwiches.pop(0)
                count = 0

        return len(students)

                
