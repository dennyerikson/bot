import subprocess as s

def sala_23():
    sala = '25'
    cpf = '38019987894'
    cartao = "/run/user/1000/gvfs/smb-share:server=10.112.1.2,share=d$/PROVAS/BOT/SALA_" + sala + "/CARTAO/" + cpf + ".pdf"
    prova = "/run/user/1000/gvfs/smb-share:server=10.112.1.2,share=d$/PROVAS/BOT/SALA_25/PROVA/prova.pdf"
    # impressora = 'RICOH_Aficio_MP_301_002673A52B66_ '  # TI
    impressora = 'ANH-TAU-INF-023 '  # TI

    try:
        if sala == '25':
            s.call(["lp -d " + impressora + cartao], shell=True)
            s.call(["lp -d " + impressora + prova], shell=True)
            print("Imprimindo SALA_{} CPF: {}".format(sala, cpf))

    except FileNotFoundError:
        print("ERROR SALA_{} CPF: {}".format(sala, cpf))

def sala_15():
    sala = '25'
    cpf = '38019987894'
    cartao = "/run/user/1000/gvfs/smb-share:server=10.112.1.2,share=d$/PROVAS/BOT/SALA_" + sala + "/CARTAO/" + cpf + ".pdf"
    prova = "/run/user/1000/gvfs/smb-share:server=10.112.1.2,share=d$/PROVAS/BOT/SALA_25/PROVA/prova.pdf"
    # impressora = 'RICOH_Aficio_MP_301_002673A52B66_ '  # TI
    # impressora = 'ANH-TAU-INF-015 '  # TI
    impressora = 'RICOH-SP-4510SF '  # TI

    try:
        if sala == '25':
            s.call(["lp -d " + impressora + cartao], shell=True)
            s.call(["lp -d " + impressora + prova], shell=True)
            print("Imprimindo SALA_{} CPF: {}".format(sala, cpf))

    except FileNotFoundError:
        print("ERROR SALA_{} CPF: {}".format(sala, cpf))

def sala_17():
    sala = '25'
    cpf = '38019987894'
    cartao = "/run/user/1000/gvfs/smb-share:server=10.112.1.2,share=d$/PROVAS/BOT/SALA_" + sala + "/CARTAO/" + cpf + ".pdf"
    prova = "/run/user/1000/gvfs/smb-share:server=10.112.1.2,share=d$/PROVAS/BOT/SALA_25/PROVA/prova.pdf"
    # impressora = 'RICOH_Aficio_MP_301_002673A52B66_ '  # TI
    impressora = 'ANH-TAU-INF-017 '  # TI

    try:
        if sala == '25':
            s.call(["lp -d " + impressora + cartao], shell=True)
            s.call(["lp -d " + impressora + prova], shell=True)
            print("Imprimindo SALA_{} CPF: {}".format(sala, cpf))

    except FileNotFoundError:
        print("ERROR SALA_{} CPF: {}".format(sala, cpf))

def sala_13():
    sala = '25'
    cpf = '38019987894'
    cartao = "/run/user/1000/gvfs/smb-share:server=10.112.1.2,share=d$/PROVAS/BOT/SALA_" + sala + "/CARTAO/" + cpf + ".pdf"
    prova = "/run/user/1000/gvfs/smb-share:server=10.112.1.2,share=d$/PROVAS/BOT/SALA_25/PROVA/prova.pdf"
    # impressora = 'RICOH_Aficio_MP_301_002673A52B66_ '  # TI
    impressora = 'ANH-TAU-INF-013 '  # TI

    try:
        if sala == '25':
            s.call(["lp -d " + impressora + cartao], shell=True)
            s.call(["lp -d " + impressora + prova], shell=True)
            print("Imprimindo SALA_{} CPF: {}".format(sala, cpf))

    except FileNotFoundError:
        print("ERROR SALA_{} CPF: {}".format(sala, cpf))



def sala_14():
    sala = '25'
    cpf = '38019987894'
    cartao = "/run/user/1000/gvfs/smb-share:server=10.112.1.2,share=d$/PROVAS/BOT/SALA_" + sala + "/CARTAO/" + cpf + ".pdf"
    prova = "/run/user/1000/gvfs/smb-share:server=10.112.1.2,share=d$/PROVAS/BOT/SALA_25/PROVA/prova.pdf"
    # impressora = 'RICOH_Aficio_MP_301_002673A52B66_ '  # TI
    impressora = 'ANH-TAU-INF-014 '  # TI

    try:
        if sala == '25':
            s.call(["lp -d " + impressora + cartao], shell=True)
            s.call(["lp -d " + impressora + prova], shell=True)
            print("Imprimindo SALA_{} CPF: {}".format(sala, cpf))

    except FileNotFoundError:
        print("ERROR SALA_{} CPF: {}".format(sala, cpf))