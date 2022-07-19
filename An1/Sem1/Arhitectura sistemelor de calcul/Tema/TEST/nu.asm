bits 32

segment code use32 public code

global inc1

inc1: 
    mov eax , [esp + 4]
    mov ebx , [esp + 8]
    add eax , ebx
    
    ret 4*2