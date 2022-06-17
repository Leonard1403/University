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
a db 10  ; 0ah


b dw 10   ; 000Ah


c dd 10 ; 0000000Ah


d dq  10  ; 000000000000000Ah  (16 cifre hexa)

x db 13   ; x in mem: 0D
y dd 12345678h   ; y in mem: 78 56 34 12

z db 7


; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        mov eax, 0
        mov ebx, 0
        mov ecx, 0
        mov edx, 0
        ; mov, add, sub
        ; mov/add/sub d, s
        ; mov d, s ; d=s
        ; add d, s; d=d+s
        ; sub d, s; d=d-s
        ; op d nu poate fi const  mov 5, [a]  ; add/ sub 5, [a]
        ; ambii op sa fie de aceasi dim (sau de acelasi tip de data)
        ; pentru ca pot aparea err logice
        mov al, [a]  ; cor 
       ; mov bx, [a]  ; err logica
       ; cel putin unul dintre op trebuie sa fie constanta sau registru
      ; mov [a], [z] ;- nu funct
       
       mov byte[a], 9
       mov [a], al
       
       mov al, bl
       
       mov word[b], 14
       
      ; movzx (move with 0 extended)
      
      mov al, 7
      movzx ebx, al  ; al se etinde la doubleword ebx fara semn 
        
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
