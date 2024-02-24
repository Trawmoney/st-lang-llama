 1from barfi import st_barfi, Block
 2
 3add = Block(name='Addition')
 4sub = Block(name='Subtraction')
 5mul = Block(name='Multiplication')
 6div = Block(name='Division')
 7
 8barfi_result = st_barfi(base_blocks= [add, sub, mul, div])
 9# or if you want to use a category to organise them in the frontend sub-menu
10barfi_result = st_barfi(base_blocks= {'Op 1': [add, sub], 'Op 2': [mul, div]})
