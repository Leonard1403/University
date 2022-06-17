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
    ; a byte
    ; b word
    ; c doubleword
    
    ; 1Ah + b - ( c + 0100b - a) + 4
    consth EQU 1Ah
    constb EQU 0100b
    constd EQU 4
    
    a db 2
    b dw 8
    c dd 17
    x dq 1122334455667788h
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        ; 1Ah + b - (c + 0100b - a) + 4
        
        ;1Ah+b
        
        mov ax, consth ; sau mov ax, 1ah
        add ax, [b] ; ax = 1ah + b
        
        ; (c + 0100b - a)
            
            ; c + 0100b
            mov ebx, [c]
            add ebx, constb ; ebx = c + 0100b
            
            
            ; -a
            ;ebx - add
            ;doubleword - byte
            ;convertim pe a de la byte la doubleword 
            mov ecx, byte[a] ; ecx - a convertit
            sub ebx, ecx ; ebx = (c + 0100b - a)
        
        
        
        
        ; 1Ah + b - (c + 0100b - a) + 4
        ;ax  -   ebx
        ;word-   doubleword
        ;convertim word la doubleword
        movzx EAX , ax ; 1Ah + b in eax
        
        sub EAX , EBX ; eax = 1Ah + b - ( c + 0100b - a)
        add eax, 4 ; eax = 1Ah + b - ( c + 0100b -a ) + 4
        
        ; +++++ X quadword
        ; doubleword(eax) + 1 quadword
        
        
        
        
        
        
        
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
