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
    ; a,b,c - byte
    ; d     - word
    ; (100*a + d + 5 - 75*b)/(c-5)
    ; 100 = cons100
    ; 75  = cons75
    
    
    a db 1
    b db 1
    c db 6
    d dw 1
        
    cons100 EQU 100
    cons75  EQU 75

        
        
; our code starts here
segment code use32 class=code
    start:
        
        ; ...
        
        MOV AL,[a]
        MOV AH, cons100
        MUL AH 
        ; AX = AL*      AH
        ; AX = a*cons100
        MOV BX , AX
        ; BX = AX
        ; BX = a*cons100
        MOV AL, cons75
        MOV AH, [b]
        MUL AH
        ; AX = AL*      AH
        ; AX = b*cons75
        MOV CX , AX
        ; CX = AX
        ; CX = b*cons75
        MOV AX,[d]
        ;AX = d
        ADD AX, 5
        ; AX = d + 5
        ADD AX , BX
        ; AX = AX + BX
        ; AX = (a*cons100 + d + 5)
        SUB AX , CX
        ; AX = AX - CX
        ; AX = (a*cons100 + d + 5 - b*cons75)
        MOV CX , AX
        MOV BL , [c]
        ; BL = c
        SUB BL , 5
        ; BL = BL - 5
        ; BL = c - 5
        MOV AX , CX
        DIV BL
        ; AL = AX / BL
        ; AL = (a*cons100 + d + 5 - b*cons75) / (c - 5)
        
        
        
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
