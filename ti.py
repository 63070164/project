import sys, glob

final_code = []
python_scripts = glob.glob('*.py') + glob.glob('*.pyw')
print(python_scripts)
for script in python_scripts:
    if script == "ti.py" or script == "Replicating-Virus.py":
        continue
    with open(script, 'r') as f:
        script_code = f.readlines()

    infected = False
    for line in script_code:
        if line == '### END OF VIRUS ###\n':
            infected = True

        if infected:
            final_code = []
            print(final_code)
            final_code.extend(line)

    with open(script, 'w') as f:
        f.writelines(final_code)
    final_code = []