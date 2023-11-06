# chapter 6

# memory
mem = [4, 6, 1, 2, 7, 8, 4, 4, 5]
# registers
num_regs = 8
r = [0]*num_regs
def get_reg_num(reg_text):
    rnum=None
    if 'r[' in reg_text:
        temp = reg_text.replace('r[','')
        temp = temp.replace(']','')
        temp = int(temp)
        rnum = temp 
    return rnum
    
def do_add(inst_tokens):
    token = inst_tokens[0]
    dest_index = 1
    inst_index = 0 
    op1_index = 2 
    op2_index = 3
    if token == 'add':
        op1= eval(inst_tokens[op1_index])
        op2= eval(inst_tokens[op2_index])
        result = op1 + op2 
        rnum = get_reg_num(inst_tokens[dest_index])
        if rnum:
            r[rnum]=result 


# instruction 
inst = 'add r[4],mem[3],mem[7]'
inst1 = inst.replace(' ',',')
inst_tokens = inst1.split(',')

print(f'Registers: {r}')
do_add(inst_tokens)
print(f'Registers: {r}')

