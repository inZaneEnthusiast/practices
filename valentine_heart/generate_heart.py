# generate_heart.py by GLM5
def draw_ascii_heart(height=25, border_char='#', inner_chars='*', density=0.1):
    """
    绘制空心爱心（纯ASCII字符）
    宽高比为2:1，在等宽字体下显示为正方形
    
    参数:
        height: 爱心高度（行数）
        border_char: 边框字符（ASCII字符）
        inner_chars: 内部装饰字符（ASCII字符组成的字符串）
        density: 内部装饰密度（0~1）
    
    返回:
        每行长度一致的字符串列表
    """
    import random
    
    # 宽度设为高度的2.7倍
    width = round(height * 2.7)
    lines = []
    
    for y in range(height, -1, -1):
        line = ""
        for x in range(width):
            # 归一化坐标到心形方程的标准范围
            nx = (x - width / 2) / (width / 3.0)
            ny = (y - height / 2) / (height / 2.5)
            
            # 垂直偏移，让爱心位置居中
            y_shift = ny + 0.12
            
            # 心形方程: (x² + y² - 1)³ - x²y³ < 0
            value = (nx * nx + y_shift * y_shift - 1) ** 3 - nx * nx * y_shift ** 3
            
            if value < 0:  # 在爱心内部
                # 检测边界
                border = False
                check_dist = 0.055
                for dx in [-check_dist, 0, check_dist]:
                    for dy in [-check_dist, 0, check_dist]:
                        if dx == 0 and dy == 0:
                            continue
                        test_x = nx + dx
                        test_y = y_shift + dy
                        test_val = (test_x * test_x + test_y * test_y - 1) ** 3 - test_x * test_x * test_y ** 3
                        if test_val >= 0:
                            border = True
                            break
                    if border:
                        break
                
                if border:
                    line += border_char
                else:
                    # 内部装饰
                    if inner_chars and random.random() < density:
                        line += random.choice(inner_chars)
                    else:
                        line += ' '
            else:
                line += ' '
        
        # 确保每行长度一致
        line = line.ljust(width)
        lines.append(line)
    
    return lines


# ============ 使用示例 ============
if __name__ == "__main__":
    # # 示例1：纯空心爱心
    # print("【纯空心爱心】")
    # print("=" * 50)
    # heart = draw_ascii_heart(height=22, border_char='#', inner_chars='', density=0)
    # for line in heart:
    #     print(line)
    
    # # 示例2：带装饰爱心
    # print("\n【带装饰爱心】")
    # print("=" * 50)
    # heart = draw_ascii_heart(height=28, border_char='#', inner_chars='*', density=0.08)
    # for line in heart:
    #     print(line)
    
    # # 示例3：大号爱心
    # print("\n【大号爱心】")
    # print("=" * 50)
    heart = draw_ascii_heart(height=35, border_char='#', inner_chars='.*+o', density=0.1)
    # print(heart)
    for line in heart:
        print("0" + line)
