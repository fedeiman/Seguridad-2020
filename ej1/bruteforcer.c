// Instalar libssl-dev en ubuntu para compilar
// Compilar con gcc -Wall bruteforcer.c -o bruteforcer -lcrypto -lssl
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/md5.h>

// Funcion de stackoverflow para calcular md5 de un string en c
// Credito: "https://stackoverflow.com/questions/7627723/how-to-create-a-md5-hash-of-a-string-in-c"
char *str2md5(const char *str, int length) {
    int n;
    MD5_CTX c;
    unsigned char digest[16];
    char *out = (char*)malloc(33);

    MD5_Init(&c);

    while (length > 0) {
        if (length > 512) {
            MD5_Update(&c, str, 512);
        } else {
            MD5_Update(&c, str, length);
        }
        length -= 512;
        str += 512;
    }

    MD5_Final(digest, &c);

    for (n = 0; n < 16; ++n) {
        snprintf(&(out[n*2]), 16*2, "%02x", (unsigned int)digest[n]);
    }

    return out;
}

int main(void) {
  // El digest de a dos caracteres hexa, ya que 8 bits son 1 char
  char digest[] = {
    0xD7, 0x40, 0xA5, 0xDC, 0x60, 0x7F, 0x78, 0xFB, 0xFF, 0xE5, 0x20, 0xEF, 0xC7,
    0xCA, 0xEB, 0xD2, 0x13, 0x79, 0x40, 0xDD, 0xB2, 0x6C, 0x30, 0xC2, 0xFD, 0x37, 
    0xED, 0x74, 0x3B, 0x77, 0x03, 0x8D, 0x32, 0x6A, 0x9C, 0x7E, 0x7E, 0x80
  };
  int digLen = strlen(digest);
  // Address es unsingned long pq el maximo uint es 0xFFFFFFFF y se queda
  // el for en un loop infinito si no
  unsigned long address;
  // Testeo todas las addresses posibles, la primera es 0x0000066c 
  // por el offset de main
  for(address = 0x0000066c; address < 0xFFFFFFFF; address += 0x1000){
    // Le paso la address como seed a srand
    srand((unsigned int) address);
    // Voy guardando el string que construyo en possibleString
    char possibleString[digLen];
    for(int i = 0; i < digLen; i++){
      // Aplico el xor entre el rand y dos caracteres del digest
      int randN = rand() & 0xff;
      possibleString[i] = (char) (digest[i] ^ randN);
    }
    // Calculo el md5 del string generado
    char *md5str = str2md5(possibleString, digLen);
    // Si el md5 es igual al dado entonces encontre el secreto 
    if(!strcmp(md5str, "080d5caaed95af9ab072c41de3a73c24")){
      // Imprimo el secreto y la seed de srand que funciono
      printf("El secreto es: %s \n",possibleString);
      printf("El address utilizado para srand fue: 0x%X \n", (unsigned int)address);
      //Termino el loop, ya la encontre
      break;
    }
  }
  if (address > 0xFFFFFFFF)
    printf("No se encontro un resultado\n");
return 0;
}