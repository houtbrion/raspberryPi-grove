# raspberryPi-grove
seeed studio grove module software for raspberry pi

## 目的
* seeed studioのwikiに公開されている各種サンプルプログラムをgitでまとめて管理できるようにする．
* 1つのgroveモジュールに対して，1つのプログラムが対応するように整理し直す． (一部のサンプルプログラムは複数のモジュールに依存しているため)

Seeed StudioのGrovePi+の
[公式Wiki](
http://www.seeedstudio.com/wiki/GrovePi%2B
"公式Wiki")
にはサポートされているモジュールは以下のものだけとある．

* Grove - Button
* Light Sensor
* Buzzer
* Sound Sensor
* Grove - Red LED
* Grove - Blue LED
* Grove - Green LED
* LCD RGB Backlight
* Rotary Angle Sensor
* Temperature Humidity Sensor
* Ultrasonic Ranger Sensor
* Relay


## 音関係

### Grove - Buzzer
* [製品情報](http://www.seeedstudio.com/depot/grove-buzzer-p-768.html?cPath=156_159 "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Buzzer "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/
Buzzer
/
Buzzer
.py
"サンプルプログラム")は本プロジェクトの「
Buzzer
/
Buzzer
.py」にも収録．


### Grove - Sound Sensor
* [製品情報](http://www.seeedstudio.com/depot/grove-sound-sensor-p-752.html?cPath=144_148 "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/index.php?title=Twig_-_Sound_Sensor "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/
Sound_Sensor
/
Sound_Sensor
.py
"サンプルプログラム")は本プロジェクトの「
Sound\_Sensor
/
Sound\_Sensor
.py」にも収録．

### 音量センサ
* [製品情報](http://www.seeedstudio.com/depot/Grove-Loudness-Sensor-p-1382.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Loudness_Sensor "技術情報")

Seeed StudioのGrovePi+の
[公式Wiki](
http://www.seeedstudio.com/wiki/GrovePi%2B
"公式Wiki")には，このモジュールはサポート対象外とあるが，
Sound Sensorのサンプルプログラムでこのセンサも動作を確認することができた．

## 位置や動作関係

### Grove - Button
* [製品情報](http://www.seeedstudio.com/depot/grove-button-p-766.html?cPath=156_160 "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Button "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/Button/Button.py
"サンプルプログラム") 
は本プロジェクトの「
button
/
button
.py」．

### Grove - Rotary Angle Sensor
* [製品情報](http://www.seeedstudio.com/depot/grove-rotary-angle-sensor-p-p-1242.html?cPath=156_160 "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Rotary_Angle_Sensor "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/
Rotary_Sensor
/
Rotary_Sensor
.py
"サンプルプログラム") 
は本プロジェクトの「
Rotary\_Sensor
/
Rotary\_Sensor
.py」．

### ボリューム
* [製品情報](http://www.seeedstudio.com/depot/Grove-Rotary-Angle-Sensor-p-770.html?cPath=85_52 "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Rotary_Angle_Sensor "技術情報")

Seeed StudioのGrovePi+の
[公式Wiki](
http://www.seeedstudio.com/wiki/GrovePi%2B
"公式Wiki")には，このモジュールはサポート対象外とあるが，
「Grove - Rotary Angle Sensor」
のサンプルプログラムでこのセンサも動作を確認することができた．

### ボリューム(パネルタイプ)
* [製品情報](http://www.seeedstudio.com/depot/Grove-Rotary-Angle-SensorP-p-1242.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Rotary_Angle_Sensor "技術情報")

Seeed StudioのGrovePi+の
[公式Wiki](
http://www.seeedstudio.com/wiki/GrovePi%2B
"公式Wiki")には，このモジュールはサポート対象外とあるが，
「Grove - Rotary Angle Sensor」
のサンプルプログラムでこのセンサも動作を確認することができた．

### スライドボリューム
* [製品情報](http://www.seeedstudio.com/depot/Grove-Slide-Potentiometer-p-1196.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Sliding_Potentiometer "技術情報")

Seeed StudioのGrovePi+の
[公式Wiki](
http://www.seeedstudio.com/wiki/GrovePi%2B
"公式Wiki")には，このモジュールはサポート対象外とあるが，
「Grove - Rotary Angle Sensor」
のサンプルプログラムでこのセンサも動作を確認することができた．

## ユーザインタフェース

## 表示関係

### 赤色LED
* [製品情報](http://www.seeedstudio.com/depot/Grove-Red-LED-p-1142.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_LED "技術情報")

技術情報のWikiに記載されているサンプルプログラムで動作を確認することができた．

使用した
[サンプルプログラム] (
https://github.com/houtbrion/raspberryPi-grove/blob/master/LED/LED.py
"サンプルプログラム")
は本プロジェクトの「LED/LED.py」にも収録．


### Grove - LCD RGB Backlight
* [製品情報](http://www.seeedstudio.com/depot/Grove-LCD-RGB-Backlight-p-1643.html?cPath=34_36 "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_LCD_RGB_Backlight "技術情報")


使用した
[サンプルプログラム] (
https://github.com/houtbrion/raspberryPi-grove/blob/master/
LCD_RGB_BackLight
/
LCD_RGB_BackLight
.py
"サンプルプログラム")
は本プロジェクトの「
LCD\_RGB\_BackLight
/
LCD\_RGB\_BackLight
.py」にも収録．


## 環境関係

### Grove - Light Sensor
* [製品情報](http://www.seeedstudio.com/depot/Grove-Light-Sensor-p-746.html?cPath=25_27 "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Light_Sensor "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/
Light_Sensor
/
Light_Sensor.py
"サンプルプログラム")は本プロジェクトの「
Light\_Sensor
/
Light\_Sensor.py
」にも収録．

### デジタル温度・湿度センサ
* [製品情報](http://www.seeedstudio.com/wiki/Grove-_Temperature_and_Humidity_Sensor "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove-_Temperature_and_Humidity_Sensor "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/
DHT
/
DHT
.py
"サンプルプログラム")は本プロジェクトの「
DHT
/
DHT
」にも収録．



## その他

### Grove - Smart Relay
* [製品情報](http://www.seeedstudio.com/depot/grove-relay-p-769.html?cPath=156_160 "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Relay "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/
Relay
/
Relay
.py
"サンプルプログラム")は本プロジェクトの「
Relay
/
Relay
.py
」にも収録．


## seeed studioのWikiでサンプルプログラムが提供されていない

## サンプルプログラムが動かない

# トライ中

## 音関係

## 位置や動作関係
### ロータリーエンコーダ
* [製品情報](http://www.seeedstudio.com/depot/Grove-Encoder-p-1352.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Encoder "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

## ユーザインタフェース

## 表示関係

## 環境関係

## その他

# seeed studioのWikiでサンプルプログラムが提供されていない

## 音関係

### スピーカー
* [製品情報](http://www.seeedstudio.com/depot/Grove-Speaker-p-1445.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Speaker "技術情報")


# サンプルプログラムが動かない



# 試してない

## 位置や動作関係

### Grove - Touch Sensor
* [製品情報](http://www.seeedstudio.com/depot/grove-touch-sensor-p-747.html?cPath=156_160 "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/index.php?title=Twig_-_Touch_Sensor "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### 3軸デジタルコンパス
* [製品情報](http://www.seeedstudio.com/depot/Grove-3Axis-Digital-Compass-p-759.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_3-Axis_Compass_V1.0 "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### 3軸デジタル加速度センサ(ADXL345)
* [製品情報](http://www.seeedstudio.com/depot/Grove-3Axis-Digital-Accelerometer16g-p-1156.html?cPath=25_132 "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_3-Axis_Digital_Accelerometer_ADXL345 "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### 3軸アナログ加速度センサ
* [製品情報](http://www.seeedstudio.com/depot/Grove-3Axis-Analog-Accelerometer-p-1086.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Breakout_-_3-Axis_Analog_Accelerometer_ADXL335 "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### I2C 3軸デジタル加速度センサ
* [製品情報](http://www.seeedstudio.com/depot/Grove-3Axis-Digital-Accelerometer15g-p-765.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_3-Axis_Digital_Accelerometer(%C2%B11.5g) "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### I2C 3軸ジャイロセンサ
* [製品情報](http://www.seeedstudio.com/depot/Grove-3Axis-Digital-Gyro-p-750.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_3-Axis_Digital_Gyro "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### 1軸ジャイロセンサ
* [製品情報](http://www.seeedstudio.com/depot/Grove-Single-Axis-Analog-Gyro-p-1451.html?cPath=25_133 "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Single_Axis_Analog_Gyro "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### PIRモーションセンサ
* [製品情報](http://www.seeedstudio.com/depot/Grove-PIR-Motion-Sensor-p-802.html "製品情報")
* [技術情報](http://garden.seeedstudio.com/index.php?title=Twig_-_PIR_Motion_Sensor "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### GPS
* [製品情報](http://www.seeedstudio.com/depot/Grove-GPS-p-959.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_GPS "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### GSR
* [製品情報](http://www.seeedstudio.com/depot/Grove-GSR-sensor-p-1614.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_GSR_Sensor "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

## ユーザインタフェース

### シリアルカメラキット
* [製品情報](http://www.seeedstudio.com/depot/Grove-Serial-Camera-Kit-p-1608.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Serial_Camera_Kit "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### I2Cタッチセンサ
* [製品情報](http://www.seeedstudio.com/depot/Grove-I2C-Touch-Sensor-p-840.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_I2C_Touch_Sensor "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### 親指ジョイスティック
* [製品情報](http://www.seeedstudio.com/depot/Grove-Thumb-Joystick-p-935.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Thumb_Joystick "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### ボタン
* [製品情報](http://www.seeedstudio.com/depot/Grove-Button-p-766.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Button "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．


## 表示関係

### Grove - LED
* [製品情報](http://www.seeedstudio.com/depot/Grove-LED-p-767.html?cPath=81_35 "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/index.php?title=GROVE_-_Starter_Kit_v1.1b#Grove_-_LED "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### LEDバー

* [製品情報](http://www.seeedstudio.com/depot/Grove-LED-Bar-p-1178.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_LED_Bar "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### サークル型LED
* [製品情報](http://www.seeedstudio.com/depot/Grove-Circular-LED-p-1353.html?cPath=81_35 "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Circular_LED "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### RGB LED
* [製品情報](http://www.seeedstudio.com/depot/Grove-Chainable-RGB-LED-p-850.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/index.php?title=Twig_-_Chainable_RGB_LED "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### 7セグメント4桁ディスプレイ
* [製品情報](http://www.seeedstudio.com/depot/Grove-4Digit-Display-p-1198.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_4-Digit_Display "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### OLED display 1.12inch
* [製品情報](http://www.seeedstudio.com/depot/Grove-OLED-Display-112-p-781.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_OLED_Display_128*64 "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

## 環境関係

### Grove - Temperature Sensor
* [製品情報](http://www.seeedstudio.com/depot/grove-temperature-sensor-p-774.html?cPath=144_147 "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Temperature_Sensor_V1.2 "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### I2C 気圧センサ(BMP180)

* [製品情報](http://www.seeedstudio.com/depot/Grove-Barometer-Sensor-BMP180-p-1840.html?cPath=25_124 "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Barometer_Sensor_(BMP180) "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### I2C デジタル光センサ
* [製品情報](http://www.seeedstudio.com/depot/Grove-Digital-Light-Sensor-p-1281.html?cPath=25_128 "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Digital_Light_Sensor "技術情報")


### デジタル温度・湿度センサ pro
* [製品情報](http://www.seeedstudio.com/depot/Grove-TemperatureHumidity-Sensor-Pro-p-838.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Temperature_and_Humidity_Sensor_Pro "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### 火炎センサ
* [製品情報](http://www.seeedstudio.com/depot/Grove-Flame-Sensor-p-1450.html"製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Flame_Sensor "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### 光センサ(パネルタイプ)
* [製品情報](http://www.seeedstudio.com/depot/Grove-Light-SensorP-p-1253.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Light_Sensor "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### 水センサ
* [製品情報](http://www.seeedstudio.com/depot/Grove-Water-Sensor-p-748.html?cPath=25_27 "製品情報")
* [技術情報](http://garden.seeedstudio.com/index.php?title=Twig_-_Water_Sensor "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### 水分センサ
* [製品情報](http://www.seeedstudio.com/depot/Grove-Moisture-Sensor-p-955.html "製品情報")
* [技術情報](http://seeedstudio.com/wiki/Grove_-_Moisture_Sensor "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### Ultrasonic Ranger
* [製品情報](http://www.seeedstudio.com/depot/Grove-Ultrasonic-Ranger-p-960.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Ultrasonic_Ranger "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### 磁気スイッチ
* [製品情報](http://www.seeedstudio.com/depot/Grove-Magnetic-Switch-p-744.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/index.php?title=Twig_-_Magnetic_Switch "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

## その他

### 電流センサ
* [製品情報](http://www.seeedstudio.com/depot/Grove-Electricity-Sensor-p-777.html?cPath=25_28 "製品情報")
* [技術情報](http://garden.seeedstudio.com/index.php?title=Twig_-_Electricity_Sensor "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### RTC
* [製品情報](http://www.seeedstudio.com/depot/Grove-RTC-p-758.html?cPath=25_131 "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_RTC "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### スイッチ(P)
* [製品情報](http://www.seeedstudio.com/depot/Grove-SwitchP-p-1252.html "製品情報")


### 赤外線反射センサ
* [製品情報](http://www.seeedstudio.com/depot/Grove-Infrared-Reflective-Sensor-p-1230.html?cPath=25_31 "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Infrared_Reflective_Sensor "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### 赤外線距離センサ
* [製品情報](http://www.seeedstudio.com/depot/Grove-IR-Distance-Interrupter-p-1278.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_IR_Distance_Interrupt "技術情報")


使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### ラインファインダ
* [製品情報](http://www.seeedstudio.com/depot/Grove-Line-Finder-p-825.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/index.php?title=Twig_-_Line_Finder "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### 赤外線送受信機
####受信機
* [製品情報](http://www.seeedstudio.com/depot/Grove-Infrared-Receiver-p-994.html"製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Infrared_Receiver "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

#### 発信機
* [製品情報](http://www.seeedstudio.com/depot/Grove-Infrared-Emitter-p-993.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Infrared_Emitter "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### 端子台
* [製品情報](http://www.seeedstudio.com/depot/Grove-Screw-Terminal-p-996.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Screw_Terminal "技術情報")

### I2Cハブ
* [製品情報](http://www.seeedstudio.com/depot/Grove-I2C-Hub-p-851.html "製品情報")
* [技術情報](http://garden.seeedstudio.com/index.php?title=Twig_-_I2C_Hub "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### Xbee Carrier
* [製品情報](http://www.seeedstudio.com/depot/Grove-XBee-Carrier-p-905.html "製品情報")
* [技術情報](http://garden.seeedstudio.com/index.php?title=Bee_Stem "技術情報")


# 調査中
購入したモジュールの中で動作が確認できていないものは以下のとおり．
電流センサ以外はハードの故障の可能性がある．

電流センサは測定用の配線材料を買わないと行けないのでしばらく動作確認不能．

しかし，ハードの初期不良だとすると発生頻度が高い．
ソフト的な問題にしても情報がなさすぎて
DEBUG困難．

##音関係

### Serial MP3 Player
* [製品情報](http://www.seeedstudio.com/depot/Grove-Serial-MP3-Player-p-1542.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_%E2%80%93_Serial_MP3_Player "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

## 位置や動作

### 3軸デジタル加速度センサ(H3LI331DL)
* [製品情報](http://www.seeedstudio.com/depot/Grove-3Axis-Digital-Accelerometer400g-p-1897.html?cPath=25_132 "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_3-Axis_Digital_Accelerometer(%C2%B1400g) "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

## 環境

### アルコールセンサ
* [製品情報](http://www.seeedstudio.com/depot/Grove-Alcohol-Sensor-p-764.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/index.php?title=Twig_-_Alcohol_Sensor "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

## その他
### I2C ADC
* [製品情報](http://www.seeedstudio.com/depot/Grove-I2C-ADC-p-1580.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_I2C_ADC "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．

### チルトスイッチ
* [製品情報](http://www.seeedstudio.com/depot/Grove-Tilt-Switch-p-771.html "製品情報")
* [技術情報](http://www.seeedstudio.com/wiki/Grove_-_Tilt_Switch "技術情報")

使用した
[サンプルプログラム](
https://github.com/houtbrion/raspberryPi-grove/blob/master/

/

.py
"サンプルプログラム")は本プロジェクトの「

/

.py
」にも収録．


