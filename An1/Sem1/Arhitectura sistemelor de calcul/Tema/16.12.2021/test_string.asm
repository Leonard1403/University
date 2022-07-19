bits 32 ; assembling for the 32 bits architecture
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit , printf , scanf               ; tell nasm that exit exists even if we won't be defining it

import scanf msvcrt.dll
import printf msvcrt.dll
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    valoarea10 db 'A' , 0
    valoarea11 db 'B' , 0
    valoarea12 db 'C' , 0
    valoarea13 db 'D' , 0
    valoarea14 db 'E' , 0
    valoarea15 db 'F' , 0
    
    citire db '%d' , 0
    afisare_c db '%c' , 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        push dword valoarea10
        call [printf]
        add esp, 4*1
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
