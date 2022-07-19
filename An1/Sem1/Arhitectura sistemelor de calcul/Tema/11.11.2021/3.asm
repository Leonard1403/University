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
    S1 db 1 , 2 , 3 , 4
    lenS1 EQU ($-S1)
    S2 db 5 , 6 , 7
    lenS2 EQU ($-S2)
    lenD  EQU lenS1 + lenS2
    D TIMES lenD db 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
    
        ; exit(0)
        
        MOV ESI , S1
        MOV ECX , lenS1
        ;JECXZ final1
        MOV EDI , D
        CLD
        Repeta1:
            LODSB ;AL <- ESI
            STOSB ;EDI <- cifra 
        Loop Repeta1
        ;final1:
        
        MOV ESI, S2
        ADD ESI , lenS2-1
        Mov ECX, lenS2
        ;Jecxz final2
        Repeta2:
            STD
            LODSB ;AL <- ESI
            CLD
            STOSB ;EDI <- cifra
        Loop Repeta2
        ;final2:

        
        
        
        
        
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
