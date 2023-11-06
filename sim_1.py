# chapter 6

# memory
mem = [4, 6, 1, 2, 7, 8, 4, 4, 5]
# registers
num_regs = 8
r = [0]*num_regs
def get_reg_num(token):
    return int(token.replace('r',''))

def add(inst_tokens, registers):
    opcode = inst_tokens[0]
    if 'ADD' in opcode:
        destination_register = get_reg_num(inst_tokens[1])
        operand1_register = get_reg_num(inst_tokens[2])
        operand1 = registers[operand1_register]
        if opcode == 'ADDL':
            operand2 = int (inst_tokens[3])
        else:
            operand2_register = get_reg_num(inst_tokens[3])
            operand2 = registers[operand2_register]
        result = operand1+operand2
        registers[destination_register]=result 
        return True
    else:
        return False 




print(f'Registers: {r}')



#                                 @ Test fetch/execute cycle
#0       LDRL r0 0                @ Load register r0 with 0 (the sum)
#1       LDRL r1 0                @ Load register r1 with 0 (the counter)
#2 Loop  ADDL r1 r1 1             @ REPEAT Increment counter in r1. Loop address = 2
#3       ADD  r0 r0 r1            @ Add the count to the sum in r0
#4       CMPL r1 10               @ Compare the count with 10
#5       BNE  Loop                @ Branch back to Loop until all numbers added (BNE 2)
#6       STOP                     @ Terminate execution
program=['LDRL r0 0','LDRL r1 0','ADDL r1 r1 1','ADD r0 r0 r1','CMPL r1 10', \
      'BNE 2','STOP']

compare_result_is_zero = 0 
run = True 
program_counter = 0

while run == True:
    inst = program[program_counter]
    old_program_counter = program_counter
    program_counter += 1
    inst = inst.split(' ')
    if not add(inst,r):
        if inst[0] == 'BNE':
            if compare_result_is_zero == 0:
                program_counter = int(inst[1])
        elif inst[0] == 'CMPL':
            compare_result_is_zero=0
            register_value = r[int(inst[1][1])]
            literal_value = int(inst[2])
            if register_value == literal_value:
                compare_result_is_zero = 1 
        elif inst[0] == 'LDRL':
            destination_register = int(inst[1][1])
            data = int(inst[2])
            r[destination_register]=data
        elif inst[0] == 'STOP':
            run = False 
            print('End of program reached')
        else:
            run = False 
            print('Error: illegal instruction ',inst)
    print(f'PC = {program_counter}\nRegisters = {r}\ncompare_result_is_zero {compare_result_is_zero}')

