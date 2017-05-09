dico = "ABCDEFGHIJKLMNOPQRSTUVWXYZ. :/"
text = "GIMWRJXBDXPRTLCEZ:CFSBIDEQCANCFGSEEFAQOCSSUKRPQAQ/OKSOET"
key = "BEBOP"

output = []
pos_key = 0
for i in range(len(text)) :
    output.append('')
    output[i] = dico[(len(dico) + dico.rfind(text[i]) - dico.rfind(key[pos_key % len(key)])) % len(dico)]
    pos_key += 1

print(''.join(output))

