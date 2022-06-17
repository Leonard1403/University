;Se da un sir de quadworduri definit in data segment
;elementele sirului sunt in baza16
; a)sa se printeze byti care compun quadwordurile din sir
; b)sa se identifice wordurile care au ultima cifra egala cu constanta k 
;   definita in segmentul de date
;   sa se salveze aceste worduri in sirul d
; c)sa se identifice double wordurile care sunt cuprinse in intervalul
;   [AAA , FFFF]
;   sa se determine numarul double wordurilor din acest intervl; sa se afiseze
;   acest numar in baza10 in fisierul iesire.txt



bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
extern printf

import printf msvcrt.dll
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll

                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    sir dq 0x1248 , 0x1289 , 0x12 , 0x875 , 0x129, 0x8325 , 0x0AABC , 0xABCBACACBA , 0x9
    len_sir equ ($-sir)/8
    formathex db '%x' , 10
    format_n db '' , 10
    copie dw 0
    copie2 dw 0
    a dd 0
    b dd 0 
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ecx , len_sir
        mov esi , sir
        mov ebx , 8
        
        CLD
        repeta:
            mov [copie] , ecx
            mov ecx , 8
            ;bucla:
            ;    mov [copie2] , ecx
            ;    lodsb
            ;    cbw 
            ;    cwd
            ;    push dword eax
            ;    push dword formathex
            ;    call [printf]
            ;    add esp, 4*2
            ;    ;mov edx , eax 
            ;    ;lodsd
            ;    mov ecx , [copie2]
            ;loop bucla
            lodsd
            mov edx , eax
            lodsd
            
            mov [a] , eax
            mov [b] , edx
            
            push dword[a]
            push dword formathex
            call [printf]
            add esp , 4*2
            
            push dword[b]
            push dword formathex
            call [printf]
            add esp , 4*2
            
            mov ecx , [copie]
        loop repeta
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
