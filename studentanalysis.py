import numpy as np
marks=[6,2,6,7,8,9,1,3,4,5,6,7,8,9,6,5]
npmarks=np.array(marks)
print("no of students: ",npmarks.ndim)
#gives no of elements
print("highest marks: ",np.max(npmarks))
print("average marks: ",np.mean(npmarks))
print("lowest marks: ",np.min(npmarks))
print(np.where(npmarks<np.mean(npmarks),"below average",np.where(npmarks==np.mean(npmarks),"average","above average")))
print(np.where(npmarks<4,"fail","pass"))
