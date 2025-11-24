'''cuadrado hecho con asteriscos, altura 8'''
block_size = 3   
blocks_per_row = 8 

for block_row in range(blocks_per_row):
    for line_in_block in range(block_size):
        for block_col in range(blocks_per_row):
            if (block_row + block_col) % 2 == 0:

                for _ in range(block_size):
                    print(" ", end="")
            else:
                for _ in range(block_size):
                    print("*", end="")
        print()  
