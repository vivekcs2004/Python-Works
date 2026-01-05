lst = [10,15,24,22,66]

num_gt_five = [n>5 for n in lst]
is_all_gt_fv = all(num_gt_five)
print(is_all_gt_fv)