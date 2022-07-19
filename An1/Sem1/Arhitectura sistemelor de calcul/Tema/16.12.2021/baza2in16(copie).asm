bits 32
global start
import printf msvcrt.dll
import exit msvcrt.dll
import scanf msvcrt.dll
extern printf, exit, scanf

segment data use32 class = data
    da dd 0
    len equ 8
    sir times len dd 0
    put dd 1
    restul db 0
    ce db 0 
    rezultat dd 0 
    citire db '%d' , 0
    div2 dd 2
    div10 dd 10
    div16 dd 16
    mesaj_afisare db 'valoare: ', 0
    afisare_variabile db 'valoare: %d' , 10

segment code use32 public code

global baza2in16

baza2in16:
    
    ;push mesaj
    ;call [printf]
    ;add esp, 4
    mov eax , [esp + 4] ; eax = am pus numarul
    mov ebx , 1 ; contorizam puterea 
    mov ecx , 0 ; contorizam restul
    mov edx , 0 ; rezultatul 
    
    mov [put] , ebx
    
    mov [da] , eax
    
    
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
        
    mov eax , ecx
    mov ebx , 0
    mov ecx , 8
    mov edx , 0
    
    MOV EDI , sir
    STD
    pentru:
        
    loop pentru
    ;push eax
    ;push afisare_variabile
    ;call [printf]
    ;add esp , 4*2
    
    
    ret 4*1 