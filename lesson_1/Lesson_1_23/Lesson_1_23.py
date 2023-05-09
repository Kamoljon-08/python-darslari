a = ["lesson_1_1", "lesson_1_2", "lesson_1_3", "lesson_1_4", "lesson_1_4", "lesson_1_6", "lesson_1_7", "lesson_1_8", "lesson_1_9", "lesson_1_10"]

import os
for i in a:

    if os.path.exists(f"{i}.py"):
        print("Bunday file mavjud")
        
    else:
        m = open(f"{i}.py", "x")