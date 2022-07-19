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
    S db 5 , 25 , 55 , 127
    len_S EQU ($-S)
    D times len_S db 0
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov EBX , len_S
        mov ESI , S
        mov EDI , D
        ;CLD
        repeta:
            MOV ECX , 8
            ;LODSB ; AL = i
            MOV AL , [ESI]
            inc ESI 
            MOV DL , AL
            MOV AL , 0
            extractie:
                SHL DL , 1
                ADC AL , 0
            loop extractie        
            ;STOSB
            MOV [EDI] , AL
            inc EDI
        SUB EBX , 1
        CMP EBX , 0
        JNE repeta
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
