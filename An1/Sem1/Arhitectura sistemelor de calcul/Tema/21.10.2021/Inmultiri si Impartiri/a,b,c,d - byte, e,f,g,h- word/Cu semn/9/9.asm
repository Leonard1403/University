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
    
    ; a,b,c,d-byte, e,f,g,h-word
    ; (2*d+e)/a
    
    a db 1
    b db 2 
    c db 0
    d db 1
    
    e dw 1
    f dw 0
    g dw 1
    h dw 0
    
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        MOV AL , [d]
        MOV AH , 2
        IMUL AH
        ; AX = AL *     AH
        ; AX = 2*d
        
        MOV BX , [e]
        ; BX = e
        
        ADD AX , BX
        ; AX = AX + BX
        ; AX = 2*d+e
        
        MOV BL , [a]
        
        IDIV BL
        ; AL = AX / BX
        ; AL = (2*d+e)/a
        
        
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
