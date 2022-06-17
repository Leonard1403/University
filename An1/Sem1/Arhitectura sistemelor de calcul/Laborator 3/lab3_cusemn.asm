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
    ;(a+b*c*100)/(a+10)+e-d; a,b,c-byte; d-doubleword; e quadword

a db -4
b db -5
c db -3
d dd -1
e dq -10

; aux1 dw 0
; aux2 dw 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;b*c*100
        mov al, [b]
        imul byte[c]   ; ax = b*c
        mov bx, 100
        imul bx ; dx:Ax = b*c*100
        
        ; a   +     dx:ax
        ; byte+doubleword in comb de reg
        
        ; salvare DX:AX in CX:BX sau in variabile auxiliare
        mov cx, dx
        mov bx, ax   ; cx:bx = dx:Ax = b*c*100
            ; sau cu variab auxiliare
            ; mov [aux1], dx
            ; mov [aux2], ax
            
        mov al, [a]
        cbw   
        cwd   ; dx:ax = a
        ; dx:ax +
        ;  cx:bx
        
        add ax, bx
        adc dx, cx   ; dx:ax = (a+b*c*100
        
        
        ; (a+10)
        mov bl, [a]
        add bl, 10
        
        ;;(a+b*c*100)/(a+10)
        ; dx:ax      / bl
        ; dx:ax      / word
        movsx bx, bl
        idiv bx   ; dx:ax / bx = ax - cat si in dx-rest
        ; ax = (a+b*c*100)/(a+10)
        
        ; (a+b*c*100)/(a+10)+e
        ;      ax           + e
        ;      word         + quad
        ; word ax sa fie quad edx:eax
        cwde  
        cdq  
        ; trasnfer e in ecx:ebx
        
        mov ebx, dword[e+0]
        mov ecx, dword[e+4]
        
        ; edx:eax + 
        ; ecx:ebx
        
        add ebx, eax
        adc ecx,edx
        ; ecx:ebx = 
    ; (a+b*c*100)/(a+10)+e
    
    ; (a+b*c*100)/(a+10)+e-d
    ;              quad   - doublword
    ; doublword d trebuie sa fie quad 
    mov eax, [d]
    cdq  ; edx:eax = d
    
    ; ecx:ebx -
    ; edx:eax 
    
    sub ebx, eax
    sbb ecx, edx 
    ; rez final in ecx:ebx
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
