//#include "autopara.h"
//#include "sdnsim.h"
//#include <cstdlib>
//#include <ctime>
//#include <vector>
//#include <algorithm>
//#include <chrono>
#include <random>
//#include <cstring>
#include <math.h>
#include <iostream>
//#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;

/* void ran_rule_trans3( FlowRuleTable & table, int rad )
{
  for (int j=0; j<=7; ++j)
  {
    if (rad == j)
    {
       table.set(j+1,i,i);
    }
  }

  if (rad == 8)
        {
    table.set(1,i,i);
    table.set(2,i,i);
        }
  if (rad == 9)
        {
    table.set(3,i,i);
    table.set(4,i,i);
        }
  if (rad == 10)
        {
    table.set(5,i,i);
    table.set(6,i,i);
        }
  if (rad == 11)
        {
    table.set(7,i,i);
    table.set(8,i,i);
        }
  if (rad == 12)
        {
    table.set(1,i,i);
    table.set(3,i,i);
        }
  if (rad == 13)
        {
    table.set(2,i,i);
    table.set(4,i,i);
        }
  if (rad == 14)
        {
    table.set(5,i,i);
    table.set(7,i,i);
        }
  if (rad == 15)
        {
    table.set(6,i,i);
    table.set(8,i,i);
        }
  if (rad == 16)
        {
    table.set(1,i,i);
    table.set(5,i,i);
        }
  if (rad == 17)
        {
    table.set(2,i,i);
    table.set(6,i,i);
        }
  if (rad == 18)
        {
    table.set(3,i,i);
    table.set(7,i,i);
        }

  if (rad == 19)
        {
    table.set(4,i,i);
    table.set(8,i,i);
        }

  if (rad == 20)
        {
    table.set(1,i,i);
    table.set(2,i,i);
    table.set(3,i,i);
    table.set(4,i,i);
        }
  if (rad == 21)
        {
    table.set(5,i,i);
    table.set(6,i,i);
    table.set(7,i,i);
    table.set(8,i,i);
        }

  if (rad == 22)
        {
    table.set(1,i,i);
    table.set(2,i,i);
    table.set(5,i,i);
    table.set(6,i,i);
        }

  if (rad == 23)
        {
    table.set(3,i,i);
    table.set(4,i,i);
    table.set(7,i,i);
    table.set(8,i,i);
        }

  if (rad == 24)
        {
    table.set(1,i,i);
    table.set(3,i,i);
    table.set(5,i,i);
    table.set(7,i,i);
        }

  if (rad == 25)
        {
    table.set(2,i,i);
    table.set(4,i,i);
    table.set(6,i,i);
    table.set(8,i,i);
        }

  if (rad == 26)
        {
    table.set(1,i,i);
    table.set(2,i,i);
    table.set(3,i,i);
    table.set(4,i,i);
    table.set(5,i,i);
    table.set(6,i,i);
    table.set(7,i,i);
    table.set(8,i,i);
        }
}

void ran_rule_trans4( FlowRuleTable & table, int rad )
{
  int mnum = 1;
  for (int j=0; j<16; ++j)
  {
    if (rad == j)
    {
      table.set(j+1,i,i);
    }
  }
  for (int j=0; j<8; j++)
  {
    if (rad == 16+j)
    {
      table.set(2*j+1,i,i)；
      table.set(2*j+2,i,i);
    }
  }
  for (int j=0; j<2; j++)
  {
    for (int k=0; k<4; k++)
    {
      if (rad == 24+j+k*2)
      {
        table.set(j+k*4+1,i,i)；
        table.set(j+k*4+3,i,i);
      }
    }
  }
  for (int j=0; j<4; j++)
  {
    for (int k=0; k<2; k++)
    {
      if (rad == 32+j+k*4)
      {
        table.set(j+k*8+1,i,i)；
        table.set(j+k*8+5,i,i);
      }
    }
  }
  for (int j=0; j<8; j++)
  {
    if (rad == 40+j)
    {
      table.set(j+1,i,i)；
      table.set(j+9,i,i);
    }
  }
  for (int j=0; j<4; j++)
  {
    if (rad == 48+j)
    {
      table.set(j*4+1,i,i)；
      table.set(j*4+2,i,i);
      table.set(j*4+3,i,i);
      table.set(j*4+4,i,i);
    }
  }
  if (rad == 52)
  {
    table.set(1,i,i)；
    table.set(j*4+2,i,i);
    table.set(j*4+3,i,i);
    table.set(j*4+4,i,i);
  }
  for (int j=0; j<4; j++)
  {
    if (rad == 52+j)
    {
      table.set(1,i,i)；
      table.set(j*4+2,i,i);
      table.set(j*4+3,i,i);
      table.set(j*4+4,i,i);
    }
  }




  for (int j=0; j<4; ++j)
  {
    mnum = pow(2, j);
    for (int k=0; k<8; k++)
    {
      if (rad == 16+j*8+k)
      {
        table.set(k*mnum+1,i,i)；
        table.set(k*mnum+mnum+1,i,i);
      }
    }
  }

}
  for (int j=0; j<4; ++j)
  {
    mnum = pow(2, j);
    for (int k=0; k<8; k++)
    {
      table.set(k+1,i,i)；
    }
    if (rad == j)
    {

    }
  }
  for (int j=0; j<=7; ++j)
  {
    if (rad == j)
    {
       table.set(j+1,i,i);
    }
  }

  if (rad == 8)
        {
    table.set(1,i,i);
    table.set(2,i,i);
        }
  if (rad == 9)
        {
    table.set(3,i,i);
    table.set(4,i,i);
        }
  if (rad == 10)
        {
    table.set(5,i,i);
    table.set(6,i,i);
        }
  if (rad == 11)
        {
    table.set(7,i,i);
    table.set(8,i,i);
        }
  if (rad == 12)
        {
    table.set(1,i,i);
    table.set(3,i,i);
        }
  if (rad == 13)
        {
    table.set(2,i,i);
    table.set(4,i,i);
        }
  if (rad == 14)
        {
    table.set(5,i,i);
    table.set(7,i,i);
        }
  if (rad == 15)
        {
    table.set(6,i,i);
    table.set(8,i,i);
        }
  if (rad == 16)
        {
    table.set(1,i,i);
    table.set(5,i,i);
        }
  if (rad == 17)
        {
    table.set(2,i,i);
    table.set(6,i,i);
        }
  if (rad == 18)
        {
    table.set(3,i,i);
    table.set(7,i,i);
        }

  if (rad == 19)
        {
    table.set(4,i,i);
    table.set(8,i,i);
        }

  if (rad == 20)
        {
    table.set(1,i,i);
    table.set(2,i,i);
    table.set(3,i,i);
    table.set(4,i,i);
        }
  if (rad == 21)
        {
    table.set(5,i,i);
    table.set(6,i,i);
    table.set(7,i,i);
    table.set(8,i,i);
        }

  if (rad == 22)
        {
    table.set(1,i,i);
    table.set(2,i,i);
    table.set(5,i,i);
    table.set(6,i,i);
        }

  if (rad == 23)
        {
    table.set(3,i,i);
    table.set(4,i,i);
    table.set(7,i,i);
    table.set(8,i,i);
        }

  if (rad == 24)
        {
    table.set(1,i,i);
    table.set(3,i,i);
    table.set(5,i,i);
    table.set(7,i,i);
        }

  if (rad == 25)
        {
    table.set(2,i,i);
    table.set(4,i,i);
    table.set(6,i,i);
    table.set(8,i,i);
        }

  if (rad == 26)
  {
    table.set(1,i,i);
    table.set(2,i,i);
    table.set(3,i,i);
    table.set(4,i,i);
    table.set(5,i,i);
    table.set(6,i,i);
    table.set(7,i,i);
    table.set(8,i,i);
  }
}

int wild_count()
{

}
*/

static inline long int pow2(int y) {
  long int rv = 1;
  for (int i = 0; i < y; i++)
  {
    rv = rv * 2;
  }
  return rv;
}


void dec2bin(int *cursor, long int num, int size)
{
  while ( size > 0 )
  {
    size--;
    *cursor = num / pow2(size);
    num = num % pow2(size);
    if ( size > 0 )
      cursor++;
  }

}


int wild_count( int *array, int size )
{
  int ct = 0;
  while ( size > 0 )
  {
    if ( *array > 0 )
      ct++;
    size--;
    if ( size > 0 )
      array++;
  }
  return ct;
}


void wild_count_trans( int *wild, int num_w, int size, int wild_size )
{
  int *wild_num = (int *) malloc(size * sizeof(int));
  int ct = -1;
  int num = 0;
  while ( ct < num_w )
  {
    dec2bin( wild_num, num, size );
    if ( wild_count( wild_num, size ) == wild_size )
      ct++;
    num++;
  }
  int k = 0;
  for (int i = 0; i < size; i++)
  {
    if ( *(wild_num+i) > 0)
    {
      *(wild+k)= i;
      k++;
    }
  }
  free(wild_num);
}





long int nChoosek( int n, int k )
{
    if (k > n) return 0;
    if (k * 2 > n) k = n-k;
    if (k == 0) return 1;

    long int result = n;
    for( int i = 2; i <= k; ++i ) {
        result *= (n-i+1);
        result /= i;
    }
    return result;
}


void print_array( int *array, int size )
{
  if (!array)
   return;
  for ( int i = 0; i < size; i++ )
    cout << *(array + i);
  cout << endl;
}


long int bin2dec( int *array, int size )
{
  long int rt = 0;
  while ( size > 0 )
  {
    size--;
    rt = rt + (*array) * pow2(size);
    if ( size > 0 )
      array++;
  }
  return rt;
}

void ran_rule_trans( int *table, int rad, int size, int rule_num)
{
  for ( int i = 0; i <= size; i++ )
  {
    if ( pow2(size - i) * nChoosek( size, i ) < rad + 1 )
      rad = rad - pow2(size - i) * nChoosek( size, i );
    else
    {
      if ( i == 0 )
      {
        *(table+rad) = rule_num; // ip address
        return;
      }

      if ( size == i )
      {
        for ( int h = 0; h < pow2(size); h++ )
        {
          *(table+h) = rule_num; // ip address
        }
        return;
      }
      int *addr = (int *) malloc( (size-i) * sizeof(int) );
      int *wild = (int *) malloc( i * sizeof(int) );
      int *wild_idx = (int *) malloc( i * sizeof(int) );
      int *table_num = (int *) malloc( size * sizeof(int) );
      int k1,k2,k;
      int table_idx;
      dec2bin( addr, rad % pow2(size-i), size-i );

      wild_count_trans( wild_idx, rad / pow2(size-i), size, i );

      print_array(addr, size-i);
      print_array(wild_idx, i);
      for ( int j = 0; j < pow2(i); j++ )
      {
        dec2bin( wild, j, i );
        k1 = 0;
        k2 = 0;
        k = 0;
        while ( k < size )
        {
          if ( k == *(wild_idx+k2) )
          {
            *(table_num+k) = *(wild+k2);
            k2++;
          }
          else
          {
            *(table_num+k) = *(addr+k1);
            k1++;
          }
          k++;
        }
        table_idx = bin2dec( table_num, size );
        *(table + table_idx) = -1; // ip address
      }

      free(addr);
      free(table_num) ;
      free(wild_idx);
      free(wild);
  //    table_set_random( table, addr, size-i, wild, i );
      return;
    }
  }
}


int main()
{
  int array[4];
  int size = 4;
  dec2bin(array, 7, size);
  for (int i = 0; i < size; i++)
    cout << array[i];
  cout << endl;
  cout << bin2dec(array, size);
  cout << wild_count(array, size) << endl;
  cout << nChoosek( 6, 3 ) << endl;

  int row = 4;
  int col = 4;
  int *table = (int *) malloc(row*col*sizeof(int));
  for ( int i = 0; i < row; i++ )
    for ( int j = 0; j <col; j++ )
    {
      *(table + i*col + j) = i*col + j;
    }


  for ( int i = 0; i < row; i++ )
    {
      for ( int j = 0; j < col; j++ )
      {
        cout << *(table + i*col + j);
      }
      cout << endl;
    }


  ran_rule_trans( table,40, 4, -1 );

  for ( int i = 0; i < row; i++ )
    {
      for ( int j = 0; j < col; j++ )
      {
        cout << *(table + i*col + j);
      }
      cout << endl;
    }

  return 0;
}
