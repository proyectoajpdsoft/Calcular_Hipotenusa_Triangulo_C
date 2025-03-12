#include <stdio.h>
#include <math.h>
#include <conio.h>

int main()
{
  double cateto1, cateto2, hipotenusa;

  printf("\n=================================");
  printf("\nCálculo de la hipotenusa de un Triángulo Rectángulo");
  printf("\n=================================");
  printf("\n\nIntroduzca el valor de un cateto: ");
  scanf("%lf", &cateto1);
  printf("\nIntroduzca el valor del otro cateto: ");
  scanf("%lf", &cateto2);
  
  hipotenusa = sqrt(cateto1 * cateto1 + cateto2 * cateto2);

  printf("\n\nLa hipotenusa es: %lf", hipotenusa);

  printf("\n\n\n\nPulse cualquier tecla para salir.\n");
  getch();

  return 0;
}