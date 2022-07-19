bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
extern exit, fopen, fprintf, fclose, fscanf , printf
import exit msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll
import printf msvcrt.dll
import fscanf msvcrt.dll
import fclose msvcrt.dll

; our data is declared here (the variables needed by our program)

;Se da un fisier text. Sa se citeasca continutul fisierului, sa se contorizeze numarul de cifre impare si sa se afiseze aceasta valoare. Numele fisierului text este definit in segmentul de date.
segment data use32 class=data
    ; ...
    a dd 0
    val2 dd 2
    val10 dd 10
    copie dq 0
    fisier1 db "in.txt"  , 0
    afisare db "Valoare: %d" , 0
    citire db "%d" , 0
    acces_citire db "r", 0
    descriptor1 dd 0
    descriptor2 dd 0
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        push dword acces_citire   
        push dword fisier1
        call [fopen]
        add esp, 4*2                ; clean-up the stack
        mov [descriptor1], eax  ; store the file descriptor returned by fopen
        
        ; check if fopen() has successfully created the file (EAX != 0)
        cmp eax, 0
        je final
        
        
        push dword a
        push dword citire
        push dword [descriptor1]
        call [fscanf]
        add esp, 4*3
 
        MOV EAX , [a]
        MOV EBX , 0
        
        CDQ ; EAX -> EDX:EAX
   
        ;MOV BX , 10
        
        ax_dif_0:
            MOV [copie+0] , EAX ;copie
            MOV [copie+4] , EDX
            
            IDIV dword[val2] ; AH = AX%2
            
            CMP EDX , 0
            je div_2
                ADD EBX , 1
            div_2:
            
            MOV EAX , [copie+0]
            MOV EDX , [copie+4]
           
            IDIV dword[val10]
            
            
            ;MOV [a] , AX
            ;push dword[a]
            ;push dword afisare
            ;call [printf]
            ;add esp, 4*2
            
            CMP EAX , 0
            
        jne ax_dif_0
         
        mov [a] , EAX
        push dword [a]
        push dword afisare
        call [printf]
        add esp, 4*2
        
        
        push dword [descriptor1]
        call [fclose]
        add esp, 4


      final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
