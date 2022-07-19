bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
                          
extern exit, fopen, fprintf, fclose, fscanf, printf, scanf 

import exit msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll
import fscanf msvcrt.dll
import fclose msvcrt.dll

import printf msvcrt.dll   
import scanf msvcrt.dll 

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    fisier db 'input.txt', 0
    r db 'r' , 0
    fa dd 0 ; descriptor
    val dd 0
    formathex db '%x ', 0 ; hex read and output
    formatdex db '%d ', 0
    copie_ecx db 0
    copie dd 0
    minim db 0xFFFFF
    div10 dd 10
; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        push dword r
        push dword fisier
        call [fopen]
        add esp, 4*2
        mov [fa] , eax
        cmp dword [fa] , 0
        
        mov ecx , 10
        mov [copie_ecx] , ecx
        je fin
            repeta:
            mov [copie_ecx], ecx
            
            ;citirea valorilor
            push dword val
            push dword formathex
            push dword [fa]
            call [fscanf]
            add esp, 4*3
            
            mov eax, [val]
            mov ecx, 9999999
            cif_min:
                ;mov eax, [val]
                cdq ; eax -> edx:eax
                
                mov ebx , 10
                idiv ebx
                ;mov [val] , eax
                ;edx -> eax%10
                ;eax -> eax/10
                
                cmp ecx , edx
                jl calc
                  mov ecx , edx  
                calc:
                
                cmp eax , 0
            jne cif_min
            
            ;afisare
            push dword ecx
            push dword formatdex
            call [printf]
            add esp, 4*2
            
            mov ecx , [copie_ecx]
            loop repeta
        fin:
        
        push dword [fa]
        call [fclose]
        add esp, 4
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
