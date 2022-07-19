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
    da dd 83
    citire db '%d' , 0
    div2 dd 2
    mesaj_afisare db 'valoare: ', 0
    afisare_variabile db 'valoare: %d' , 10
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        push dword [da]
        push afisare_variabile
        call [printf]
        add esp, 4*2
        
        ;shr eax , 1
        mov ax , [da]
        and ax , 1111110b
        
        mov [da] , ax
        push dword [da]
        push afisare_variabile
        call [printf]
        add esp, 4*2
        
        mov ax , [da]
        div byte[div2]
        CBW
        mov [da] , ax
        
        push dword [da]
        push afisare_variabile
        call [printf]
        add esp, 4*2
        
        mov ax , [da]
        and ax , 111110b
        
        mov [da] , ax
        push dword [da]
        push afisare_variabile
        call [printf]
        add esp, 4*2
        
        mov ax , [da]
        div byte[div2]
        CBW
        mov [da] , ax
        
        push dword [da]
        push afisare_variabile
        call [printf]
        add esp, 4*2
        
        mov ax , [da]
        and ax , 11110b
        
        mov [da] , ax
        push dword [da]
        push afisare_variabile
        call [printf]
        add esp, 4*2
        
        mov ax , [da]
        div byte[div2]
        CBW
        mov [da] , ax
        
        push dword [da]
        push afisare_variabile
        call [printf]
        add esp, 4*2
        
        mov ax , [da]
        and ax , 1110b
        
        mov [da] , ax
        push dword [da]
        push afisare_variabile
        call [printf]
        add esp, 4*2
        
        mov ax , [da]
        div byte[div2]
        CBW
        mov [da] , ax
        
        push dword [da]
        push afisare_variabile
        call [printf]
        add esp, 4*2
        
        mov ax , [da]
        and ax , 110b
        
        mov [da] , ax
        push dword [da]
        push afisare_variabile
        call [printf]
        add esp, 4*2
        
        
        
        mov ax , [da]
        div byte[div2]
        CBW
        mov [da] , ax
        
        push dword [da]
        push afisare_variabile
        call [printf]
        add esp, 4*2
        
        mov ax , [da]
        and ax , 10b
        
        mov [da] , ax
        push dword [da]
        push afisare_variabile
        call [printf]
        add esp, 4*2
        
        
        ;mov edx , 0
        ;mul word[div2]
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
