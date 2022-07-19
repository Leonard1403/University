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
    ; a,b,c - byte, d - word
    ; 3*[20*(b-a+2)-10*c]+2*(d-3)
    
    a db 1
    b db 2
    c db 1
    d dw 2
    cons20 EQU 20
    
    
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        MOV AL , [b]
        ; AL = b
        SUB AL , [a]
        ; AL = b - a
        ADD AL , 2
        ; AL = b - a + 2
        
        MOV BL , 20
        MUL BL
        ; AX = AL * 20
        ; AX = 20*(b-a+2)
        MOV BX , AX
        ; BX = 20*(b-a+2)
        
        MOV AL , 10
        MUL byte[c]
        ; AX = c * 10
        
        SUB BX , AX
        ; BX = BX - AX
        ; BX = 20*(b-a+2)-10*c
        
        MOV AX , BX
        ; AX = 20*(b-a+2)-10*c
        
        MOV BX , 3
        MUL BX
        ; DX:AX = AX*3
        ; DX:AX = 3*[20*(b-a+2)-10*c]
        
        MOV BX , AX
        MOV CX , DX
        ; CX:BX = 3*[20*(b-a+2)-10*c]
        
        MOV AX , d
        ; AX = d
        SUB AX , 3
        ; AX = d - 3
        MOV BX , 2
        MUL BX
        ; DX:AX = 2*(d-3)
        
        ADD AX , BX
        ADC DX , CX
        
        
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
