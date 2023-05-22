# student = 75
# if student > 70:
#     print("grade A")

# else:
#     print("not grade A")

scored =int(input("enter student marks:"))

if scored <55:
    print("below average")
elif scored >=55 and scored <=59:
    print("scored C+")
elif scored >=59 and scored <=64:
    print("scored B-")
elif scored >64 and scored <=69:
    print("scored B")
elif scored >69 and scored <=74:
    print("scored B+")
elif scored >74 and scored <=79:
    print("scored A-")
else:
    print("scored A")
