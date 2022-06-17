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
    a db 4
    b db 5
    c db 3
    d dd 1
    e dq 10
; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        
        
        
        
        ;b*c*100
        mov al, [b]
        mul byte [c] ; ax = b*c*100
        mov bx, 100
        mul bx ; dx:ax = b*c*100
        
        ; a byte -> double word in combinatii
        ;de reg cx:bx
        
        mov bl, [a]
        mov bh, 0
        mov cx, 0 ; cx:bx = a
        
        ; cx:bx + 
        ; dx:ax
        ;________ = 
        ; 1.bx + ax
        ; 2.cx + dx + posibilul transport
        
        add ax, bx
        adc dx, cx ; dx:ax = (a+b*c*100)
        
        ; a + 10
        mov bl, 10
        add bl, [a] ; bl = a + 10
        
        ; dx:ax = (a+b*c*100)   / bl = a+10
        ; double word           / byte
        ; double word           / word
        
        mov bh, 0
        
        div bx ; dx:ax / bx = ax cat si in dx rest
        
        ; (a+b*c*100)/(a+10)+e-data
        ;                       ax +    e       -data
        ;                       word + quad     -double word
        
        ; ax -> quad word   -> edx:eax
        
        mov bx, ax
        mov eax , 0
        movzx eax, bx
        mov edx, 0      ; edx:eax = (a+b*c*100)/(a+10)

        ; e din mem -> ecx:ebx
        
        ; presupunem ca e dq 1122334455667788h
        ; e in mem:         88   77  66   55  44  33  22  11
        ; adresele lui e:   e+0  e+1 e+2  3   4   5   6   e+7
        
        mov ecx,    dword[e+4] ;transfer 4 bytes ( 1 doubleword) cu incepere de la adresa lui e+4 in ecx
        ;ecx = 11223344
        
        mov ebx,    dword[e+0] ;transfer 4 bytes ( 1 doubleword) cu incepere de la adresa lui e+0 in ebx
        ;ebx = 55667788
        
        ; edx:eax + 
        ; ecx:ebx
        ;_________= 
        ;adunare simpla eax , ebx
        ;adunare cu carry dintre edx, ecx
        
        add eax, ebx
        adc edx, ecx ; edx: eax
        
        ;edx:eax - data
        ;quad    - double
        ;d doubleword -> quadword
        ;d -> ecx:ebx
        
        mov ebx, [d]
        mov ecx, 0
        
        ; edx:eax -
        ; ecx:ebx =
        ; scsadere simpla eax, ebx
        ; scadere cu imprumut dintre edx, ecx
        
        sub eax, ebx
        sbb edx, ecx    ;rez final in edx:eax
        
        
        
        
        
        
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program