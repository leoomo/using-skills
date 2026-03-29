# ESS内部布局模板

本文档提供6种ESS内部布局模板，适用于分体式储能柜和集装箱式储能系统的场地规划。

## 模板列表

| # | 模板名称 | 适用场景 | 设备数量/规格 |
|---|---------|---------|--------------|
| 1 | 分体式ESS布局(5×2) | 10台MC-L430 | 10台 |
| 2 | 分体式ESS布局(3×4) | 12台MC-L430 | 12台 |
| 3 | 集装箱ESS内部布局 | WS-L4300 | 1台20ft/40ft |
| 4 | 电池簇详细布局 | 电池模组排列 | N/A |
| 5 | PCS堆叠布局 | 多台PCS并联 | N/A |
| 6 | ESS设备清单表格 | 项目设备统计 | N/A |

---

## 模板1：分体式ESS布局（5×2排列）

**适用场景：** 10台MC-L430储能柜的标准布局。

**布局说明：**
- 5列 × 2排 = 10台储能柜
- 每台设备间距1.5m（IEC 62619安全间距）
- 通道宽度2m
- 总占地面积约75-85m²

```xml
<mxGraphModel>
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>

    <!-- 标题 -->
    <mxCell id="title" value="分体式ESS布局 (5×2排列)&#xa;10×MC-L430" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="200" y="20" width="400" height="50" as="geometry"/>
    </mxCell>

    <!-- ESS区域边界 -->
    <mxCell id="ess_area" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#6C8EBF;strokeWidth=2;dashed=1;dashPattern=8 8" vertex="1" parent="1">
      <mxGeometry x="100" y="100" width="600" height="350" as="geometry"/>
    </mxCell>

    <mxCell id="ess_area_label" value="ESS储能区" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;fontStyle=1;fontColor=#6C8EBF" vertex="1" parent="1">
      <mxGeometry x="110" y="105" width="100" height="20" as="geometry"/>
    </mxCell>

    <!-- MC-L430 #1 -->
    <mxCell id="mc1" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="120" y="140" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="mc1_label" value="#1" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="120" y="210" width="50" height="20" as="geometry"/>
    </mxCell>

    <!-- MC-L430 #2 -->
    <mxCell id="mc2" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="190" y="140" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="mc2_label" value="#2" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="190" y="210" width="50" height="20" as="geometry"/>
    </mxCell>

    <!-- MC-L430 #3 -->
    <mxCell id="mc3" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="260" y="140" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="mc3_label" value="#3" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="260" y="210" width="50" height="20" as="geometry"/>
    </mxCell>

    <!-- MC-L430 #4 -->
    <mxCell id="mc4" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="330" y="140" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="mc4_label" value="#4" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="330" y="210" width="50" height="20" as="geometry"/>
    </mxCell>

    <!-- MC-L430 #5 -->
    <mxCell id="mc5" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="400" y="140" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="mc5_label" value="#5" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="400" y="210" width="50" height="20" as="geometry"/>
    </mxCell>

    <!-- 第二排 -->

    <!-- MC-L430 #6 -->
    <mxCell id="mc6" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="120" y="280" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="mc6_label" value="#6" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="120" y="350" width="50" height="20" as="geometry"/>
    </mxCell>

    <!-- MC-L430 #7 -->
    <mxCell id="mc7" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="190" y="280" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="mc7_label" value="#7" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="190" y="350" width="50" height="20" as="geometry"/>
    </mxCell>

    <!-- MC-L430 #8 -->
    <mxCell id="mc8" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="260" y="280" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="mc8_label" value="#8" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="260" y="350" width="50" height="20" as="geometry"/>
    </mxCell>

    <!-- MC-L430 #9 -->
    <mxCell id="mc9" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="330" y="280" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="mc9_label" value="#9" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="330" y="350" width="50" height="20" as="geometry"/>
    </mxCell>

    <!-- MC-L430 #10 -->
    <mxCell id="mc10" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="400" y="280" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="mc10_label" value="#10" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="400" y="350" width="50" height="20" as="geometry"/>
    </mxCell>

    <!-- EMS控制柜 -->
    <mxCell id="ems_cabinet" value="EMS&#xa;控制柜" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="500" y="180" width="80" height="80" as="geometry"/>
    </mxCell>

    <!-- STS柜 -->
    <mxCell id="sts_cabinet" value="STS&#xa;切换柜" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="500" y="280" width="80" height="60" as="geometry"/>
    </mxCell>

    <!-- 尺寸标注 -->
    <mxCell id="dim_width" value="~15m" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="300" y="420" width="60" height="20" as="geometry"/>
    </mxCell>

    <mxCell id="dim_height" value="~6m" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="700" y="200" width="40" height="20" as="geometry"/>
    </mxCell>

    <!-- 间距标注 -->
    <mxCell id="spacing_note" value="设备间距: 1.5m&#xa;通道宽度: 2m" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=9;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="110" y="400" width="100" height="40" as="geometry"/>
    </mxCell>

    <!-- 总容量标注 -->
    <mxCell id="total_cap" value="总容量: 4.3MWh / 2MW&#xa;(10×MC-L430-2H3)" style="text;html=1;strokeColor=none;fillColor=none;align=right;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1;fontColor=#6C8EBF" vertex="1" parent="1">
      <mxGeometry x="520" y="380" width="150" height="40" as="geometry"/>
    </mxCell>

  </root>
</mxGraphModel>
```

---

## 模板2：分体式ESS布局（3×4排列）

**适用场景：** 12台MC-L430储能柜的紧凑布局。

**布局说明：**
- 4列 × 3排 = 12台储能柜
- 适合场地受限的项目
- 设备间距1.2m（最小间距）
- 总占地面积约60-70m²

```xml
<mxGraphModel>
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>

    <!-- 标题 -->
    <mxCell id="title" value="分体式ESS布局 (3×4排列)&#xa;12×MC-L430" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="200" y="20" width="400" height="50" as="geometry"/>
    </mxCell>

    <!-- ESS区域边界 -->
    <mxCell id="ess_area" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#6C8EBF;strokeWidth=2;dashed=1;dashPattern=8 8" vertex="1" parent="1">
      <mxGeometry x="80" y="100" width="520" height="380" as="geometry"/>
    </mxCell>

    <mxCell id="ess_area_label" value="ESS储能区" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;fontStyle=1;fontColor=#6C8EBF" vertex="1" parent="1">
      <mxGeometry x="90" y="105" width="100" height="20" as="geometry"/>
    </mxCell>

    <!-- 第一排 -->
    <mxCell id="mc1" value="#1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="100" y="140" width="50" height="60" as="geometry"/>
    </mxCell>

    <mxCell id="mc2" value="#2" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="170" y="140" width="50" height="60" as="geometry"/>
    </mxCell>

    <mxCell id="mc3" value="#3" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="240" y="140" width="50" height="60" as="geometry"/>
    </mxCell>

    <mxCell id="mc4" value="#4" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="310" y="140" width="50" height="60" as="geometry"/>
    </mxCell>

    <!-- 第二排 -->
    <mxCell id="mc5" value="#5" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="100" y="220" width="50" height="60" as="geometry"/>
    </mxCell>

    <mxCell id="mc6" value="#6" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="170" y="220" width="50" height="60" as="geometry"/>
    </mxCell>

    <mxCell id="mc7" value="#7" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="240" y="220" width="50" height="60" as="geometry"/>
    </mxCell>

    <mxCell id="mc8" value="#8" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="310" y="220" width="50" height="60" as="geometry"/>
    </mxCell>

    <!-- 第三排 -->
    <mxCell id="mc9" value="#9" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="100" y="300" width="50" height="60" as="geometry"/>
    </mxCell>

    <mxCell id="mc10" value="#10" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="170" y="300" width="50" height="60" as="geometry"/>
    </mxCell>

    <mxCell id="mc11" value="#11" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="240" y="300" width="50" height="60" as="geometry"/>
    </mxCell>

    <mxCell id="mc12" value="#12" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="310" y="300" width="50" height="60" as="geometry"/>
    </mxCell>

    <!-- EMS和STS控制柜 -->
    <mxCell id="ems_cabinet" value="EMS" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="400" y="180" width="60" height="60" as="geometry"/>
    </mxCell>

    <mxCell id="sts_cabinet" value="STS" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="480" y="180" width="60" height="60" as="geometry"/>
    </mxCell>

    <!-- 通道 -->
    <mxCell id="aisle" value="通道 2m" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontColor=#999999" vertex="1" parent="1">
      <mxGeometry x="100" y="195" width="260" height="20" as="geometry"/>
    </mxCell>

    <!-- 尺寸标注 -->
    <mxCell id="dim_note" value="紧凑布局: 设备间距1.2m" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=9;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="90" y="400" width="150" height="20" as="geometry"/>
    </mxCell>

    <!-- 总容量 -->
    <mxCell id="total_cap" value="总容量: 5.16MWh / 2.4MW&#xa;(12×MC-L430-2H3)" style="text;html=1;strokeColor=none;fillColor=none;align=right;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1;fontColor=#6C8EBF" vertex="1" parent="1">
      <mxGeometry x="380" y="400" width="180" height="40" as="geometry"/>
    </mxCell>

  </root>
</mxGraphModel>
```

---

## 模板3：集装箱ESS内部布局（WS-L4300）

**适用场景：** WS-L4300液冷储能集装箱的内部设备布局。

**布局说明：**
- 20ft或40ft标准集装箱
- 集成电池、PCS、BMS、消防、空调
- 设备间距和通道需满足维护要求

```xml
<mxGraphModel>
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>

    <!-- 标题 -->
    <mxCell id="title" value="集装箱ESS内部布局 (WS-L4300)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="200" y="20" width="400" height="30" as="geometry"/>
    </mxCell>

    <!-- 集装箱外壳 -->
    <mxCell id="container" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#666666;strokeWidth=3" vertex="1" parent="1">
      <mxGeometry x="80" y="70" width="640" height="380" as="geometry"/>
    </mxCell>

    <mxCell id="container_label" value="WS-L4300-BC-3 液冷储能集装箱 (40ft)" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;fontStyle=1;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="90" y="75" width="300" height="20" as="geometry"/>
    </mxCell>

    <!-- 电池区 -->
    <mxCell id="battery_zone" value="电池区&#xa;(电池簇×8)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="100" y="110" width="280" height="200" as="geometry"/>
    </mxCell>

    <!-- 电池簇1-4 -->
    <mxCell id="bc1" value="#1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#CAE8FC;strokeColor=#6C8EBF;fontSize=9" vertex="1" parent="1">
      <mxGeometry x="110" y="130" width="60" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="bc2" value="#2" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#CAE8FC;strokeColor=#6C8EBF;fontSize=9" vertex="1" parent="1">
      <mxGeometry x="180" y="130" width="60" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="bc3" value="#3" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#CAE8FC;strokeColor=#6C8EBF;fontSize=9" vertex="1" parent="1">
      <mxGeometry x="250" y="130" width="60" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="bc4" value="#4" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#CAE8FC;strokeColor=#6C8EBF;fontSize=9" vertex="1" parent="1">
      <mxGeometry x="320" y="130" width="50" height="80" as="geometry"/>
    </mxCell>

    <!-- 电池簇5-8 -->
    <mxCell id="bc5" value="#5" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#CAE8FC;strokeColor=#6C8EBF;fontSize=9" vertex="1" parent="1">
      <mxGeometry x="110" y="220" width="60" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="bc6" value="#6" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#CAE8FC;strokeColor=#6C8EBF;fontSize=9" vertex="1" parent="1">
      <mxGeometry x="180" y="220" width="60" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="bc7" value="#7" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#CAE8FC;strokeColor=#6C8EBF;fontSize=9" vertex="1" parent="1">
      <mxGeometry x="250" y="220" width="60" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="bc8" value="#8" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#CAE8FC;strokeColor=#6C8EBF;fontSize=9" vertex="1" parent="1">
      <mxGeometry x="320" y="220" width="50" height="80" as="geometry"/>
    </mxCell>

    <!-- PCS区 -->
    <mxCell id="pcs_zone" value="PCS区&#xa;(2MW)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="400" y="110" width="140" height="100" as="geometry"/>
    </mxCell>

    <!-- BMS控制柜 -->
    <mxCell id="bms_zone" value="BMS&#xa;控制柜" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="560" y="110" width="80" height="100" as="geometry"/>
    </mxCell>

    <!-- 空调区 -->
    <mxCell id="ac_zone" value="空调系统&#xa;(液冷)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="400" y="230" width="140" height="80" as="geometry"/>
    </mxCell>

    <!-- 消防区 -->
    <mxCell id="fire_zone" value="消防系统" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="560" y="230" width="80" height="80" as="geometry"/>
    </mxCell>

    <!-- EMS控制台 -->
    <mxCell id="ems_zone" value="EMS&#xa;控制台" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="560" y="330" width="80" height="60" as="geometry"/>
    </mxCell>

    <!-- 变压器接口 -->
    <mxCell id="transformer_interface" value="变压器接口&#xa;(690V输出)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=9" vertex="1" parent="1">
      <mxGeometry x="400" y="330" width="140" height="60" as="geometry"/>
    </mxCell>

    <!-- 维护通道 -->
    <mxCell id="aisle_front" value="前维护通道 1.5m" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontColor=#999999" vertex="1" parent="1">
      <mxGeometry x="100" y="320" width="280" height="20" as="geometry"/>
    </mxCell>

    <!-- 技术参数 -->
    <mxCell id="tech_specs" value="技术参数:&#xa;- 容量: 4.3MWh / 2MW&#xa;- 电压: 690V AC输出&#xa;- 尺寸: 40ft (12.2m×2.4m×2.9m)&#xa;- 消防: 七氟丙烷/水消防&#xa;- 空调: 液冷温控" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=9;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="80" y="460" width="200" height="80" as="geometry"/>
    </mxCell>

  </root>
</mxGraphModel>
```

---

## 模板4：电池簇详细布局

**适用场景：** 展示电池簇内部结构和电池模组排列。

**布局说明：**
- 单簇电池详细结构
- 电池模组排列
- BMS和冷却系统

```xml
<mxGraphModel>
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>

    <!-- 标题 -->
    <mxCell id="title" value="电池簇详细布局" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="200" y="20" width="400" height="30" as="geometry"/>
    </mxCell>

    <!-- 电池簇外壳 -->
    <mxCell id="cluster_enclosure" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=2" vertex="1" parent="1">
      <mxGeometry x="100" y="70" width="500" height="250" as="geometry"/>
    </mxCell>

    <mxCell id="cluster_label" value="电池簇 (Battery Cluster)&#xa;100kWh / 50kW" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;fontStyle=1;fontColor=#1A3D5C" vertex="1" parent="1">
      <mxGeometry x="110" y="75" width="200" height="40" as="geometry"/>
    </mxCell>

    <!-- Pack 1 -->
    <mxCell id="pack1" value="Pack #1&#xa;25kWh" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#CAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="120" y="130" width="70" height="80" as="geometry"/>
    </mxCell>

    <!-- Pack 2 -->
    <mxCell id="pack2" value="Pack #2&#xa;25kWh" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#CAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="200" y="130" width="70" height="80" as="geometry"/>
    </mxCell>

    <!-- Pack 3 -->
    <mxCell id="pack3" value="Pack #3&#xa;25kWh" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#CAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="280" y="130" width="70" height="80" as="geometry"/>
    </mxCell>

    <!-- Pack 4 -->
    <mxCell id="pack4" value="Pack #4&#xa;25kWh" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#CAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="360" y="130" width="70" height="80" as="geometry"/>
    </mxCell>

    <!-- BMS控制 -->
    <mxCell id="bms" value="BMS&#xa;控制" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="450" y="130" width="80" height="80" as="geometry"/>
    </mxCell>

    <!-- 冷却系统 -->
    <mxCell id="cooling" value="冷却系统" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="120" y="230" width="200" height="60" as="geometry"/>
    </mxCell>

    <!-- 高压箱 -->
    <mxCell id="hv_box" value="高压箱" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="340" y="230" width="100" height="60" as="geometry"/>
    </mxCell>

    <!-- 电气接口 -->
    <mxCell id="elec_if" value="电气接口" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="460" y="230" width="80" height="60" as="geometry"/>
    </mxCell>

    <!-- 模组详情 -->
    <mxCell id="module_detail" value="每Pack包含: 7个电池模组 (3.57kWh/模组)&#xa;每模组: 1P24S (LFP 280Ah)" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=9;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="100" y="340" width="300" height="40" as="geometry"/>
    </mxCell>

    <!-- 规格参数 -->
    <mxCell id="specs" value="规格:&#xa;- 标称电压: 1280V&#xa;- 容量: 100Ah&#xa;- 循环寿命: 6000+ cycles&#xa;- 防护等级: IP55" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=9;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="450" y="320" width="150" height="80" as="geometry"/>
    </mxCell>

  </root>
</mxGraphModel>
```

---

## 模板5：PCS堆叠布局

**适用场景：** 多台PCS并联安装的布局。

**布局说明：**
- PCS并联配置
- 电气接线
- 散热要求

```xml
<mxGraphModel>
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>

    <!-- 标题 -->
    <mxCell id="title" value="PCS堆叠布局 (多机并联)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="200" y="20" width="400" height="30" as="geometry"/>
    </mxCell>

    <!-- PCS区域边界 -->
    <mxCell id="pcs_area" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#9673A6;strokeWidth=2;dashed=1;dashPattern=8 8" vertex="1" parent="1">
      <mxGeometry x="100" y="70" width="500" height="300" as="geometry"/>
    </mxCell>

    <mxCell id="pcs_area_label" value="PCS区" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;fontStyle=1;fontColor=#9673A6" vertex="1" parent="1">
      <mxGeometry x="110" y="75" width="80" height="20" as="geometry"/>
    </mxCell>

    <!-- PCS #1 -->
    <mxCell id="pcs1" value="PCS #1&#xa;500kW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="120" y="110" width="100" height="80" as="geometry"/>
    </mxCell>

    <!-- PCS #2 -->
    <mxCell id="pcs2" value="PCS #2&#xa;500kW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="240" y="110" width="100" height="80" as="geometry"/>
    </mxCell>

    <!-- PCS #3 -->
    <mxCell id="pcs3" value="PCS #3&#xa;500kW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="360" y="110" width="100" height="80" as="geometry"/>
    </mxCell>

    <!-- PCS #4 -->
    <mxCell id="pcs4" value="PCS #4&#xa;500kW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="480" y="110" width="100" height="80" as="geometry"/>
    </mxCell>

    <!-- 交流母线 -->
    <mxCell id="ac_bus_pcs" value="AC Bus&#xa;400V/690V" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="120" y="220" width="460" height="60" as="geometry"/>
    </mxCell>

    <!-- 直流配电 -->
    <mxCell id="dc_dist" value="直流配电" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="120" y="310" width="100" height="50" as="geometry"/>
    </mxCell>

    <!-- 变压器接口 -->
    <mxCell id="trafo_if" value="变压器接口" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="480" y="310" width="100" height="50" as="geometry"/>
    </mxCell>

    <!-- 并联说明 -->
    <mxCell id="parallel_note" value="并联运行: 4×500kW = 2MW&#xa;负载自动分配&#xa;N+1冗余可选" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=9;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="250" y="380" width="200" height="50" as="geometry"/>
    </mxCell>

    <!-- 技术要求 -->
    <mxCell id="tech_req" value="散热要求: 风冷/液冷&#xa;间距: &gt;0.8m" style="text;html=1;strokeColor=none;fillColor=none;align=right;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=9;fontColor=#999999" vertex="1" parent="1">
      <mxGeometry x="420" y="380" width="150" height="40" as="geometry"/>
    </mxCell>

  </root>
</mxGraphModel>
```

---

## 模板6：ESS设备清单表格

**适用场景：** 项目设备统计和清单展示。

```xml
<mxGraphModel>
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>

    <!-- 标题 -->
    <mxCell id="title" value="ESS设备清单" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="200" y="20" width="400" height="40" as="geometry"/>
    </mxCell>

    <!-- 项目信息 -->
    <mxCell id="project_info" value="项目: Ketzin光储项目 | 容量: 4.3MWh / 2MW" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="200" y="60" width="400" height="25" as="geometry"/>
    </mxCell>

    <!-- 表格边框 -->
    <mxCell id="table_border" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;" vertex="1" parent="1">
      <mxGeometry x="80" y="100" width="540" height="320" as="geometry"/>
    </mxCell>

    <!-- 表头 -->
    <mxCell id="header1" value="序号" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#6C8EBF;strokeColor=#666666;fontSize=11;fontStyle=1;fontColor=#FFFFFF" vertex="1" parent="1">
      <mxGeometry x="80" y="100" width="50" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="header2" value="设备名称" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#6C8EBF;strokeColor=#666666;fontSize=11;fontStyle=1;fontColor=#FFFFFF" vertex="1" parent="1">
      <mxGeometry x="130" y="100" width="150" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="header3" value="型号规格" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#6C8EBF;strokeColor=#666666;fontSize=11;fontStyle=1;fontColor=#FFFFFF" vertex="1" parent="1">
      <mxGeometry x="280" y="100" width="180" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="header4" value="数量" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#6C8EBF;strokeColor=#666666;fontSize=11;fontStyle=1;fontColor=#FFFFFF" vertex="1" parent="1">
      <mxGeometry x="460" y="100" width="60" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="header5" value="备注" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#6C8EBF;strokeColor=#666666;fontSize=11;fontStyle=1;fontColor=#FFFFFF" vertex="1" parent="1">
      <mxGeometry x="520" y="100" width="100" height="30" as="geometry"/>
    </mxCell>

    <!-- 行1 -->
    <mxCell id="row1_1" value="1" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="80" y="130" width="50" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row1_2" value="分体式储能柜" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="130" y="130" width="150" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row1_3" value="MC-L430-2H3 (430kWh/200kW)" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="280" y="130" width="180" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row1_4" value="10" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="460" y="130" width="60" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row1_5" value="" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="520" y="130" width="100" height="30" as="geometry"/>
    </mxCell>

    <!-- 行2 -->
    <mxCell id="row2_1" value="2" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="80" y="160" width="50" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row2_2" value="EMS能量管理系统" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="130" y="160" width="150" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row2_3" value="MS-EMS" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="280" y="160" width="180" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row2_4" value="1" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="460" y="160" width="60" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row2_5" value="" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="520" y="160" width="100" height="30" as="geometry"/>
    </mxCell>

    <!-- 行3 -->
    <mxCell id="row3_1" value="3" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="80" y="190" width="50" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row3_2" value="STS静态转换开关" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="130" y="190" width="150" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row3_3" value="MS-TS500" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="280" y="190" width="180" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row3_4" value="4" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="460" y="190" width="60" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row3_5" value="" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="520" y="190" width="100" height="30" as="geometry"/>
    </mxCell>

    <!-- 行4 -->
    <mxCell id="row4_1" value="4" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="80" y="220" width="50" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row4_2" value="升压变压器" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="130" y="220" width="150" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row4_3" value="2000kVA, 400V/20kV" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="280" y="220" width="180" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row4_4" value="1" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="460" y="220" width="60" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row4_5" value="客户现有" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="520" y="220" width="100" height="30" as="geometry"/>
    </mxCell>

    <!-- 行5 -->
    <mxCell id="row5_1" value="5" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="80" y="250" width="50" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row5_2" value="中压开关站" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="130" y="250" width="150" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row5_3" value="J08, 20kV" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="280" y="250" width="180" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row5_4" value="1" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="460" y="250" width="60" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row5_5" value="" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="520" y="250" width="100" height="30" as="geometry"/>
    </mxCell>

    <!-- 行6 -->
    <mxCell id="row6_1" value="6" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="80" y="280" width="50" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row6_2" value="光伏组件" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="130" y="280" width="150" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row6_3" value="2MWp" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="280" y="280" width="180" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row6_4" value="1" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="460" y="280" width="60" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row6_5" value="" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="520" y="280" width="100" height="30" as="geometry"/>
    </mxCell>

    <!-- 行7 -->
    <mxCell id="row7_1" value="7" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="80" y="310" width="50" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row7_2" value="组串逆变器" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="130" y="310" width="150" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row7_3" value="交流侧" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="280" y="310" width="180" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row7_4" value="1" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="460" y="310" width="60" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row7_5" value="" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="520" y="310" width="100" height="30" as="geometry"/>
    </mxCell>

    <!-- 行8 -->
    <mxCell id="row8_1" value="8" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="80" y="340" width="50" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row8_2" value="消防系统" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="130" y="340" width="150" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row8_3" value="七氟丙烷/水消防" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="280" y="340" width="180" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row8_4" value="1" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="460" y="340" width="60" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row8_5" value="" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="520" y="340" width="100" height="30" as="geometry"/>
    </mxCell>

    <!-- 行9 -->
    <mxCell id="row9_1" value="9" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="80" y="370" width="50" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row9_2" value="空调系统" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="130" y="370" width="150" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row9_3" value="液冷温控" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="280" y="370" width="180" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row9_4" value="1" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="460" y="370" width="60" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="row9_5" value="" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="520" y="370" width="100" height="30" as="geometry"/>
    </mxCell>

    <!-- 合计 -->
    <mxCell id="total_label" value="合计容量:" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#E6E6E6;strokeColor=#666666;fontSize=11;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="80" y="410" width="200" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="total_value" value="储能: 4.3MWh / 2MW | 光伏: 2MWp" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=11;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="280" y="410" width="340" height="30" as="geometry"/>
    </mxCell>

  </root>
</mxGraphModel>
```

---

## 使用说明

1. **选择模板**：根据项目类型选择分体式或集装箱布局
2. **复制XML**：将模板的完整 XML 代码复制
3. **导入draw.io**：创建新文件并导入 XML
4. **自定义修改**：
   - 修改设备数量和排列
   - 调整间距和通道
   - 更新设备型号参数
5. **计算占地**：根据布局计算实际占地面积
