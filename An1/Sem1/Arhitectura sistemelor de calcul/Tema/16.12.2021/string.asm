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
    da dd 0
    v10 db 'A' , 0
    v11 db 'B' , 0
    v12 db 'C' , 0
    v13 db 'D' , 0
    v14 db 'E' , 0
    v15 db 'F' , 0
    ;e10 db 10
    ;e11 db 11
    ;e12 db 12
    ;e13 db 13
    ;e14 db 14 
    ;e15 db 15
    len equ 7
    sir times len dd -1
    put dd 1
    restul db 0
    ce db 0 
    rezultat dd 0 
    copie dd 0
    copie_ecx dd 0
    citire db '%d' , 0
    afisare_c db '%c' , 0
    div2 dd 2
    div10 dd 10
    div16 dd 16
    mesaj_afisare db 'valoare: ', 0
    afisare_variabile db 'valoare: %d' , 10
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        push mesaj_afisare
        call [printf]
        add esp, 4
        
        push da
        push citire
        call [scanf]
        add esp , 4*2
        mov ecx , 0
        ;mov ecx , 1 ; puterile lui 2 
        
        repeta:
            mov eax , dword [da]
            cdq
            ;mov edx , [da+4]
            ;mov edx , dword [da+4]
            div dword [div10]
            mov [restul] , edx
            ;cwd
            
            ;mov [da+0] , eax
            ;mov [da+4] , edx
            mov [da] , eax
            ;cmp 
            
            ;-----------------------------------------
            mov eax , [restul]
            ;mov edx , 0
            mul dword [put]
            ;mov [ce] , eax
            
            ;add [rezultat+0] , eax
            ;adc [rezultat+4] , edx
           
            add ecx , eax
            ;mov [rezultat] , ecx

            
            
            
            mov eax , dword [put]
            mul dword [div2]
            mov [put] , eax
            
             
            ;-----------------------------------------
            
            ;push ecx
            ;push afisare_variabile
            ;call [printf]
            ;add esp , 4*2
            
            cmp dword [da] , 0
        jne repeta
        
        ;push ecx
        ;push afisare_variabile
        ;call [printf]
        ;add esp , 4*2
        
        mov eax , ecx ; eax rezultatul
        mov ebx , 0
        mov ecx , 7
        mov edx , 0
        
        mov [copie] , eax
        MOV EDI , sir
        ;MOV ESI , sir 
        CLD
        pentru1:
            mov eax , dword [copie]
            cdq
            
            ;mov edx , 0
            div dword[div16]
            mov [copie] , eax
            mov eax , edx
            STOSD
            
            cmp eax , 0
            je e0
            ;push eax
            ;push afisare_variabile
            ;call [printf]
            ;add esp , 4*2
        loop pentru1
        e0:
        ;mov EDI , sir
        mov eax , 0
        mov ecx , 7
        mov ESI , sir
        STD
        pentru2:
            LODSD
            mov [copie_ecx] , ecx
            mov [copie] , eax
            cmp eax , 0
            je este0 ; eax e 0 sare (NU VREAU SA-MI AFISEZE VAL 0)
            ;CMP EAX , 10
            ;JGE sub10 ;jge destination >= source (signed)
            ;    push eax
            ;    push citire
            ;    call [printf]
            ;    add esp, 4*2
            ;sub10:
            ; 
            ;JNE nueste10
            ;    push v10
            ;    push afisare_c
            ;    call [printf]
            ;    add esp, 4*2
            ;nueste10:
            push dword [copie]
            push afisare_variabile
            call [printf]
            add esp , 4*2
            este0:
            mov ecx , dword [copie_ecx]
        loop pentru2
        
        ;push dword [rezultat]
        ;push afisare_variabile
        ;call [printf]
        ;add esp , 4*2
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
