import numpy as np

def process_marks(m):
    print('Exam marks\n',      m)
    print('Passes?\n',         m >= 50)
    print('Full marks?\n',     m == 100)
    print('Not full marks?\n', m != 100)

my_exam_marks = np.array([71, 95, 49, 100, 65])
process_marks(my_exam_marks)

our_exam_marks = np.array([[71, 95, 49, 100, 65], [99, 22, 78, 88, 92]])
process_marks(our_exam_marks)