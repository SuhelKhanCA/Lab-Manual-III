program_course_count = {}
with open('courses.txt', 'r') as file:
    lines = file.readlines()

for line in lines[1:]:
    program, course = line.strip().split(',')
    if program in program_course_count:
        program_course_count[program] += 1
    else:
        program_course_count[program] = 1
        
for program, count in program_course_count.items():
    print(f"{program}-{count:02}")