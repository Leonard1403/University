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
    afisare db 'mesaj: ', 10
    citire db '%s' , 0
    sir times 101 db 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ax , -1
        mov bh , 1
        idiv bh
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
