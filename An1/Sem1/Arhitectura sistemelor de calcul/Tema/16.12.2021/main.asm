bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program

import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
import scanf msvcrt.dll

extern exit, printf, scanf

extern baza2in16
;tell nasm that exit exists even if we won't be defining it                          

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    nr dd 0
    n dd 0
    copie db 0
    cit_n db 'n: ', 0
    cit_nr db 'nr: ', 0
    format_citire db '%d', 0
    format_afisare db '%d' ,10, 0
    newline db 10
    

;0011 0101 0101 
;0011
;11
;124098 12409120948 120498 0

; our code starts here
segment code use32 public class=code
    start:
        ; ...
        
        push dword cit_n
        call [printf]
        ADD ESP, 4*1
        
        Push dword n
        push dword format_citire
        call [scanf]
        add esp, 4*2
        
        ;push dword [n]
        ;push dword format_afisare
        ;call [printf]
        ;add esp, 4*2
        
        
        repeta: ;repeta = for
            
            push dword cit_nr
            call [printf]
            add esp, 4*1
            
            push dword nr
            push dword format_citire
            call [scanf]
            add esp, 4*2
            
            push dword [nr]
            call baza2in16
            
            ;push dword [nr]
            ;push dword format_afisare
            ;call [printf]
            ;add esp, 4*2
            
            ;push dword eax
            ;push dword format_afisare
            ;call [printf]
            ;add esp, 4*2
            
            ;push dword [n]
            ;push dword format_afisare
            ;call [printf]
            ;add esp, 4*2
            
            push dword newline
            call [printf]
            add esp, 4*1
            
            mov ecx , dword [n]
            sub ecx , 1
            mov dword [n] , ecx
            cmp ecx , 0
            ;partea de for
        jne repeta
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
