import numpy as np

def process_marks(m):
    print('\nExam marks\n',              m)
    print('B?\n',                       (m >= 60) & (m < 70))
    print('A or U?\n',                  (m >= 70) | (m < 30))
    print('A or even, but not both?\n', (m >= 70) ^ (m % 2 == 0))
    print('Not (A or U)?\n',            ~((m >= 70) | (m < 30)))

my_exam_marks = np.array([71, 95, 49, 100, 65])
process_marks(my_exam_marks)

our_exam_marks = np.array([[71, 95, 49, 100, 65], [99, 22, 78, 88, 92]])
process_marks(our_exam_marks)