import numpy as np
student_id=[1023,5202,6230,1671,1682,5241,4532]
student_height=[40.,42.,45.,41.,38.,40.,42.0]
chiso = np.lexsort((student_id,student_height))
print(chiso)
print([(student_id[i],student_height[i]) for i in chiso])
