global  main
extern  printf
bits    64
extern  scanf
default rel

section .data
       info_in_string:  db 'Enter a String: ', 0	 
       info_ou_string:  db 'You entered: ', 0 
       info_in_integer: db 'Enter a number: ', 0
       format:          db "%s", 0
       int_format:      db "%d", 0
       new_line:        db 10, 0 ;print("%s", )
	
section .bss
       input	   resb 1024
       output      resb 1024
       int_input   resb 32
       int_output  resb 32
	
section .text
    main:
	push rbp
	
    call info_ask_input
  
	;scanf, get string
	lea	rdi, [format]
	lea	rsi, [input]	
	mov	rax, 0
    
	call	scanf wrt ..plt

    lea     rdi, [output]           
    lea     rsi, [input]            
    mov     rcx, 1024               
    cld                 
    rep     movsb 
	
    call info_ask_number_input ; show informative text
    call breakLine ; \n

    ;scanf, get integer
	lea	rdi, [int_format]
	lea	rsi, [int_input]	
	mov	rax, 0
	call	scanf wrt ..plt

    lea     rdi, [int_output]           
    lea     rsi, [int_input]            
    mov     rcx, 4               
              
    rep     movsb 

	call print_output_string ; print the string output
    call breakLine ;\n
    call print_output_integer ; print the integer
    call breakLine ;\n
  
	add	rsp, 8
	sub	rax, rax
	ret

info_ask_number_input:
    lea rdi, [format]
    lea rsi, [info_in_integer]
    mov rax, 0
    call printf wrt ..plt
    ret

info_ask_input:
    lea rdi, [format]
    lea rsi, [info_in_string]
    mov rax, 0
    call printf wrt ..plt
    ret

breakLine:

    lea     rdi, [new_line]
    mov     rax, 0
    call    printf wrt ..plt
    ret

print_output_string:
	lea	rdi, [format]
	lea	rsi, [output]
	mov rax, 0
	call	printf wrt ..plt
    ret

print_output_integer:
	lea	rdi, [int_format]
	lea	rsi, [int_output]
	mov rax, 0
	call	printf wrt ..plt