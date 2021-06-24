# printing mutliplicaion tables

for i in range(2,21):
    with open(f"Mult_table_of_{i}", 'w') as f:
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j}")
            if j != 20:
                f.write('\n')
