;Se citeste de la tastatura un sir de caractere (litere mici si litere mari, cifre, caractere speciale, etc).
;Sa se formeze un sir nou doar cu literele mici si un sir nou doar cu literele mari. Sa se afiseze cele 2 siruri rezultate pe ecran.



bits 32



;declarare functii externe si variabile



global _functia;functie cunoscuta la nivel global




extern _printf;facem cunoscuta functia din c in programul asm



extern _rez;facem cunoscuta variabila din c in programul asm

;segmentele de date si cod trebuie sa fie publice



segment data public data use32
    
    sir1 dd 0
    sir2 dd 0
    copie dd 0


segment code public code use32



;functia .asm care pune in _rez1 literele mici din sir
_functia:

;Entry code: Crearea cadrului de stiva
    push ebp
    mov ebp,esp

    ;functia(cha s1[], char s2[] , int n);
    ; ebp + 8  = s1
    ; ebp + 12 = s2
    ; ebp + 16 = n
    
    mov eax, [ebp+8]
    mov [sir1], eax
    
    mov eax, [ebp+12]
    mov [sir2], eax
    
    ;mov esi,[ebp+12];la [ebp+12] se afla adresa sirului de caractere citit de la tastatura
    ;mov edi,_rez1
    
    mov ecx,0
    mov ecx , [ebp+16];la [ebp+8] se afla numarul de elemente ale sirului de caractere
    mov [copie],ecx
    
    mov esi, [sir1]
    mov edi,0
    CLD
    repeta:
        lodsb
        mov [_rez+edi], al
        add edi, 2
        
    loop repeta
    
    mov esi, [sir2]
    mov edi, 1
    mov ecx,[copie]
    CLD
    repeta2:
        lodsb
        mov [_rez+edi],al
        add edi, 2
    loop repeta2
    ;Return/Exit Code
    ;refacem cadrul de stiva pentru programul apelant
    mov esp, ebp
    pop ebp
    ret