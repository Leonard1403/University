bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ... fara semn
;(a+b*c*100)/(a+10)+e-d; a,b,c-byte; d-doubleword; e quadword

a db 4
b db 5
c db 3
d dd 1
e dq 10
; our code starts here
segment code use32 class=code
    start:
        ; ...b*c*100
        mov al, [b]
        mul byte [c]  ; ax = b*c
        mov bx, 100
        mul bx   ; dx:ax = b*c*100
        
        ; a byte-> doubleword in comb de reg cx:bx  
        mov bl, [a]
        mov bh, 0
        mov cx, 0  ; cx:bx = a
        
        ; cx:bx+
        ; dx:ax 
        ;_______=
        ;1. bx+ax
        ;2  cx+dx + posibilul transport
        add ax, bx 
        adc dx, cx   ; dx:Ax = ;(a+b*c*100)
        
        ; a+10
        mov bl, 10
        add bl, [a] ; bl = a+10
        
        ; dx:Ax = ;(a+b*c*100)   / bl = a+10
        ; doubleword            / byte 
        ; doubleword            / word
        mov bh, 0
        
        div bx   ; dx:ax / bx   = ax cat si in dx rest
        ; ax = (a+b*c*100)/(a+10)
        
        
       ; (a+b*c*100)/(a+10)+e-d;
       ;                   ax +    e     - d
       ;                   word + quad - doublword
       
       ; ax -> quadword   -> edx:eax
       
       mov bx, ax
       mov eax, 0
       movzx eax, bx
       mov edx, 0   ; edx:eax = (a+b*c*100)/(a+10)
       
       ; e din mem -> ecx:ebx  
       
       
        ;            ecx    :  ebx
       ; pp ca e dq 11223344 55667788h
       ; e in mem:          88    77    66   55    44   33    22   11
       ; adresele lui e:  e+0    e+1    2     3     4    5    6   e+7
       mov ecx,    dword [e+4]    ; transfer 4 bytes (1 doubleword) cu incepere de la adresa lui e+4 in  ecx; ecx = 11223344
       mov ebx,    dword [e+0]  ;                                                              e+0   in ebx ; ebx = 55667788
       
       ; edx:eax  + 
       ; ecx: ebx =
       ; adunare simpla eax, ebx
       ; adunare cu cary  dintre edx, ecx
       add eax, ebx
       adc edx, ecx   ; edx:eax 
       
       ; edx:eax - d
       ; quad    - doublw
       ; d doubleword -> quadword d - > ecx: ebx
       
       mov ebx, [d]
       mov ecx, 0
       
       ; edx:eax -
       ; ecx:ebx = 
       ; scadere simla eax, ebx
       ; scadere cu imprumut dinre edx, ecx
       
       sub eax, ebx
       sbb  edx, ecx   ; rez final in edx:eax
       
        
       
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
