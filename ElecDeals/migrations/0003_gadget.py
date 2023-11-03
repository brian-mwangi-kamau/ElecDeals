# Generated by Django 4.2.6 on 2023-11-03 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElecDeals', '0002_customuser_is_active_customuser_is_admin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gadget',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50)),
                ('item_description', models.TextField(max_length=1000)),
                ('item_color', models.CharField(choices=[('black', 'Black'), ('silver', 'Silver'), ('white', 'White'), ('space grey', 'Space grey'), ('rose gold', 'Rose gold'), ('red', 'Red'), ('blue', 'Blue')], max_length=50)),
                ('item_brand', models.CharField(choices=[('apple', 'Apple'), ('samsung', 'Samsung'), ('dell', 'Dell'), ('hp', 'HP'), ('lenovo', 'Lenovo'), ('acer', 'Acer'), ('asus', 'Asus')], max_length=50)),
                ('item_os', models.CharField(choices=[('windows', 'Windows'), ('ios', 'iOS'), ('linux', 'Linux'), ('macos', 'macOS'), ('chromeos', 'ChromeOS'), ('android', 'Android'), ('harmonyos', 'HarmonyOS')], max_length=50)),
                ('item_type', models.CharField(choices=[('smartphone', 'Smartphone'), ('laptop', 'Laptop'), ('desktop', 'Desktop'), ('tablet', 'Tablet'), ('ultrabook', 'Ultrabook'), ('gaming laptop', 'Gaming Laptop'), ('2-in-1 laptop', '2-in-1 Laptop')], max_length=50)),
                ('item_capacity', models.CharField(choices=[('8gb ram', '8GB RAM'), ('16gb ram', '16GB RAM'), ('512gb ssd', '512GB SSD'), ('1tb hdd', '1TB HDD'), ('256gb nvme', '256GB NVMe')], max_length=50)),
                ('item_features', models.CharField(choices=[('Touchscreen', 'Touchscreen'), ('Backlit_Keyboard', 'Backlit Keyboard'), ('Gaming', 'Gaming'), ('Convertible', 'Convertible'), ('High_Resolution_Display', 'High-Resolution Display'), ('Thin_and_Light', 'Thin and Light'), ('Business_Laptop', 'Business Laptop'), ('Stylus_Support', 'Stylus Support'), ('4G_LTE', '4G LTE'), ('5G', '5G'), ('Wi_Fi_6', 'Wi-Fi 6'), ('Bluetooth', 'Bluetooth'), ('USB_C', 'USB-C'), ('HDMI_Port', 'HDMI Port'), ('Laptop_Bag_Included', 'Laptop Bag Included'), ('External_GPU_Support', 'External GPU Support'), ('Biometric_Security', 'Biometric Security'), ('Webcam', 'Webcam'), ('Noise_Cancellation', 'Noise Cancellation'), ('RGB_Keyboard', 'RGB Keyboard'), ('Dual_Sim_Support', 'Dual SIM Support')], max_length=50)),
                ('item_image', models.ImageField(upload_to='files/')),
                ('item_price', models.IntegerField()),
            ],
        ),
    ]
