print('-----ROADMAP PROVIDER PROJECT-----')

level = int(input('enter 1-Fresher, 2-Experienced = '))

if level == 1:
    print('Ok...you are a fresher!')
    interest = int(input('enter your interest 1) Web Dev, 2) App dev, 3) DS,AI,ML = '))
    
    if interest == 1:
        print('Learn HTML/CSS/JS/PYTHON/DJANGO/FLASK')
    
    elif interest == 2:
        print('Learn JAVA/DSA/PROJECTS')

    elif interest == 3:
        print('Learn python/pandas/numpy')

    else:
        print('in-valid input')

elif level == 2:
    print('Ok...you are a experienced person!')
    interest = int(input('enter your interest 1) Data Analytics, 2) Cloud Computing, 3) Front-end = '))

    if interest == 1:
        print('Learn PYTHON/LIBRARIES/TOOLS')
    
    elif interest == 2:
        print('Learn DevOps/CloudTools')

    elif interest == 3:
        print('LEARN PYTHON/DJANGO/FLASK')

    else:
        print('in-valid input')

else:
    print('In-valid input')