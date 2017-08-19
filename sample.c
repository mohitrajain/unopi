#include<stdio.h>
//uint8_t buf[8] = { 0 };
char ch[5] ;
int t=0;
char *c[52] = {"83000","13021","00000","81000","00017","00000","00018","00000","00023","00000","00008","00000","00019","00000","00004","00000","00007","00000","85000","00040","00000","80750","11011","00000","00008","00000","00015","00000","00015","00000","00018","00000","00044","00000","11026","00000","00018","00000","00021","00000","00015","00000","00007","00000","11030","00000","11030","00000","11030","00000","00040","00000"};
int i = 0,j=0;
int val;
int once = 1;
void setup() {
  //Serial.begin(9600);
  //delay(200);
}
void releaseKey()
{
//buf[0] = 0;
//buf[2] = 0;
//Serial.write(buf, 8); // Release key
}
void main(){
while(once == 1){
  for(j=0;j<52;j++)
  { t = 0;
  for (i=0;i<5;i++)
      ch[t++] = c[j][i];
        val = (ch[0]-48)*10000 + (ch[1]-48)*1000 + (ch[2]-48)*100 + (ch[3]-48)*10 + (ch[4]-48);
        // checking for delay code i.e. 8****
        if(val >= 80000 && val <= 89999){
          //delay(val - 80000);
           printf("code = %d delay for %d \n",val,val - 80000);
               }
        else if(val == 0){
              printf("release key \n");
            //releaseKey();
              printf("delay of 250 milli seconds \n"); 
            //delay(250);
            }
        else{
        //buf[0] = (ch[0]-48) << (ch[1]-48);
        //buf[2] = (ch[2]-48)*100 + (ch[3]-48)*10 + (ch[4]-48);
        //Serial.write(buf,8);
         printf("serial writing %d \n",val);
        }
  }
  once = 2;
}
}
