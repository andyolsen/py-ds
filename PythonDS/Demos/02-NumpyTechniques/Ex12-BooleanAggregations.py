import numpy as np

def process_marks(m):
    print('\nExam marks\n',  m)
    print('All passes?    ', np.all(m >= 50))
    print('Any passes?    ', np.any(m >= 50))
    print('Count of passes', np.count_nonzero(m >= 50))
    print('Count of B     ', np.count_nonzero((m >= 60) & (m < 70)))
    print('Count of A or U', np.count_nonzero((m >= 70) | (m < 30)))

my_exam_marks = np.array([71, 95, 49, 100, 65])
process_marks(my_exam_marks)

our_exam_marks = np.array([[71, 95, 49, 100, 65], [99, 22, 78, 88, 92]])
process_marks(our_exam_marks)