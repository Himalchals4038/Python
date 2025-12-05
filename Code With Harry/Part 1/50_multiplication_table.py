for i in range (2, 21):
    with open(f"tables/Multiplication_table_of_{i}.txt", 'a+') as f:
        for j in range (1, 21):
            f.write(f"{i} X {j} = {i*j}")
            if (j!=20):
                f.write("\n")

