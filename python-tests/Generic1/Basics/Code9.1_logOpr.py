#logical operators
has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("loan can be granted")
if has_good_credit and has_criminal_record:
    print("loan can't be granted")
if has_good_credit or has_criminal_record:
    print("loan can be granted")





