loop:
   lda #$81
   sta $6000
   lda #$42
   sta $6000
   lda #$24
   sta $6000
   lda #$18
   sta $6000
   jmp loop

