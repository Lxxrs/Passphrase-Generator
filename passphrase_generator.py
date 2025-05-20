import itertools

separators = [' ', '-', '$', '/', '&']
alpha_variations = ['Alpha', 'alpha']
beta_variations = ['beta', 'bet4', 'Beta', 'Bet4']
gamma_variations = ['gamma', 'Gamma', 'gammas', 'Gammas']
delta_variations = ['delta', '']

passwords = []
for alpha in alpha_variations:
    for sep1 in separators:
        for beta in beta_variations:
            for sep2 in separators:
                for gamma in gamma_variations:
                    for delta in delta_variations:
                        if delta == '':
                            passwords.append(f"{alpha}{sep1}{beta}{sep2}{gamma}")
                        else:
                            for sep3 in separators:
                                passwords.append(f"{alpha}{sep1}{beta}{sep2}{gamma}{sep3}{delta}")

# Write the passwords to a file.
with open('password_dict.txt', 'w') as f:
    for password in passwords:
        f.write(f"{password}\n")
