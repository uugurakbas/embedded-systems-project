# Raspberry Pi Tabanlı Akıllı Sıcaklık ve Mesafe Kontrollü Servo Sistemi

Bu proje, **Raspberry Pi** kullanarak ortam sıcaklığına ve mesafeye bağlı olarak bir **servo motoru** kontrol etmeyi amaçlar. Sıcaklık belirli bir eşik değerini aştığında ve önünde güvenli bir mesafe varsa servo motor hareket eder. Bu sistem, örneğin bir **akıllı havalandırma** veya **uyarı sisteminde** kullanılabilir.

## 🚀 Projenin Amacı

- Ortam sıcaklığını **DHT11** sensörü ile ölçmek.
- Önündeki engeli **ultrasonik mesafe sensörü (HC-SR04)** ile algılamak.
- Belirli koşullarda **servo motor** çalıştırmak.
- Raspberry Pi GPIO pinlerini kullanarak gömülü sistem mantığını uygulamak.

---

## 🛠 Kullanılan Donanım Bileşenleri

- Raspberry Pi 3/4/5
- DHT11 Sıcaklık ve Nem Sensörü
- HC-SR04 Ultrasonik Mesafe Sensörü
- SG90 Servo Motor
- Jumper kablolar
- Breadboard

---

## 🧠 Sistem Mantığı

1. DHT11 ile sıcaklık ölçülür.
2. Eğer sıcaklık **27°C**'nin üzerindeyse:
   - HC-SR04 ile mesafe ölçülür.
   - Eğer mesafe **10 cm'den fazlaysa**, servo motor çalışır.
   - Aksi takdirde uyarı mesajı verilir.
3. Sıcaklık düşükse sistem bekleme modunda kalır.

---

## 🧾 Koddan Bir Kesit

``` python

if temperature > 27:
    print("Sicaklik Asildi!")
    
    if distance > 10:
        print("Mesafe Guvenli")
        servo_spin_loop()
    else:
        print("Dikkat, Lutfen uzak durunuz!")
```

---
## 📷 Devre Şeması

Aşağıda sistemde kullanılan sensör ve motorların Raspberry Pi GPIO pinlerine bağlantısı listelenmiştir:

### 🔹 DHT11 Sıcaklık ve Nem Sensörü
| DHT11 Pin | Raspberry Pi GPIO |
|-----------|-------------------|
| VCC       | 5V                |
| DATA      | GPIO14 (Pin 8)    |
| GND       | GND               |

### 🔹 HC-SR04 Ultrasonik Mesafe Sensörü
| HC-SR04 Pin | Raspberry Pi GPIO |
|-------------|-------------------|
| VCC         | 5V                |
| TRIG        | GPIO23            |
| ECHO        | GPIO24            |
| GND         | GND               |

### 🔹 SG90 Servo Motor
| Servo Pin | Raspberry Pi GPIO |
|-----------|-------------------|
| Sinyal    | GPIO12            |
| VCC       | 5V                |
| GND       | GND               |



