bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, scanf; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
import scanf msvcrt.dll
                          
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a dd 0
    b dd 0
    rezultat dd 0
    
    cit_a db 'a = ', 0
    cit_b db 'b = ', 0
    format_citire db '%d', 0
    format_afisare db '%d * %d = %d' , 
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        push dword cit_a
        Call [printf]
        ADD esp, 4*1
        
        ;scanf("%d,a)
        Push dword a
        Push dword format_citire
        Call [scanf]
        Add esp, 4*2
        
        
        
        push dword cit_b
        Call [printf]
        ADD esp, 4*1
        
        ;scanf("%d,b)
        Push dword b
        Push dword format_citire
        Call [scanf]
        Add esp, 4*2
        
        mov AX , word [a]
        mov BX , word [b]
        
        IMUL BX
        MOV word[rezultat+0] , AX ; transfer continut DX:AX in rezultat
        Mov word[rezultat+2] , DX
        
        
        push dword [rezultat]
        push dword [b]
        push dword [a]          
        push dword format_afisare
        call [printf]
        add esp, 4*4
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
