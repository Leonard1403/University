bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit , printf , scanf               ; tell nasm that exit exists even if we won't be defining it

import scanf msvcrt.dll
import printf msvcrt.dll
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    da dd 0
    valoarea10 db 'A' , 0
    valoarea11 db 'B' , 0
    valoarea12 db 'C' , 0
    valoarea13 db 'D' , 0
    valoarea14 db 'E' , 0
    valoarea15 db 'F' , 0
    ;e10 db 10
    ;e11 db 11
    ;e12 db 12
    ;e13 db 13
    ;e14 db 14 
    ;e15 db 15
    
    poz0 dd 0
    poz1 dd 0
    poz2 dd 0
    poz3 dd 0
    poz4 dd 0
    poz5 dd 0
    poz6 dd 0
    poz7 dd 0
    poz8 dd 0
    
    len equ 7
    sir times len db -1
    put dd 1
    restul db 0
    ce db 0 
    rezultat dd 0 
    copie dd 0
    copie_ecx dd 0
    citire db '%d' , 0
    afisare_c db '%c' , 0
    div2 dd 2
    div10 dd 10
    div16 dd 16
    mesaj_afisare db 'valoare: ', 0
    mesaj_rezultat db 'rezultatul: ', 0
    afisare_variabile db 'valoare: %d' , 10
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        push mesaj_afisare
        call [printf]
        add esp, 4
        
        push dword da
        push dword citire
        call [scanf]
        add esp , 4*2
        mov ecx , 0
        ;mov ecx , 1 ; puterile lui 2 
        
        
        repeta:
            mov eax , dword [da]
            cdq
            ;mov edx , [da+4]
            ;mov edx , dword [da+4]
            div dword [div10]
            mov [restul] , edx
            ;cwd
            
            ;mov [da+0] , eax
            ;mov [da+4] , edx
            mov [da] , eax
            ;cmp 
            
            ;-----------------------------------------
            mov eax , [restul]
            ;mov edx , 0
            mul dword [put]
            ;mov [ce] , eax
            
            ;add [rezultat+0] , eax
            ;adc [rezultat+4] , edx
           
            add ecx , eax
            ;mov [rezultat] , ecx

            
            
            
            mov eax , dword [put]
            mul dword [div2]
            mov [put] , eax
            
             
            ;-----------------------------------------
            
            ;push ecx
            ;push afisare_variabile
            ;call [printf]
            ;add esp , 4*2
            
            cmp dword [da] , 0
        jne repeta
        
        ;push ecx
        ;push afisare_variabile
        ;call [printf]
        ;add esp , 4*2
        
        mov [rezultat] , ecx
        mov eax , ecx ; eax rezultatul
        mov ebx , 0
        ;mov ecx , 7
        mov edx , 0
        
        push dword mesaj_rezultat
        call [printf]
        add esp, 4
        
        mov eax , [rezultat]
        mov ebx , 0 
        mov edx , 0
        
        ;push mesaj_rezultat
        ;call [printf]
        ;add esp, 4
        
        cdq
        div dword [div16]
        ;edx restul
        mov [poz1] , edx
        mov ecx , [poz1]
        cmp eax , 0
        je stop1
        
        cdq
        div dword [div16]
        ;edx restul
        mov [poz2] , edx
        mov ecx , [poz2]
        cmp eax , 0
        je stop2
        
        cdq
        div dword [div16]
        ;edx restul
        mov [poz3] , edx
        mov ecx , [poz3]
        cmp eax , 0
        je stop3
        
        cdq
        div dword [div16]
        ;edx restul
        mov [poz4] , edx
        mov ecx , [poz4]
        cmp eax , 0
        je stop4
        
        cdq
        div dword [div16]
        ;edx restul
        mov [poz5] , edx
        mov ecx , [poz5]
        cmp eax , 0
        je stop5
        
        cdq
        div dword [div16]
        ;edx restul
        mov [poz6] , edx
        mov ecx , [poz6]
        cmp eax , 0
        je stop6
        
        cdq
        div dword [div16]
        ;edx restul
        mov [poz7] , edx
        mov ecx , [poz7]
        cmp eax , 0
        je stop7
        
        cdq
        div dword [div16]
        ;edx restul
        mov [poz8] , edx
        mov ecx , [poz8]
        cmp eax , 0
        je stop8
        
        
        stop8:
        cmp dword [poz8] , 10
        jge j10_8
        push dword [poz8]
        push citire
        call [printf]
        add esp, 4*2
        j10_8:
        
        jne valoarea10_8
            push dword valoarea10
            
            call [printf]
            add esp, 4*2
        valoarea10_8:
        
        cmp dword [poz8] , 11
        jne valoarea11_8
            push dword valoarea11
           
            call [printf]
            add esp, 4*2
        valoarea11_8:
        
        cmp dword [poz8] , 12
        jne valoarea12_8
            push dword valoarea12

            call [printf]
            add esp, 4*2
        valoarea12_8:
        
        cmp dword [poz8] , 13
        jne valoarea13_8
            push dword valoarea13
      
            call [printf]
            add esp, 4*2
        valoarea13_8:
        
        cmp dword [poz8] , 14
        jne valoarea14_8
            push dword valoarea14
        
            call [printf]
            add esp, 4*2
        valoarea14_8:
  
        cmp dword [poz8] , 15
        jne valoarea15_8
            push dword valoarea15
        
            call [printf]
            add esp, 4*2
        valoarea15_8:
 
        
        stop7:
        cmp dword [poz7] , 10
        jge j10_7
        push dword [poz7]
        push citire
        call [printf]
        add esp, 4*2
        j10_7:
        
        jne valoarea10_7
            push dword valoarea10
       
            call [printf]
            add esp, 4*2
        valoarea10_7:
        
        cmp dword [poz7] , 11
        jne valoarea11_7
            push dword valoarea11
      
            call [printf]
            add esp, 4*2
        valoarea11_7:
        
        cmp dword [poz7] , 12
        jne valoarea12_7
            push dword valoarea12
      
            call [printf]
            add esp, 4*2
        valoarea12_7:
        
        cmp dword [poz7] , 13
        jne valoarea13_7
            push dword valoarea13
          
            call [printf]
            add esp, 4*2
        valoarea13_7:
        
        cmp dword [poz7] , 14
        jne valoarea14_7
            push dword valoarea14
         
            call [printf]
            add esp, 4*2
        valoarea14_7:
  
        cmp dword [poz7] , 15
        jne valoarea15_7
            push dword valoarea15
       
            call [printf]
            add esp, 4*2
        valoarea15_7:
        
        
        
        stop6:
        cmp dword [poz6] , 10
        jge j10_6
        push dword [poz6]
        push citire
        call [printf]
        add esp, 4*2
        j10_6:
        
        jne valoarea10_6
            push dword valoarea10
    
            call [printf]
            add esp, 4*2
        valoarea10_6:
        
        cmp dword [poz6] , 11
        jne valoarea11_6
            push dword valoarea11
 
            call [printf]
            add esp, 4*2
        valoarea11_6:
        
        cmp dword [poz6] , 12
        jne valoarea12_6
            push dword valoarea12
           
            call [printf]
            add esp, 4*2
        valoarea12_6:
        
        cmp dword [poz6] , 13
        jne valoarea13_6
            push dword valoarea13
         
            call [printf]
            add esp, 4*2
        valoarea13_6:
        
        cmp dword [poz6] , 14
        jne valoarea14_6
            push dword valoarea14
       
            call [printf]
            add esp, 4*2
        valoarea14_6:
  
        cmp dword [poz6] , 15
        jne valoarea15_6
            push dword valoarea15
          
            call [printf]
            add esp, 4*2
        valoarea15_6:
        
        
        
        stop5:
        cmp dword [poz5] , 10
        jge j10_5
        push dword [poz5]
        push citire
        call [printf]
        add esp, 4*2
        j10_5:
        
        jne valoarea10_5
            push dword valoarea10
          
            call [printf]
            add esp, 4*2
        valoarea10_5:
        
        cmp dword [poz5] , 11
        jne valoarea11_5
            push dword valoarea11
        
            call [printf]
            add esp, 4*2
        valoarea11_5:
        
        cmp dword [poz5] , 12
        jne valoarea12_5
            push dword valoarea12
           
            call [printf]
            add esp, 4*2
        valoarea12_5:
        
        cmp dword [poz5] , 13
        jne valoarea13_5
            push dword valoarea13
          
            call [printf]
            add esp, 4*2
        valoarea13_5:
        
        cmp dword [poz5] , 14
        jne valoarea14_5
            push dword valoarea14
         
            call [printf]
            add esp, 4*2
        valoarea14_5:
  
        cmp dword [poz5] , 15
        jne valoarea15_5
            push dword valoarea15
        
            call [printf]
            add esp, 4*2
        valoarea15_5:
        
        
        
        stop4:
        cmp dword [poz4] , 10
        jge j10_4
        push dword [poz4]
        push citire
        call [printf]
        add esp, 4*2
        j10_4:
        
        jne valoarea10_4
            push dword valoarea10
        
            call [printf]
            add esp, 4*2
        valoarea10_4:
        
        cmp dword [poz4] , 11
        jne valoarea11_4
            push dword valoarea11
         
            call [printf]
            add esp, 4*2
        valoarea11_4:
        
        cmp dword [poz4] , 12
        jne valoarea12_4
            push dword valoarea12
           
            call [printf]
            add esp, 4*2
        valoarea12_4:
        
        cmp dword [poz4] , 13
        jne valoarea13_4
            push dword valoarea13
           
            call [printf]
            add esp, 4*2
        valoarea13_4:
        
        cmp dword [poz4] , 14
        jne valoarea14_4
            push dword valoarea14
         
            call [printf]
            add esp, 4*2
        valoarea14_4:
  
        cmp dword [poz4] , 15
        jne valoarea15_4
            push dword valoarea15
       
            call [printf]
            add esp, 4*2
        valoarea15_4:
        
        
        
        stop3:
        cmp dword [poz3] , 10
        jge j10_3
        push dword [poz3]
        push citire
        call [printf]
        add esp, 4*2
        j10_3:
        
        jne valoarea10_3
            push dword valoarea10
        
            call [printf]
            add esp, 4*2
        valoarea10_3:
        
        cmp dword [poz3] , 11
        jne valoarea11_3
            push dword valoarea11
        
            call [printf]
            add esp, 4*2
        valoarea11_3:
        
        cmp dword [poz3] , 12
        jne valoarea12_3
            push dword valoarea12
           
            call [printf]
            add esp, 4*2
        valoarea12_3:
        
        cmp dword [poz3] , 13
        jne valoarea13_3
            push dword valoarea13
        
            call [printf]
            add esp, 4*2
        valoarea13_3:
        
        cmp dword [poz3] , 14
        jne valoarea14_3
            push dword valoarea14
          
            call [printf]
            add esp, 4*2
        valoarea14_3:
  
        cmp dword [poz3] , 15
        jne valoarea15_3
            push dword valoarea15
    
            call [printf]
            add esp, 4*2
        valoarea15_3:
        
        
        
        stop2:
        cmp dword [poz2] , 10
        jge j10_2
        push dword [poz2]
        push citire
        call [printf]
        add esp, 4*2
        j10_2:
        
        jne valoarea10_2
            push dword valoarea10
        
            call [printf]
            add esp, 4*2
        valoarea10_2:
        
        cmp dword [poz2] , 11
        jne valoarea11_2
            push dword valoarea11
         
            call [printf]
            add esp, 4*2
        valoarea11_2:
        
        cmp dword [poz2] , 12
        jne valoarea12_2
            push dword valoarea12
        
            call [printf]
            add esp, 4*2
        valoarea12_2:
        
        cmp dword [poz2] , 13
        jne valoarea13_2
            push dword valoarea13
      
            call [printf]
            add esp, 4*2
        valoarea13_2:
        
        cmp dword [poz2] , 14
        jne valoarea14_2
            push dword valoarea14
          
            call [printf]
            add esp, 4*2
        valoarea14_2:
  
        cmp dword [poz2] , 15
        jne valoarea15_2
            push dword valoarea15
        
            call [printf]
            add esp, 4*2
        valoarea15_2:
        
        
        
        stop1:
        cmp dword [poz1] , 10
        jge j10_1
        push dword [poz1]
        push citire
        call [printf]
        add esp, 4*2
        j10_1:
        
        jne valoarea10_1
            push dword valoarea10
        
            call [printf]
            add esp, 4*2
        valoarea10_1:
        
        cmp dword [poz1] , 11
        jne valoarea11_1
            push dword valoarea11
       
            call [printf]
            add esp, 4*2
        valoarea11_1:
        
        cmp dword [poz1] , 12
        jne valoarea12_1
            push dword valoarea12
          
            call [printf]
            add esp, 4*2
        valoarea12_1:
        
        cmp dword [poz1] , 13
        jne valoarea13_1
            push dword valoarea13
        
            call [printf]
            add esp, 4*2
        valoarea13_1:
        
        cmp dword [poz1] , 14
        jne valoarea14_1
            push dword valoarea14
        
            call [printf]
            add esp, 4*2
        valoarea14_1:
  
        cmp dword [poz1] , 15
        jne valoarea15_1
            push dword valoarea15
           
            call [printf]
            add esp, 4*2
        valoarea15_1:
        
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
