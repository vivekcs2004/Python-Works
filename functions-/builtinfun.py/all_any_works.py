words = ["housefull","beuatiful","peacefull","harmful","thinkful","powerful"]

end_with_ful = [w.endswith("ful") for w in words]
is_all_ends_with_ful = all(end_with_ful)
# print(is_all_ends_with_ful)


wordss = ["program","problem","perfect","apple"]

starts_with_pro = [w.startswith("pro") for w in wordss]
print(any(starts_with_pro))