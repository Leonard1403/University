bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    
    ;2/(a+b*c-9)+e-d; a,b,c-byte; d-doubleword; e-qword
    a db 1
    b db 1
    c db 1
    d dd 1
    e dq 1
; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        MOV AL , [b]
        MOV BL , [c]
        MUL BL
        ; AX = AL * BL 
        ; AX = b*c
        mov bl , [a]
        mov bh, 0 
        ADD AX , bx
        ; AX = a+b*c
        
        SUB AX , 9
        ; AX = a+b*c-9
        
        MOV BX , AX
        ; BX = a+b*c-9
        
        MOV AX , 2
        MOV DX , 0
        DIV BX
        ; AX = DX:AX/BX
        ; AX = 2/(a+b*c-9)
        
        MOV bx , ax
        mov eax , 0
        movzx eax , bx
        ; EAX = AX
        MOV EDX , 0
        ; EDX:EAX = EAX
        
        MOV ECX , dword[e+4]
        MOV EBX , dword[e+0]
        
        add ebx , eax
        adc ecx , edx
        ; ecx:ebx = ecx:ebx + edx:eax
        ; ecx:ebx = 2/(a+b*c-9) + e
        
        mov eax , [d]
        mov edx , 0
        
        sub ebx , eax
        sbb ecx , edx
        ; ecx:ebx = ecx:ebx + edx:eax
        ; ecx:ebx = 2/(a+b*c-9) + e
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
