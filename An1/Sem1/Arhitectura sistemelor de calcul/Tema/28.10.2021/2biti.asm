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
    A dw 0000101000101010b
    B dw 0101010101011010b               
    C dd 00000000000000000000000000000000b
    ;Se dau cuvintele A si B. Se cere dublucuvantul C:
    ;bitii 0-3 ai lui C coincid cu bitii 5-8 ai lui B
    ;bitii 4-8 ai lui C coincid cu bitii 0-4 ai lui A
    ;bitii 9-15 ai lui C coincid cu bitii 6-12 ai lui A
    ;bitii 16-31 ai lui C coincid cu bitii lui B
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov dx , [A]
        mov bx , [B]
        mov ecx ,[C]
        ;   0000 1111 0000 0000 0000 0000 0000 0000
        ;  (1234 5678 1234 5678-1234 5678 1234 5678)

        and bx , 0000000111100000b
                ;0   0   0   0   	0   0   0  1  	1  1  1  0  	0  0  0 0b
                ;b15 b14 b13 b12 	b11 b10 b9 b8 	b7 b6 b5 b4 	b3 b2 b1 b0

        mov eax , 0
        movzx eax , bx
        mov ebx , eax
        shr ebx , 5
        or ecx , ebx

        mov ebx , 0
        mov bx , [B]

        and dx , 0000000000011111b
                ;a15 a14 a13 a12 	a11 a10 a9 a8 	a7 a6 a5 a4 	a3 a2 a1 a0
        shl dx, 4
        mov eax, 0
        movzx eax , dx
        mov edx , eax
        or ecx , edx

        mov edx , 0
        mov dx , [A]


        and dx , 0001111111000000b
                ;a15 a14 a13 a12 	a11 a10 a9 a8 	a7 a6 a5 a4 	a3 a2 a1 a0

        ; 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0  0  0  0  0  0  0  0  0  0
        ;c31 c30 c29 c28 c27 c26 c25 c24 c23 c22 c21 c20 c19 c18 c17 c16 c15 c14 c13 c12 c11 c10 c9 c8 c7 c6 c5 c4 c3 c2 c1 c0

        mov eax, 0
        movzx eax , dx
        mov edx , eax
        shl edx , 3

        or ecx , edx
        mov edx , 0
        mov dx , [A]

        ;-----------------------------------------------------------

        mov eax , 0
        movzx eax , bx
        mov ebx , eax
        shl ebx , 16

        or ecx , ebx

        mov ebx , 0
        mov bx , [B]

        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
