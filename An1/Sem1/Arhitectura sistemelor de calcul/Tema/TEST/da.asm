bits 32
global start
import printf msvcrt.dll
import exit msvcrt.dll
import scanf msvcrt.dll
extern printf, exit, scanf

;
extern inc1

segment data use32
    ; ...
    val dd 0
    unu dd 1
    afisare db 'valoare: %d', 0
    mesaj db 'val: ' , 0
    citire db '%d' , 0
    
; our code starts here
segment code use32 public code
    start:
        ; ...
        
        push dword mesaj
        call [printf]
        add esp, 4*1
        
        push dword val
        push dword citire
        call [scanf]
        add esp, 4*2
        
        push dword [val]
        push dword [unu]
        call inc1
        
        push dword eax
        push dword afisare
        call [printf]
        add esp, 4*2
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
