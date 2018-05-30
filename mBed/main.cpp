#include "mbed.h"
#define acc_add ((uint8_t) 0xA6)
#define gyro_add ((uint8_t) 0xD0)
#include "C12832.h"

//Serial device(dp16, dp15); // tx, rx
C12832 lcd(p5, p7, p6, p8, p11);

I2C i2c(p28, p27);//sda,scl

Serial device(p9, p10);  // tx, rx
int main() 
{
    device.baud(9600); //set baud
    i2c.frequency(100000);
    //acc init
    char cmd[2];
    cmd[0] = 0x31;
    cmd[1] = 0x09;
    i2c.write(acc_add, cmd, 2);
    wait(0.1);
    cmd[0] = 0x2D;
    cmd[1] = 0x08;
    i2c.write(acc_add, cmd, 2);
    wait(0.1);
    //gyro init
    cmd[0] = 0x16;
    cmd[1] = 0x1A;
    i2c.write(gyro_add, cmd, 2);
    wait(0.1);
    cmd[0] = 0x15;
    cmd[1] = 0x09;
    i2c.write(gyro_add, cmd, 2);
    wait(0.1);
    char data[6];
    //lcd.baud(9600);
    int16_t acc_data_raw[3];
    int16_t gyro_data_raw[3];
    float acc_data[3],gyro_data[3];
    float highest = 0.0, lowest = 0.0;
    int select = 1;
    while(1)
    {
        cmd[0]=0x32;
        i2c.write(acc_add, cmd, 1);
        wait(0.001);
        i2c.read(acc_add,data, 6);
        for(int i=0;i<3;i++)
        {
            acc_data_raw[i]= ((data[2*i+1] << 8) | data[2*i]);
            acc_data[i]= (float)(acc_data_raw[i])*0.0383;
        }
        cmd[0]=0x1D;
        i2c.write(gyro_add, cmd, 1);
        wait(0.001);
        i2c.read(gyro_add,data, 6);
        for(int i=0;i<3;i++)
        {
            gyro_data_raw[i]= ((data[2*i] << 8) | data[2*i+1]);
            gyro_data[i]=(float)(gyro_data_raw[i])/14.375;
        }
        lcd.cls();
        lcd.locate(0,3);
        //lcd.printf("ax=%2.2lf",gyro_data[select]);
        //if (gyro_data[select] > highest)
            //highest = gyro_data[select];
        //if (gyro_data[select] < lowest)
            //lowest = gyro_data[select];
        //lcd.printf("\nhigh: %2.2lf", highest); //compare high
        //lcd.printf("\nlow: %2.2lf", lowest); //compare low
        lcd.printf("ax=%2.2lf ay=%2.2lf az=%2.2lf",acc_data[0],acc_data[1],acc_data[2]);
        lcd.printf("\n");
        //lcd.printf("vx=%2.2lf vy=%2.2lf vz=%2.2lf\n",gyro_data[0],gyro_data[1],gyro_data[2]);
        device.printf("x=%2.2lf y=%2.2lf z=%2.2lf\n",acc_data[0],acc_data[1],acc_data[2]);
    }
}
