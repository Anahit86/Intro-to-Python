import argparse

#####N5############
list5 = ["f", 4, 6, 7, "jhaf", True, 6, 8, 4, 6]
print("before_change:", list5)
list5.pop(5)
list5.pop(4)
list5.pop(0)
print("after_change:", list5)
