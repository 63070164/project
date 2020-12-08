import glob

final = []
final_code = []
python_scripts = glob.glob('*.py') + glob.glob('*.pyw')

for script in python_scripts:
    with open(script, 'r') as f:
        script_code = f.readlines()

    infected = False
    for line in script_code:
        if '### END OF VIRUS ###\n' not in script_code:
            infected = True
        if infected:
            final.append(line)
        if line == '### END OF VIRUS ###\n':
            infected = True
    while '\n' in final:
        final.remove('\n')
    with open(script, 'w') as f:
        f.writelines(final_code)
    final = []
    final_code = []
