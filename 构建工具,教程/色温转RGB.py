import math

def color_temperature_to_rgb(kelvin):
    temp = kelvin / 100.0

    # 红色分量
    if temp <= 66:
        red = 255
    else:
        red = 329.698727446 * ((temp - 60) ** -0.1332047592)
        red = max(0, min(255, red))

    # 绿色分量
    if temp <= 66:
        green = 99.4708025861 * math.log(temp) - 161.1195681661
    else:
        green = 288.1221695283 * ((temp - 60) ** -0.0755148492)
    green = max(0, min(255, green))

    # 蓝色分量
    if temp >= 66:
        blue = 255
    elif temp <= 19:
        blue = 0
    else:
        blue = 138.5177312231 * math.log(temp - 10) - 305.0447927307
        blue = max(0, min(255, blue))

    return (red, green, blue)

def main():
    print(" 色温 → RGB 转换工具（支持 1000K ~ 40000K）")
    kelvin = float(input("请输入色温 (K)："))
    r, g, b = color_temperature_to_rgb(kelvin)
    print(f"\n结果：RGB = ({r:.2f}, {g:.2f}, {b:.2f})")
    print(f"归一化值：({r/255:.3f}, {g/255:.3f}, {b/255:.3f})")
    print(f"HEX = #{int(r):02X}{int(g):02X}{int(b):02X}")

if __name__ == "__main__":
    main()