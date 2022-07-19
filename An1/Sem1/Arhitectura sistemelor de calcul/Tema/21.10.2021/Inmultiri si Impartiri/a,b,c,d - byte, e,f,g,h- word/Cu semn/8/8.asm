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
    ; 2*(a+b)-e
    
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
        
        MOV AL , [a]
        ADD AL , [b]
        MOV AH , 2
        IMUL AH
        ; AX = 2*(a+b)
        
        MOV BX , AX
        ; BX = 2*(a+b)
        MOV AL , [e]
        ; AL = e
        CBW
        ; AX = e
        SUB BX , AX
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
