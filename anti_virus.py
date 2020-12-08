import glob

final_code = []
python_scripts = glob.glob('*.py') + glob.glob('*.pyw')

for script in python_scripts:
    if script == "ti.py":
        continue
    with open(script, 'r') as f:
        script_code = f.readlines()

    infected = False
    for line in script_code:
        if infected:
            final_code.extend(line)
        if line == '### END OF VIRUS ###\n':
            infected = True

    with open(script, 'w') as f:
        f.writelines(final_code)
    final_code = []
